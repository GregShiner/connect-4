import tkinter as tk


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
        self.init_game_board()

    def init_game_board(self):

        self.window.title('Connect 4')
        self.window.geometry('1000x1000')

        game_screen = tk.Frame(self.window, width=self.screen_width, height=self.screen_height, bg='white')
        game_screen.place(x=100, y=100)
        game_board_width = self.board_width
        game_board_height = self.board_height
        game_board = tk.Frame(game_screen, width=self.board_width, height=self.board_height, bg='black')
        game_board.place(x=25, y=25)

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

        self.window.after(2000, self.player_one_drop_chip, 0, 5, 9)
        self.window.mainloop()

    def player_one_chip(self, row, column):
        if row > 0:
            self.empty_chip(row-1, column)
        self.game_board_pieces[row][column].itemconfig(self.game_board_circle_ids[row][column], fill='red')

    def empty_chip(self, row, column):
        self.game_board_pieces[row][column].itemconfig(self.game_board_circle_ids[row][column], fill='black')

    def player_one_drop_chip(self, current_row, current_column, desired_row):
        if current_row <= desired_row:
            self.window.after(50, self.player_one_drop_chip, current_row+1, current_column, desired_row)
            self.player_one_chip(current_row, current_column)
        else:
            pass
        # if current_row == desired_row:
        #     return
        # elif current_row > desired_row:
        #
        # else:
        #     return -1

    def player_two_chip(self, row, column):
        self.game_board_pieces[row][column].itemconfig(self.game_board_circle_ids[row][column], fill='blue')
