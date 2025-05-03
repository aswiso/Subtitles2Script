import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.scrolledtext import ScrolledText
import re

# constants
NIGHT_D = "#181818"
NIGHT_D2 = "#1f1f1f"
NIGHT_L = "#ccccae"

def open_file():
    global gl_filepath
    gl_filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not gl_filepath:
        return
    txt_box.delete("1.0", tk.END)
    with open(file=gl_filepath, mode="r", encoding="utf-8-sig") as open_file:
        input_text = open_file.read()
        txt_box.insert(tk.END, input_text)
    root.title(f"Subtitle Editor - {gl_filepath}")

def save_file():
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(file=filepath, mode="w", encoding="utf-8") as save_file:
        save_text = txt_box.get("1.0", tk.END)
        save_file.write(save_text)
    root.title(f"Subtitle Editor - {filepath}")

def transform():
    wind_text = txt_box.get("1.0", tk.END)

    regex_transf = [
        ("(\\d+),", ""),
        ("[^a-zäöüßA-ZÄÖÜ.,>?!()']", " "),
        ("\\s+", " "),
        (">", "\n")
    ]
    for i, j in regex_transf:
        wind_text = re.sub(i, j, wind_text)
    txt_box.delete("1.0", tk.END)
    txt_box.insert(tk.END, wind_text)

def revert():
    try:
        txt_box.delete("1.0", tk.END)
        with open(file=gl_filepath, mode="r", encoding="utf-8-sig") as open_file:
            input_text = open_file.read()
            txt_box.insert(tk.END, input_text)
    except Exception as e:
        messagebox.showerror("Error", "Original file not found")

def clear():
    txt_box.delete("1.0", tk.END)

root = tk.Tk()
root.title("Subtitle Editor")
root.rowconfigure(0, minsize=50, weight=1)
root.columnconfigure(0, minsize=50, weight=1)

window = tk.Frame(master=root, background=NIGHT_D)
window.grid(row=0, column=0, sticky="nsew")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_box = ScrolledText(master=window, background=NIGHT_D2, foreground=NIGHT_L)
txt_box.grid(row=0, column=1, sticky="nsew", pady=(5, 5), padx=(0, 5))


frm_buttons = tk.Frame(master=window, background=NIGHT_D)
frm_buttons.grid(row=0, column=0, sticky="ns", pady=(5, 5))

btn_open = tk.Button(master=frm_buttons, text="Open", command=open_file, bg=NIGHT_D, fg=NIGHT_L)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save = tk.Button(master=frm_buttons, text="Save as...", command=save_file, bg=NIGHT_D, fg=NIGHT_L)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=(0, 5))
btn_transform = tk.Button(master=frm_buttons, text="Transform", command=transform, bg=NIGHT_D, fg=NIGHT_L)
btn_transform.grid(row=2, column=0, sticky="ew", padx=5, pady=(0, 5))
btn_revert = tk.Button(master=frm_buttons, text="Revert", command=revert, bg=NIGHT_D, fg=NIGHT_L)
btn_revert.grid(row=3, column=0, sticky="ew", padx=5, pady=(0, 5))
btn_clear = tk.Button(master=frm_buttons, text="Clear", command=clear, bg=NIGHT_D, fg=NIGHT_L)
btn_clear.grid(row=4, column=0, padx=5, sticky="ew", pady=(0, 5))
btn_close = tk.Button(master=window, text="Exit", command=root.destroy, bg=NIGHT_D, fg=NIGHT_L)
btn_close.grid(row=0, column=0, sticky="ews", padx=5, pady=5)

tk.mainloop()