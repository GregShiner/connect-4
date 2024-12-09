import numpy as np
import copy
from game import Game, Space


class MinimaxAI:
    def __init__(self, game: Game | None=None, depth=4):
        """
        Initialize the AI with a game instance.

        Args:
        game (Game): The game instance to play on
        depth (int, optional): Search depth for minimax. Defaults to 4.
        """
        self.game = game if game else Game()
        self.depth = depth

    def evaluate_board(self, board, player):
        """
        Heuristic evaluation of the board for the given player.

        Args:
        board (numpy.ndarray): The current game board
        player (Player): The player to evaluate for

        Returns:
        int: Evaluation score of the board
        """
        # Define constants for scoring
        WINDOW_LENGTH = 4
        SCORE_4_IN_A_ROW = 100
        SCORE_3_IN_A_ROW = 5
        SCORE_2_IN_A_ROW = 2
        OPPONENT_MULTIPLIER = -1

        # Convert player to piece
        piece = player.to_piece()
        opponent_piece = (~player).to_piece()

        def count_window_pieces(window, piece):
            """Count the number of pieces in a window."""
            return np.count_nonzero(window == piece)

        def evaluate_window(window, piece):
            """
            Evaluate a single 4-piece window on the board.

            Args:
            window (numpy.ndarray): A numpy array of 4 board positions
            piece (Space): The player's piece to evaluate for

            Returns:
            int: Score for this window
            """
            score = 0

            # 4 in a row is a winning condition
            if count_window_pieces(window, piece) == 4:
                score += SCORE_4_IN_A_ROW
            # 3 in a row with an empty space is promising
            elif (count_window_pieces(window, piece) == 3 and 
                  count_window_pieces(window, Space.EMPTY) == 1):
                score += SCORE_3_IN_A_ROW
            # 2 in a row with two empty spaces is also good
            elif (count_window_pieces(window, piece) == 2 and 
                  count_window_pieces(window, Space.EMPTY) == 2):
                score += SCORE_2_IN_A_ROW

            # Penalize opponent's potential winning moves
            if (count_window_pieces(window, opponent_piece) == 3 and 
                count_window_pieces(window, Space.EMPTY) == 1):
                score -= SCORE_3_IN_A_ROW

            return score

        def score_position(board, piece):
            """
            Score the entire board for a given piece.

            Args:
            board (numpy.ndarray): The game board
            piece (Space): The player's piece to evaluate

            Returns:
            int: Total score for the board
            """
            score = 0

            # Score center column (strategically important)
            if board.shape[1] % 2 == 0:
                center_array = board[:, board.shape[1]//2]
                center_count = np.count_nonzero(center_array == piece)
                center_array = board[:, (board.shape[1]//2) - 1]
                center_count = np.count_nonzero(center_array == piece)
                score += center_count * 2
            else:
                center_array = board[:, (board.shape[1]//2)]
                center_count = np.count_nonzero(center_array == piece)
                score += center_count * 3

            # Horizontal windows
            for r in range(board.shape[0]):
                for c in range(board.shape[1] - 3):
                    window = board[r, c:c+WINDOW_LENGTH]
                    score += evaluate_window(window, piece)

            # Vertical windows
            for c in range(board.shape[1]):
                for r in range(board.shape[0] - 3):
                    window = board[r:r+WINDOW_LENGTH, c]
                    score += evaluate_window(window, piece)

            # Positive sloped diagonal windows
            for r in range(board.shape[0] - 3):
                for c in range(board.shape[1] - 3):
                    window = np.array([board[r+i, c+i] for i in range(WINDOW_LENGTH)])
                    score += evaluate_window(window, piece)

            # Negative sloped diagonal windows
            for r in range(board.shape[0] - 3):
                for c in range(board.shape[1] - 3):
                    window = np.array([board[r+3-i, c+i] for i in range(WINDOW_LENGTH)])
                    score += evaluate_window(window, piece)

            return score

        # Final score calculation
        player_score = score_position(board, piece)
        opponent_score = score_position(board, opponent_piece)

        return player_score + (opponent_score * OPPONENT_MULTIPLIER)

    def get_valid_moves(self, board):
        """
        Returns a list of columns that are valid moves (not full).
        """
        return [col for col in range(self.game.cols) 
                if board[0, col] == Space.EMPTY]

    def minimax(self, game: Game, depth, is_maximizing, alpha, beta, player):
        """
        Minimax algorithm with alpha-beta pruning.
        """
        valid_moves = self.get_valid_moves(game.board)

        # Terminal condition: maximum depth or no valid moves
        if depth == 0 or not valid_moves:
            return self.evaluate_board(game.board, player), None

        if is_maximizing:
            max_eval = float('-inf')
            best_move = None
            for move in valid_moves:
                # Create a deep copy of the game to simulate move
                temp_game = copy.deepcopy(game)

                # Use play_col which handles all move logic
                is_win = temp_game.play_col(move)

                # Check for winning move
                if is_win:
                    return float('inf'), move

                eval, _ = self.minimax(temp_game, depth - 1, False, alpha, beta, ~player)
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
                temp_game = copy.deepcopy(game)

                # Use play_col which handles all move logic
                is_win = temp_game.play_col(move)

                # Check for winning move
                if is_win:
                    return float('-inf'), move

                eval, _ = self.minimax(temp_game, depth - 1, True, alpha, beta, player)
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
        _, best_move = self.minimax(self.game, self.depth, True, 
                                    float('-inf'), float('inf'), self.game.player)
        return best_move
