import unittest
from board import Board
from ai_player import AIPlayer


class TestAIPlayer(unittest.TestCase):
    def setUp(self):
        self.board = Board(size=15)
        config = {'depth': 5, 'reach': 2, 'branching': 3, 'deepen': False, 'tables': 'src/tests/test.csv', 'random': False}
        config2 = {'depth': 5, 'reach': 2, 'branching': 3, 'deepen': False, 'tables': None, 'random': False}
        self.ai = AIPlayer(config, self.board)
        self.ai2 = AIPlayer(config2, self.board)

    def test_ai_is_created_with_tables(self):
        table_entries = self.ai.tables.items()
        self.assertEqual(len(table_entries), 10)

    def test_ai_is_created_without_tables(self):
        tables = self.ai2.tables
        self.assertEqual(tables, None)

    def test_ai_gives_a_move(self):
        self.board.add_piece(0, 0, 'X')
        y, x = self.ai.get_move(self.board, True, None)
        self.assertGreaterEqual(y, 0)
        self.assertLess(y, self.board.get_size())
        self.assertGreaterEqual(x, 0)
        self.assertLess(x, self.board.get_size())

    def test_ai_gives_a_move_without_tables(self):
        self.board.add_piece(0, 0, 'X')
        y, x = self.ai2.get_move(self.board, True, None)
        self.assertGreaterEqual(y, 0)
        self.assertLess(y, self.board.get_size())
        self.assertGreaterEqual(x, 0)
        self.assertLess(x, self.board.get_size())

    def test_constraints_work(self):
        self.board.add_piece(2, 2, 'X')
        y, x = self.ai.get_move(self.board, True, [(6, 6), (7, 7), (8, 8)])
        self.assertGreaterEqual(y, 6)
        self.assertLessEqual(y, 8)
        self.assertGreaterEqual(x, 6)
        self.assertLessEqual(x, 8)

    def test_ai_blocks_when_treatened(self):
        self.board.add_piece(5, 5, 'X')
        self.board.add_piece(4, 5, 'O')
        self.board.add_piece(5, 6, 'X')
        self.board.add_piece(4, 6, 'O')
        self.board.add_piece(5, 7, 'X')
        self.board.add_piece(5, 4, 'O')
        self.board.add_piece(5, 8, 'X')
        y, x = self.ai.get_move(self.board, True, None)
        self.assertEqual(y, 5)
        self.assertEqual(x, 9)

    def test_ai_finishes_row_despite_threat(self):
        self.board.add_piece(5, 5, 'O')
        self.board.add_piece(4, 5, 'X')
        self.board.add_piece(5, 6, 'O')
        self.board.add_piece(4, 6, 'X')
        self.board.add_piece(5, 7, 'O')
        self.board.add_piece(4, 7, 'X')
        self.board.add_piece(5, 8, 'O')
        self.board.add_piece(4, 8, 'X')
        y, x = self.ai.get_move(self.board, True, None)
        self.assertEqual(y, 5)
        self.assertIn(x, [4, 9])
