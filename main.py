from game import Game
from ui import GameBoard

# board.drop_multiple_chips(5)

game_time = 0

game = Game(6, 8)
game.play_col(0)
game.play_col(0)
game.play_col(0)
game.play_col(1)
print(game)



