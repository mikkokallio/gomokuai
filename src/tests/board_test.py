import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(size=15, row_len=5)

    def test_can_add_stone_to_empty_space(self):
        try:
            self.board.add_piece(3, 3, 'X')
        except ValueError:
            assert False

    def test_cannot_add_stone_to_taken_space(self):
        with self.assertRaises(ValueError):
            self.board.add_piece(3, 3, 'X')
            self.board.add_piece(3, 3, 'X')

    def test_five_in_a_row_wins(self):
        moves = [(1,1,'X'), (1,2,'X'), (1,3,'X'), (1,4,'X')]
        [self.board.add_piece(*move) for move in moves]
        win = self.board.is_winning_move(self.board.state, 1, 5, 'X')
        self.assertTrue(win)
        moves = [(2,1,'O'), (2,2,'O'), (2,3,'O'), (2,4,'O')]
        [self.board.add_piece(*move) for move in moves]
        win = self.board.is_winning_move(self.board.state, 2, 5, 'O')
        self.assertTrue(win)

    def test_mixed_row_does_not_win(self):
        moves = [(1,1,'X'), (1,2,'O'), (1,3,'X'), (1,4,'O')]
        [self.board.add_piece(*move) for move in moves]
        win = self.board.is_winning_move(self.board.state, 1, 5, 'X')
        self.assertFalse(win)

    def test_overline_does_not_win(self):
        moves = [(1,1,'X'), (2,2,'X'), (3,3,'X'), (4,4,'X'), (6,6,'X')]
        [self.board.add_piece(*move) for move in moves]
        win = self.board.is_winning_move(self.board.state, 5, 5, 'X')
        self.assertFalse(win)
