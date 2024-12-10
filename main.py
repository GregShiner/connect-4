from game import Game, Player
from ai_agent import MinimaxAI

game = Game()

# Example gameplay loop
while True:
    print(game)
    if game.player == Player.ONE:  # Human player here
        col = int(input("Enter column: "))
        if game.play_col(col - 1):
            print(f"Player {game.player.value} wins!")
            game = Game()
    else:  # AI player
        print("AI is thinking...")
        col = MinimaxAI(game, depth=4).decide_move()
        print(f"AI plays column: {col + 1}")
        if game.play_col(col):
            print(f"Player {game.player.value} wins!")
            game = Game()

