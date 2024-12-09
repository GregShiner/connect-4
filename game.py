from enum import Enum
import numpy as np
from typing import Tuple


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
    def __init__(self, rows=6, cols=8, combo_len=4, starting_player = Player.ONE):
        self.rows = rows
        self.cols = cols
        self.combo_len = combo_len
        self.board = np.full(shape=(self.rows, self.cols), fill_value=Space.EMPTY, dtype=Space)
        self.player = starting_player

    def play_col(self, col: int) -> bool:
        # Row gets set to -1 in 2 conditions
        # 1. Its the first row
        # 2. There is no available slot
        row = np.argmin(self.board[:, col] == Space.EMPTY) - 1
        if row == -1 and self.board[0, col] != Space.EMPTY:
            raise ValueError("Column is full")
        # The row being set to -1 to represent the last cell breaks the win checking logic, so set it back to a positive index
        if row == -1:
            row = self.rows - 1
        self.board[row, col] = self.player.to_piece()
        is_win = self.check_win((row, col))
        if is_win:
            return True
        self.player = ~self.player
        return False

    def check_win(self, coords: Tuple[int, int]) -> bool:
        number_in_row = 0
        # for row_mult, col_mult in [(0, 1), (1, 0), (1, 1), (1, -1)]:
        #     for offset in range(-(self.combo_len - 1), self.combo_len):
        #         row = (row_mult * offset) + coords[0]
        #         col = (row_mult * offset) + coords[1]
        #
        #         if row < 0 or row >= self.rows:
        #             continue
        #         if col < 0 or col >= self.cols:
        #             continue
        #
        #         if self.board[row, col] == self.player.to_piece():
        #             number_in_row += 1
        #         else:
        #             number_in_row = 0
        #
        #         if number_in_row == 4:
        #             return True
        for offset in range(-(self.combo_len - 1), self.combo_len):
            row = offset + coords[0]
            col = coords[1]

            if row < 0 or row >= self.rows:
                continue
            if col < 0 or col >= self.cols:
                continue

            if self.board[row, col] == self.player.to_piece():
                number_in_row += 1
            else:
                number_in_row = 0

            if number_in_row == 4:
                return True

    def __str__(self):
        string = ""
        for row in self.board:
            for col in row:
                string += str(col) + " "
            string += "\n"
        string += f"Current Player: {self.player}"

        return string
