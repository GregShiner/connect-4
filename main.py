from game import Game
from ui import GameBoard

# board.drop_multiple_chips(5)

game_time = 0

# board.window.after(game_time+2000, board.player_one_drop_chip, 0, 5, 10)
# game_time += 2000
# board.window.after(game_time+2000, board.player_one_drop_chip, 0, 4, 10)
# game_time += 2000
# board.window.after(2000, board.drop_multiple_chips, 5)
# board.drop_multiple_chips(5)
game = Game(6, 8)
game.play_col(0)
game.play_col(0)
# game.play_col(0)
# game.play_col(1)
game.ui_board.window.mainloop()
print(game)



