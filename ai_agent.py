import numpy as np
from game import Space


class MinimaxAI:
    def __init__(self, depth=4):
        self.depth = depth

    def evaluate_board(self, board, player):
        """
        Heuristic evaluation of the board.
        Returns a score based on the advantage of the given player.
        """
        # Placeholder for a board evaluation function
        return np.random.randint(-10, 10)

    def get_valid_moves(self, board):
        """
        Returns a list of columns that are valid moves (not full).
        """
        return [col for col in range(board.shape[1]) if board[0, col] == Space.EMPTY]

    def minimax(self, board, depth, is_maximizing, alpha, beta, player):
        """
        Minimax algorithm with alpha-beta pruning.
        """
        valid_moves = self.get_valid_moves(board)

        # Terminal condition: maximum depth or no valid moves
        if depth == 0 or not valid_moves:
            return self.evaluate_board(board, player), None

        if is_maximizing:
            max_eval = float('-inf')
            best_move = None
            for move in valid_moves:
                temp_board = board.copy()
                self.simulate_move(temp_board, move, player)
                eval, _ = self.minimax(temp_board, depth - 1, False, alpha, beta, ~player)
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
                temp_board = board.copy()
                self.simulate_move(temp_board, move, ~player)
                eval, _ = self.minimax(temp_board, depth - 1, True, alpha, beta, player)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def simulate_move(self, board, col, player):
        """
        Simulates dropping a piece in the specified column for the player.
        """
        row = np.argmin(board[:, col] == Space.EMPTY) - 1
        if row == 0 and board[0, col] != Space.EMPTY:
            raise ValueError("Column is full")
        board[row, col] = player.to_piece()

    def decide_move(self, game):
        """
        Determines the best move for the AI player.
        """
        _, best_move = self.minimax(game.board, self.depth, True, float('-inf'), float('inf'), game.player)
        return best_move
