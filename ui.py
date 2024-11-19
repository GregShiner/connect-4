import tkinter as tk

root = tk.Tk()

# Create some labels
labels = []
for i in range(5):
    for j in range(3):
        label = tk.Label(root, text=f"Label {i},{j}", borderwidth=1, relief="solid")
        label.grid(row=i, column=j, sticky="nsew")
        labels.append(label)

# Configure the grid to expand
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(3):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()