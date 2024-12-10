import tkinter as tk
import time as time
from game import Game


class GameBoard:

    def __init__(self, screen_width, screen_height, board_width, board_height, rows, columns):
        self.window = tk.Tk()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.board_width = board_width
        self.board_height = board_height
        self.rows = rows
        self.columns = columns
        self.game_board_pieces = [[]]
        self.game_board_circle_ids = [[]]
        self.game = Game()
        self.init_game_board()

    def init_game_board(self):

        self.window.title('Connect 4')
        self.window.geometry('800x800')

        game_screen = tk.Frame(self.window, width=self.screen_width, height=self.screen_height, bg='white')
        game_screen.place(x=100, y=100)
        game_board_width = self.board_width
        game_board_height = self.board_height
        game_board = tk.Frame(game_screen, width=self.board_width, height=self.board_height, bg='black')
        game_board.place(x=(self.screen_width - self.board_width) / 2, y=(self.screen_height - self.board_height) / 2)

        circle_canvas_width = game_board_width / self.columns
        circle_canvas_height = game_board_height / self.columns

        circle_width = int(circle_canvas_width / 1.3)
        circle_height = int(circle_canvas_height / 1.3)

        x0 = (circle_canvas_width - circle_width) / 2
        y0 = (circle_canvas_height - circle_height) / 2
        x1 = x0 + circle_width
        y1 = y0 + circle_height

        for i in range(self.rows):
            self.game_board_circle_ids.append([])
            self.game_board_pieces.append([])
            for j in range(self.columns):
                game_board_piece = tk.Canvas(game_board, width=circle_canvas_width,
                                             height=circle_canvas_height, highlightthickness=0, bg='yellow')
                self.game_board_circle_ids[i].append(
                    game_board_piece.create_oval(x0, y0, x1, y1, fill="black", outline='black'))
                game_board_piece.grid(row=i, column=j, padx=0, pady=0, sticky="nsew")
                self.game_board_pieces[i].append(game_board_piece)

        time_delay = 1000
        total_time = 0

        total_time += time_delay

        self.window.after(total_time, self.player_one_play_col, 0, 0)
        total_time += time_delay
        self.window.after(total_time, self.player_two_play_col, 0, 0)
        total_time += time_delay
        self.window.after(total_time, self.player_one_play_col, 1, 0)
        total_time += time_delay
        self.window.after(total_time, self.player_two_play_col, 1, 0)
        total_time += time_delay
        self.window.after(total_time, self.player_one_play_col, 0, 0)
        total_time += time_delay
        self.window.after(total_time, self.player_two_play_col, 0, 0)
        total_time += time_delay
        self.window.after(total_time, self.player_one_play_col, 0, 0)
        total_time += time_delay
        self.window.after(total_time, self.player_two_play_col, 0, 0)
        total_time += time_delay
        self.window.mainloop()

    def player_one_play_col(self, column, row=0):
        if self.game_board_pieces[row][column].itemcget(self.game_board_circle_ids[row][column], "fill") == "black":
            # Move the drop and update the display
            self.game_board_pieces[row][column].itemcget(self.game_board_circle_ids[row][column], "fill")
            self.player_one_drop_chip(row, column)

            # Schedule the next row drop
            if row + 1 < self.rows:
                self.window.after(50, self.player_one_play_col, column, row + 1)
            else:
                print('at bottom of board')
                return
        else:
            print('current board piece is not black')
            return

    def player_two_play_col(self, column, row=0):
        if self.game_board_pieces[row][column].itemcget(self.game_board_circle_ids[row][column], "fill") == "black":
            # Move the drop and update the display
            self.game_board_pieces[row][column].itemcget(self.game_board_circle_ids[row][column], "fill")
            self.player_two_drop_chip(row, column)

            # Schedule the next row drop
            if row + 1 < self.rows:
                self.window.after(50, self.player_two_play_col, column, row + 1)
            else:
                print('at bottom of board')
                return
        else:
            print('current board piece is not black')
            return


    def empty_chip(self, row, column):
        self.game_board_pieces[row][column].itemconfig(self.game_board_circle_ids[row][column], fill='black')

    def player_one_drop_chip(self, row, column):
        if row > 0:
            self.empty_chip(row - 1, column)
        self.game_board_pieces[row][column].itemconfig(self.game_board_circle_ids[row][column], fill='red')
        self.window.update()

    def player_two_drop_chip(self, row, column):
        if row > 0:
            self.empty_chip(row - 1, column)
        self.game_board_pieces[row][column].itemconfig(self.game_board_circle_ids[row][column], fill='blue')
        self.window.update()
