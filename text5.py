import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.text_area = tk.Text(root)
        self.text_area.pack(expand=True, fill="both")
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Word Count", command=self.word_count)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Zoom In", command=self.zoom_in)
        view_menu.add_command(label="Zoom Out", command=self.zoom_out)
        menubar.add_cascade(label="View", menu=view_menu)

        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Find", command=self.find_text)
        menubar.add_cascade(label="Tools", menu=tools_menu)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())

    def save_file(self):
        pass  # Implement save functionality here

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def word_count(self):
        content = self.text_area.get(1.0, tk.END)
        words = content.split()
        num_words = len(words)
        messagebox.showinfo("Word Count", f"Total Words: {num_words}")

    def zoom_in(self):
        # Implement zoom in functionality here
        pass

    def zoom_out(self):
        # Implement zoom out functionality here
        pass

    def find_text(self):
        # Implement find functionality here
        pass

    def show_about(self):
        messagebox.showinfo("About", "Simple Text Editor\nCreated with Python and Tkinter")

def main():
    root = tk.Tk()
    text_editor = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
