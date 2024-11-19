from game import Game
import ui

ui.init_game_board(screen_width=800, screen_height=800, board_width=700, board_height=700, rows=10, columns=10)
game = Game()
game.play_col(0)
game.play_col(0)
game.play_col(1)
print(game)
