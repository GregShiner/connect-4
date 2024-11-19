import tkinter as tk
import time as time

game_board_pieces = [[]]
game_board_circle_ids = [[]]


def player_one_chip(game_board_square, game_piece_id):
    game_board_square.itemconfig(game_piece_id, fill='red')


def player_two_chip(game_piece_id):
    game_board_piece.itemconfig(game_piece_id, fill='blue')


root = tk.Tk()

root.title('Connect 4')
root.geometry('1000x1000')


def init_game_board():

    game_screen = tk.Frame(root, width=800, height=800, bg='white')
    game_screen.place(x=100, y=100)
    game_board_width = 700
    game_board_height = 700
    game_board = tk.Frame(game_screen, width=game_board_width, height=game_board_height, bg='black')
    game_board.place(x=25, y=25)

    game_board_rows = 10
    game_board_columns = 10

    circle_canvas_width = game_board_width/game_board_columns
    circle_canvas_height = game_board_height/game_board_columns

    circle_width = int(circle_canvas_width/1.3)
    circle_height = int(circle_canvas_height/1.3)

    x0 = (circle_canvas_width - circle_width) / 2
    y0 = (circle_canvas_height - circle_height) / 2
    x1 = x0 + circle_width
    y1 = y0 + circle_height

    for i in range(game_board_rows):
        game_board_circle_ids.append([])
        game_board_pieces.append([])
        for j in range(game_board_columns):
            game_board_piece = tk.Canvas(game_board, width=circle_canvas_width,
                                         height=circle_canvas_height, highlightthickness=0, bg='yellow')
            game_board_circle_ids[i].append(game_board_piece.create_oval(x0, y0, x1, y1, fill="black", outline='black'))
            game_board_piece.grid(row=i, column=j, padx=0, pady=0, sticky="nsew")
            game_board_pieces[i].append(game_board_piece)


init_game_board()

player_one_chip(game_board_pieces[1][5], game_board_circle_ids[1][5])

root.mainloop()
