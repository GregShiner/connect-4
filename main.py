from ui import GameBoard
from sys import argv

def display_help():
    print("Usage: python main.py <flag>")
    print("Flags:")
    print("--help, -h   Display this help message")
    print("--cli,  -c   Run this program in cli mode")
    exit(0)

if len(argv) >= 2:
    if argv[1] in ["--help", "-h"]:
        display_help()
    if argv[1] in ["--cli", "-c"]:
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
    else:
        print(f"Unknown option: {argv[1]}")
        display_help()
else:
    game_board = GameBoard(600, 600, 500, 500, 8, 8)
