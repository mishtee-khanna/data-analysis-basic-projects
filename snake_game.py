import random
import tkinter as tk


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.configure(bg="#111827")
        self.root.resizable(False, False)

        self.grid_size = 20
        self.cell_size = 20
        self.width = self.grid_size * self.cell_size
        self.height = self.grid_size * self.cell_size

        self.root.geometry(f"{self.width + 20}x{self.height + 80}")

        self.score = 0
        self.speed = 150
        self.direction = "Right"
        self.next_direction = "Right"
        self.running = True

        self.canvas = tk.Canvas(
            root,
            width=self.width,
            height=self.height,
            bg="black",
            highlightthickness=0,
        )
        self.canvas.pack(pady=(10, 0))

        self.info_frame = tk.Frame(root, bg="#111827")
        self.info_frame.pack(fill="x", pady=10)

        self.score_label = tk.Label(
            self.info_frame,
            text="Score: 0",
            font=("Arial", 14, "bold"),
            fg="#e2e8f0",
            bg="#111827",
        )
        self.score_label.pack(side="left", padx=15)

        self.restart_button = tk.Button(
            self.info_frame,
            text="Restart",
            font=("Arial", 12, "bold"),
            bg="#22c55e",
            fg="white",
            relief="flat",
            command=self.reset_game,
        )
        self.restart_button.pack(side="right", padx=15)

        self.status_label = tk.Label(
            self.info_frame,
            text="Use arrow keys or WASD",
            font=("Arial", 11),
            fg="#cbd5e1",
            bg="#111827",
        )
        self.status_label.pack(side="left", padx=15)

        self.root.bind("<KeyPress>", self.on_key_press)

        self.reset_game()

    def reset_game(self):
        self.score = 0
        self.speed = 150
        self.direction = "Right"
        self.next_direction = "Right"
        self.running = True
        self.score_label.config(text="Score: 0")
        self.status_label.config(text="Use arrow keys or WASD")

        self.snake = [
            [self.grid_size // 2, self.grid_size // 2],
            [self.grid_size // 2 - 1, self.grid_size // 2],
            [self.grid_size // 2 - 2, self.grid_size // 2],
        ]

        self.food = self.spawn_food()
        self.draw_board()
        self.update_game()

    def spawn_food(self):
        while True:
            food = [
                random.randint(0, self.grid_size - 1),
                random.randint(0, self.grid_size - 1),
            ]
            if food not in self.snake:
                return food

    def draw_board(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(
            0,
            0,
            self.width,
            self.height,
            fill="#0b1220",
            outline="#0b1220",
            width=0,
        )

        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(
                x * self.cell_size,
                y * self.cell_size,
                (x + 1) * self.cell_size,
                (y + 1) * self.cell_size,
                fill="#22c55e",
                outline="#15803d",
                width=1,
            )

        fx, fy = self.food
        self.canvas.create_rectangle(
            fx * self.cell_size,
            fy * self.cell_size,
            (fx + 1) * self.cell_size,
            (fy + 1) * self.cell_size,
            fill="#ef4444",
            outline="#991b1b",
            width=1,
        )

    def on_key_press(self, event):
        if event.keysym == "Return":
            if not self.running:
                self.reset_game()
            return

        if not self.running:
            return

        key = event.keysym.lower()
        mapping = {
            "up": "Up",
            "w": "Up",
            "down": "Down",
            "s": "Down",
            "left": "Left",
            "a": "Left",
            "right": "Right",
            "d": "Right",
        }

        new_direction = mapping.get(key)
        if not new_direction:
            return

        opposite = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left",
        }

        if new_direction != opposite.get(self.direction, None):
            self.next_direction = new_direction

    def move_snake(self):
        self.direction = self.next_direction

        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            new_head = [head_x, head_y - 1]
        elif self.direction == "Down":
            new_head = [head_x, head_y + 1]
        elif self.direction == "Left":
            new_head = [head_x - 1, head_y]
        else:
            new_head = [head_x + 1, head_y]

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.speed = max(60, self.speed - 5)
            self.score_label.config(text=f"Score: {self.score}")
            self.food = self.spawn_food()
        else:
            self.snake.pop()

        if (
            new_head[0] < 0
            or new_head[0] >= self.grid_size
            or new_head[1] < 0
            or new_head[1] >= self.grid_size
            or new_head in self.snake[1:]
        ):
            self.running = False
            self.status_label.config(text="Game Over! Press Enter to restart.")
            return

    def update_game(self):
        if self.running:
            self.move_snake()
            self.draw_board()
            self.root.after(self.speed, self.update_game)


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
