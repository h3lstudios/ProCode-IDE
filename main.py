import sys
from tkinter import filedialog
from PIL import Image, ImageTk


def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".pc", filetypes=[("ProCode Files", "*.pc")]
    )
    if file_path:
        with open(file_path, "w") as file:
            text = text_area.get(1.0, tk.END)
            file.write(text)


def load_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".pc", filetypes=[("ProCode Files", "*.pc")]
    )
    if file_path:
        with open(file_path, "r") as file:
            text = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, text)


def on_text_changed(event):
    if text_area.get(1.0, tk.END) == '\n':  
        text_area.delete(1.0, tk.END)
        placeholder_text = """Copy template.pc from https://github.com/h3lstudios/ProCode"""
        text_area.insert(tk.END, placeholder_text)


root = tk.Tk()
root.title("Text Editor")


# Logo
logo_image = Image.open("logo.png") 
logo_image = logo_image.resize((200, 200))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo)
logo_label.pack()


text_area = tk.Text(root)
text_area.pack(fill=tk.BOTH, expand=True)
text_area.ind("<FocusIn>", on_text_changed)


save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack(side=tk.LEFT)

load_button = tk.Button(root, text="Load", command=load_file)
load_button.pack(side=tk.LEFT)


# Keyboard Shortcuts
if sys.platform.startswith("darwin"):  # macOS
    root.bind("<Command-s>", lambda event: save_file())  # Command + S
    root.bind("<Command-o>", lambda event: load_file())  # Command + O
else:  # Windows or Linux
    root.bind("<Control-s>", lambda event: save_file())  # Ctrl + S
    root.bind("<Control-o>", lambda event: load_file())  # Ctrl + O


root.mainloop()