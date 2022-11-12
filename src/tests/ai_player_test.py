import unittest
from board import Board
from AI_player import AIPlayer


class TestAIPlayer(unittest.TestCase):
    def setUp(self):
        self.board = Board(size=15, row_len=5)
        self.ai = AIPlayer(5, 2, 3, self.board)

    def test_ai_gives_a_move(self):
        self.board.add_piece(0, 0, 'X')
        y, x = self.ai.get_move(self.board, True)
        self.assertGreaterEqual(y, 0)
        self.assertLess(y, self.board.get_size())
        self.assertGreaterEqual(x, 0)
        self.assertLess(x, self.board.get_size())
