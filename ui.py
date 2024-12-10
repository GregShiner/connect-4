import tkinter as tk
import time as time

from game import Game, Player
from ai_agent import MinimaxAI


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
        self.user_input = None
        self.playRound = None
        self.button_pressed = tk.StringVar()
        self.exit_button = None
        self.info_label = None
        self.init_game_board()

    def init_game_board(self):
        self.window.title('Connect 4')
        self.window.geometry('800x800')

        self.screen_width = 800
        self.screen_height = 800
        self.board_width = 600  # Set your desired width
        self.board_height = 600  # Set your desired height

        game_screen = tk.Frame(self.window, width=self.screen_width, height=self.screen_height, bg='gray')
        game_screen.place(x=0, y=0)  # Place it at the top-left corner

        game_board = tk.Frame(game_screen, width=self.board_width, height=self.board_height, bg='black')
        game_board.place(x=(self.screen_width - self.board_width) // 2,
                         y=(self.screen_height - self.board_height) // 2)

        self.user_input = tk.Entry(game_screen, width=20)  # Increased width for better visibility
        self.user_input.place(x=self.board_width/2+40, y=700)  # Place it within the game screen frame

        self.playRound = tk.Button(game_screen, text="Play Round", command=lambda: self.button_pressed.set("button pressed"))
        self.playRound.place(x=self.board_width/2+200, y=700)

        self.exit_button = tk.Button(game_screen, text="Exit", command=self.exit_program)
        self.exit_button.place(x=self.board_width/2-50, y=700)

        self.info_label = tk.Label(self.window, width=40)
        self.info_label.place(x=self.board_width/2-50, y=50)


        game_screen.pack_propagate(False)  # Prevents the frame from resizing to fit its children
        game_board.pack_propagate(False)  # Prevents the frame from resizing to fit its children

        circle_canvas_width = self.board_width / self.columns
        circle_canvas_height = self.board_height / self.columns

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

        self.launch_ai_agent()


    def get_user_input(self):
        user_input = self.user_input.get()
        self.user_input.delete(0, "end")
        return user_input

    def exit_program(self):

        self.window.destroy()

    def player_one_play_col(self, column, row=0):
        if self.game_board_pieces[row][column].itemcget(self.game_board_circle_ids[row][column], "fill") == "black":
            # Move the drop and update the display
            self.game_board_pieces[row][column].itemcget(self.game_board_circle_ids[row][column], "fill")
            self.player_one_drop_chip(row, column)

            # Schedule the next row drop
            if row + 1 < self.rows:
                self.window.after(50, self.player_one_play_col, column, row + 1)
            else:
                return
        else:
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
        self.game_board_pieces[row][column].itemconfig(self.game_board_circle_ids[row][column], fill='blue')

    def player_two_drop_chip(self, row, column):
        if row > 0:
            self.empty_chip(row - 1, column)
        self.game_board_pieces[row][column].itemconfig(self.game_board_circle_ids[row][column], fill='red')

    def clear_board(self):
        for row in range(self.rows):
            for col in range(self.columns):
                self.game_board_pieces[row][col].itemconfig(self.game_board_circle_ids[row][col], fill='black')

    def launch_ai_agent(self):

        self.game = Game(self.rows, self.columns)

        time_delay = 10
        total_time = 10

        # Example gameplay loop
        while True:
            print(self.game)
            if self.game.player == Player.ONE:  # Human player here
                self.info_label.config(text="Pick a column")
                self.playRound.wait_variable(self.button_pressed)
                user_col = int(self.get_user_input())

                human_won = self.game.play_col(user_col - 1)
                self.window.after(total_time, self.player_one_play_col, user_col-1, 0)
                total_time += time_delay
                if human_won:
                    print(f"Player {self.game.player.value} wins!")
                    self.info_label.config(text="User Wins!")
                    time.sleep(1)
                    self.game = Game()
                    self.clear_board()
            else:  # AI player
                print("AI is thinking...")
                self.info_label.config(text="AI is thinking...")
                col = MinimaxAI(self.game, depth=4).decide_move()
                ai_won = self.game.play_col(col)
                self.window.after(total_time, self.player_two_play_col, col, 0)
                total_time += time_delay
                print(f"AI plays column: {col + 1}")
                self.info_label.config(text=f"AI plays column: {col + 1}")
                if ai_won:
                    print(f"Player {self.game.player.value} wins!")
                    self.info_label.config(text="AI Wins!")
                    time.sleep(1)
                    self.game = Game()
                    self.clear_board()
