import numpy as np
import copy
from game import Space


class MinimaxAI:
    def __init__(self, game, depth=4):
        """
        Initialize the AI with a game instance.

        Args:
        game (Game): The game instance to play on
        depth (int, optional): Search depth for minimax. Defaults to 4.
        """
        self.game = game
        self.depth = depth

    def evaluate_board(self, board, player):
        """
        Heuristic evaluation of the board.
        Returns a score based on the advantage of the given player.
        """
        # Placeholder for a board evaluation function
        return np.random.randint(-10, 10)

    def get_valid_moves(self):
        """
        Returns a list of columns that are valid moves (not full).
        """
        return [col for col in range(self.game.board.shape[1]) 
                if self.game.board[0, col] == Space.EMPTY]

    def minimax(self, board, depth, is_maximizing, alpha, beta, player):
        """
        Minimax algorithm with alpha-beta pruning.
        """
        valid_moves = self.get_valid_moves()

        # Terminal condition: maximum depth or no valid moves
        if depth == 0 or not valid_moves:
            return self.evaluate_board(board, player), None

        if is_maximizing:
            max_eval = float('-inf')
            best_move = None
            for move in valid_moves:
                # Create a deep copy of the game to simulate move
                temp_game = copy.deepcopy(self.game)

                # Use play_col which handles all move logic
                is_win = temp_game.play_col(move)

                # Check for winning move
                if is_win:
                    return float('inf'), move

                eval, _ = self.minimax(temp_game.board, depth - 1, False, alpha, beta, ~player)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in valid_moves:
                # Create a deep copy of the game to simulate move
                temp_game = copy.deepcopy(self.game)

                # Use play_col which handles all move logic
                is_win = temp_game.play_col(move)

                # Check for winning move
                if is_win:
                    return float('-inf'), move

                eval, _ = self.minimax(temp_game.board, depth - 1, True, alpha, beta, player)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def decide_move(self):
        """
        Determines the best move for the AI player.
        Uses the current game's board and player.
        """
        _, best_move = self.minimax(self.game.board, self.depth, True, 
                                    float('-inf'), float('inf'), self.game.player)
        return best_move
