import tkinter as tk
from tkinter import ttk
import random
import string

# === Setup Window ===
root = tk.Tk()
root.title("Universal Key Generator")
root.geometry("420x520")
root.resizable(False, False)

# === Dark Mode Styling ===
dark_bg = "#1e1e1e"
dark_fg = "#ffffff"
accent_color = "#3a3a3a"

root.configure(bg=dark_bg)

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background=dark_bg, foreground=dark_fg)
style.configure("TCheckbutton", background=dark_bg, foreground=dark_fg)
style.configure("TButton", background=accent_color, foreground=dark_fg)
style.map("TButton", background=[("active", "#505050")])

# === Variables for checkboxes ===
use_upper = tk.BooleanVar()
use_lower = tk.BooleanVar()
use_num = tk.BooleanVar()
use_special = tk.BooleanVar()

# === Checkbuttons ===
ttk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=use_upper).pack(anchor='w', padx=10, pady=3)
ttk.Checkbutton(root, text="Include Lowercase (a-z)", variable=use_lower).pack(anchor='w', padx=10, pady=3)
ttk.Checkbutton(root, text="Include Numbers (0-9)", variable=use_num).pack(anchor='w', padx=10, pady=3)
ttk.Checkbutton(root, text="Include Special Characters (!@#$...)", variable=use_special).pack(anchor='w', padx=10, pady=3)

# === Pattern Input ===
ttk.Label(root, text="Key Pattern (use 'x' as placeholder):").pack(pady=(10, 0), anchor='w', padx=10)
pattern_entry = ttk.Entry(root)
pattern_entry.pack(fill='x', padx=10, pady=5)

# === Count Input ===
ttk.Label(root, text="How many keys to generate?").pack(pady=(10, 0), anchor='w', padx=10)
count_entry = ttk.Entry(root)
count_entry.pack(fill='x', padx=10, pady=5)

# === Output Text Box ===
output = tk.Text(root, height=10, bg="#2b2b2b", fg=dark_fg, insertbackground="white")
output.pack(fill='both', padx=10, pady=(20, 10))

# === Generate Function ===
def on_generate():
    pattern = pattern_entry.get().strip()
    try:
        num_keys = int(count_entry.get().strip())
        if num_keys <= 0:
            raise ValueError
    except ValueError:
        output.delete(1.0, tk.END)
        output.insert(tk.END, "⚠️ Enter a valid number of keys (1 or more).\n")
        return

    # Build character pool
    char_pool = ""
    if use_upper.get():
        char_pool += string.ascii_uppercase
    if use_lower.get():
        char_pool += string.ascii_lowercase
    if use_num.get():
        char_pool += string.digits
    if use_special.get():
        char_pool += "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"

    if not char_pool:
        output.delete(1.0, tk.END)
        output.insert(tk.END, "⚠️ Please select at least one character type.\n")
        return

    # Generate keys
    keys = []
    for _ in range(num_keys):
        key = ""
        for ch in pattern:
            if ch == 'x':
                key += random.choice(char_pool)
            else:
                key += ch
        keys.append(key)

    # Display results
    output.delete(1.0, tk.END)
    output.insert(tk.END, "\n".join(keys))

# === Generate Button ===
ttk.Button(root, text="Generate Keys", command=on_generate).pack(pady=10)

# === Run App ===
root.mainloop()
