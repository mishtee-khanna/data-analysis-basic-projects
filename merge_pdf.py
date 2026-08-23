import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

from pypdf import PdfWriter


class PdfMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.resizable(False, False)
        self.pdf_paths = []

        frame = tk.Frame(root, padx=16, pady=16)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="PDF files (merged in this order):").pack(anchor="w")
        self.file_list = tk.Listbox(frame, width=65, height=10)
        self.file_list.pack(fill="both", pady=(4, 8))

        buttons = tk.Frame(frame)
        buttons.pack(fill="x")
        tk.Button(buttons, text="Add PDFs", command=self.add_pdfs).pack(side="left")
        tk.Button(buttons, text="Remove selected", command=self.remove_selected).pack(
            side="left", padx=6
        )
        tk.Button(buttons, text="Move up", command=lambda: self.move_selected(-1)).pack(
            side="left"
        )
        tk.Button(buttons, text="Move down", command=lambda: self.move_selected(1)).pack(
            side="left", padx=6
        )
        tk.Button(frame, text="Merge PDFs", command=self.merge_pdfs).pack(pady=(12, 0))

    def add_pdfs(self):
        paths = filedialog.askopenfilenames(
            title="Choose PDF files", filetypes=[("PDF files", "*.pdf")]
        )
        for path in paths:
            if path not in self.pdf_paths:
                self.pdf_paths.append(path)
                self.file_list.insert(tk.END, Path(path).name)

    def remove_selected(self):
        selected = self.file_list.curselection()
        if selected:
            index = selected[0]
            del self.pdf_paths[index]
            self.file_list.delete(index)

    def move_selected(self, direction):
        selected = self.file_list.curselection()
        if not selected:
            return
        index = selected[0]
        new_index = index + direction
        if not 0 <= new_index < len(self.pdf_paths):
            return
        self.pdf_paths[index], self.pdf_paths[new_index] = (
            self.pdf_paths[new_index],
            self.pdf_paths[index],
        )
        filename = self.file_list.get(index)
        self.file_list.delete(index)
        self.file_list.insert(new_index, filename)
        self.file_list.selection_set(new_index)

    def merge_pdfs(self):
        if not self.pdf_paths:
            messagebox.showwarning("No files selected", "Add at least one PDF file first.")
            return

        output_path = filedialog.asksaveasfilename(
            title="Save merged PDF as",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialfile="merged.pdf",
        )
        if not output_path:
            return

        writer = PdfWriter()
        try:
            for pdf_path in self.pdf_paths:
                writer.append(pdf_path)
            with open(output_path, "wb") as output_file:
                writer.write(output_file)
        except Exception as error:
            messagebox.showerror("Merge failed", f"Could not merge the PDFs.\n\n{error}")
            return
        finally:
            writer.close()

        messagebox.showinfo("Merge complete", f"Merged PDF saved to:\n{output_path}")


if __name__ == "__main__":
    root = tk.Tk()
    PdfMergerApp(root)
    root.mainloop()

