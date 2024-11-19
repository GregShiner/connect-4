import tkinter as tk
import time as time

# # Create some labels
# labels = []
# for i in range(5):
#     for j in range(3):
#         label = tk.Label(root, text=f"Label {i},{j}", borderwidth=1, relief="solid")
#         label.grid(row=i, column=j, sticky="nsew")
#         labels.append(label)
#
# # Configure the grid to expand
# for i in range(5):
#     root.grid_rowconfigure(i, weight=1)
# for j in range(3):
#     root.grid_columnconfigure(j, weight=1)


def player_one_chip():
    game_circle.itemconfig(game_circle_id, fill='red')
    root.after(3000, player_two_chip)


def player_two_chip():
    game_circle.itemconfig(game_circle_id, fill='blue')


root = tk.Tk()

root.title('Connect 4')
root.geometry('1000x1000')

circle_canvas_width = 100
circle_canvas_height = 100
game_circle = tk.Canvas(root, width=circle_canvas_width, height=circle_canvas_height, bg='yellow')
game_circle.pack()

circle_width = 75
circle_height = 75

x0 = (circle_canvas_width - circle_width) / 2
y0 = (circle_canvas_height - circle_height) / 2
x1 = x0 + circle_width
y1 = y0 + circle_height

game_circle_id = game_circle.create_oval(x0, y0, x1, y1, fill="black", outline='black')
game_circle.place(x=150, y=150)
root.after(3000, player_one_chip)

root.mainloop()
