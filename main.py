from game import Game, Player
from ai_agent import MinimaxAI

game = Game()
ai = MinimaxAI(depth=4)

# Example gameplay loop
while True:
    print(game)
    if game.player == Player.ONE:  # Human player here
        col = int(input("Enter column: "))
        game.play_col(col)
    else:  # AI player
        print("AI is thinking...")
        col = ai.decide_move(game)
        print(f"AI plays column: {col}")
        game.play_col(col)

    # Add logic to check for game over conditions
