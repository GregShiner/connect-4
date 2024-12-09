from game import Game

game = Game()

while True:
    print(game)
    col = int(input("Enter col: "))
    is_win = game.play_col(col - 1)
    if is_win:
        print(f"Player {game.player.value} wins!")
        game = Game()
