from game import Game
from ui import GameBoard

board = GameBoard(800, 800, 700, 700, 10, 10)
# board.player_one_drop_chip(10, 5, 2)
game = Game()
game.play_col(0)
game.play_col(0)
game.play_col(1)
print(game)
