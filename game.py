from enum import Enum
import numpy as np
from ui import GameBoard


DEFAULT = "\x1b[0;39;49m"
RED = "\x1b[0;31;49m"
BLUE = "\x1b[0;34;49m"
END = "\x1b[0m"


class Space(Enum):
    # Empty space
    EMPTY = 0
    # Player 1 space
    ONE = 1
    # Player 2 space
    TWO = 2

    def __str__(self):
        match self.value:
            case Space.EMPTY.value:
                return f"{DEFAULT}0{END}"
            case Space.ONE.value:
                return f"{BLUE}1{END}"
            case Space.TWO.value:
                return f"{RED}2{END}"


class Player(Enum):
    ONE = 1
    TWO = 2

    def __str__(self):
        match self.value:
            case Space.ONE.value:
                return f"{BLUE}1{END}"
            case Space.TWO.value:
                return f"{RED}2{END}"

    def to_piece(self):
        match self.value:
            case Player.ONE.value:
                return Space.ONE

            case Player.TWO.value:
                return Space.TWO

    def __invert__(self):
        match self.value:
            case Player.ONE.value:
                return Player.TWO

            case Player.TWO.value:
                return Player.ONE


class Game:
    def __init__(self, rows=6, cols=8, combo_len=4, starting_player=Player.ONE):
        self.board = np.full(shape=(rows, cols), fill_value=Space.EMPTY, dtype=Space)
        self.rows = rows
        self.player = starting_player
        self.game_time = 0

    def play_col(self, col: int) -> None:
        row = np.argmin(self.board[:, col] == Space.EMPTY) - 1
        if row == 0 and self.board[0, col] != Space.EMPTY:
            raise ValueError("Column is full")
        self.board[row, col] = self.player.to_piece()

        self.player = ~self.player

    def __str__(self):
        string = ""
        for row in self.board:
            for col in row:
                string += str(col) + " "
            string += "\n"
        string += f"Current Player: {self.player}"

        return string
