import random
def game_win(user, computer):
    if user == computer:
        return None

    # Snake Vs Gun
    if user == "snake" and computer == "gun":
        return False
    if user == "gun" and computer == "snake":
        return True

    # Water vs Gun
    if user == "water" and computer == "gun":
        return True
    if user == "gun" and computer == "water":
        return False

    # Water vs Snake
    if user == "snake" and computer == "water":
        return True
    if user == "water" and computer == "snake":
        return False
    

rand_no = random.randint(1,3)
print("Computer's turn : ")
if rand_no == 1:
    computer = "snake"
if rand_no == 2:
    computer = "water"
else:
    computer = "gun"

user =  input("Your turn : ")

result = game_win(user, computer)

print(f"You chose : {user}")
print(f"Computer chose : {computer}")

if result == None:
    print("It's a draw game")

elif result:
    print("You win!!")
else:
    print("Computer Wins!!")