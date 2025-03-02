import random
import string
import tkinter as tk
from tkinter import messagebox, scrolledtext
import pyperclip

def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected!"

    return ''.join(random.choice(characters) for _ in range(length))

def generate_and_display():
    try:
        num_passwords = int(num_passwords_entry.get())
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        passwords = [generate_password(length, use_letters, use_numbers, use_symbols) for _ in range(num_passwords)]
        password_display.delete("1.0", tk.END)
        password_display.insert(tk.END, "\n".join(passwords))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length and count!")

def copy_to_clipboard():
    passwords = password_display.get("1.0", tk.END).strip()
    if passwords:
        pyperclip.copy(passwords)
        messagebox.showinfo("Copied", "Passwords copied to clipboard!")

def save_to_file():
    passwords = password_display.get("1.0", tk.END).strip()
    if passwords:
        with open("passwords.txt", "a") as file:
            file.write(passwords + "\n")
        messagebox.showinfo("Saved", "Passwords saved to passwords.txt!")

# GUI Setup
root = tk.Tk()
root.title("PassForge  - Password Generator")
root.geometry("400x450")
root.resizable(False, False)

tk.Label(root, text="PassForge ", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Number of Passwords:").pack()
num_passwords_entry = tk.Entry(root)
num_passwords_entry.pack()
num_passwords_entry.insert(0, "1")

tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "12")

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

generate_btn = tk.Button(root, text="Generate Passwords", command=generate_and_display, bg="blue", fg="white")
generate_btn.pack(pady=5)

password_display = scrolledtext.ScrolledText(root, width=40, height=5, wrap=tk.WORD)
password_display.pack(pady=5)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="green", fg="white")
copy_btn.pack(pady=5)

save_btn = tk.Button(root, text="Save to File", command=save_to_file, bg="orange", fg="white")
save_btn.pack(pady=5)

root.mainloop()
