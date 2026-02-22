import tkinter as tk
from collections import Counter

root = tk.Tk()
root.title("FLAMES Game")
root.geometry("600x450")
root.configure(bg="#2c2f33")

# ---------- CENTER FRAME ----------
frame = tk.Frame(
    root,
    bg="#f5f5f5",
    bd=2,
    relief="ridge"
)
frame.place(relx=0.5, rely=0.5, anchor="center")

# ---------- TITLE ----------
title = tk.Label(
    frame,
    text="🔥 FLAMES GAME 🔥",
    font=("Segoe UI", 20, "bold"),
    bg="#f5f5f5",
    fg="#ff5733"
)
title.grid(row=0, column=0, columnspan=2, pady=(20, 15))

# ---------- NAME INPUT ----------
tk.Label(
    frame,
    text="Name 1",
    font=("Segoe UI", 12),
    bg="#f5f5f5"
).grid(row=1, column=0, sticky="e", padx=10, pady=8)

tk.Label(
    frame,
    text="Name 2",
    font=("Segoe UI", 12),
    bg="#f5f5f5"
).grid(row=2, column=0, sticky="e", padx=10, pady=8)

iname1 = tk.Entry(frame, font=("Segoe UI", 12), width=20)
iname2 = tk.Entry(frame, font=("Segoe UI", 12), width=20)
iname1.grid(row=1, column=1, pady=8)
iname2.grid(row=2, column=1, pady=8)

# ---------- RESULT LABEL ----------
result_label = tk.Label(
    frame,
    text="💖 Enter names and click Play 💖",
    font=("Segoe UI", 12, "bold"),
    bg="#f5f5f5",
    fg="#333"
)
result_label.grid(row=4, column=0, columnspan=2, pady=20)

# ---------- LOGIC ----------
def play():
    n1 = iname1.get().replace(" ", "").lower()
    n2 = iname2.get().replace(" ", "").lower()

    if not n1 or not n2:
        result_label.config(text="⚠️ Please enter both names!", fg="red")
        return

    c1 = Counter(n1)
    c2 = Counter(n2)

    for ch in list(c1.keys()):
        if ch in c2:
            common = min(c1[ch], c2[ch])
            c1[ch] -= common
            c2[ch] -= common

    count = sum(c1.values()) + sum(c2.values())

    flames = ["Friends 🤝", "Love ❤️", "Affection 💖",
              "Marriage 💍", "Enemies ⚔️", "Sibling 👨‍👩‍👧"]

    index = 0
    while len(flames) > 1:
        index = (index + count - 1) % len(flames)
        flames.pop(index)

    result_label.config(
        text=f"✨ Result: {flames[0]} ✨",
        fg="#ff5733"
    )

# ---------- BUTTON ----------
play_btn = tk.Button(
    frame,
    text="▶ PLAY",
    font=("Segoe UI", 12, "bold"),
    bg="#ff5733",
    fg="white",
    activebackground="#ff784e",
    width=15,
    command=play
)
play_btn.grid(row=3, column=0, columnspan=2, pady=10)

# ---------- PADDING ----------
for i in range(5):
    frame.grid_rowconfigure(i, minsize=40)

frame.grid_columnconfigure(0, minsize=120)
frame.grid_columnconfigure(1, minsize=200)

root.mainloop()
