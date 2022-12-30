import unittest
import pytest
from app import App
from ai_player import AIPlayer


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App(['Tester', 'Tester'], 5, True, False, False)

    def test_app_is_created(self):
        self.assertEqual(self.app.names, ['Tester', 'Tester'])
        self.assertIsInstance(self.app.players[0], AIPlayer)

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_app_can_run_short_game_that_ends_in_draw(self):
        result = self.app.run()
        self.assertEqual(result.split(',')[4], 'draw')

    def test_app_can_run_short_game_that_ends_in_win(self):
        self.app.board.add_piece(5, 7, 'X')
        self.app.board.add_piece(6, 7, 'X')
        self.app.board.add_piece(7, 7, 'X')
        self.app.board.add_piece(8, 7, 'X')
        result = self.app.run()
        self.assertEqual(result.split(',')[4], 'Tester')

    def test_app_output_win(self):
        output_app = App(['Tester', 'Tester'], 5, False, False, False)
        output_app.board.add_piece(5, 7, 'X')
        output_app.board.add_piece(6, 7, 'X')
        output_app.board.add_piece(7, 7, 'X')
        output_app.board.add_piece(8, 7, 'X')
        result = output_app.run()
        out, err = self.capsys.readouterr()
        lines = out.split('\n')
        self.assertEqual('Tester vs Tester', lines[0])
        self.assertEqual('  000000000011111', lines[1])
        self.assertEqual('Place X (0, 0) steps from the center', lines[19])
        self.assertEqual('Tester (X) wins on turn 1!', lines[-3])

    def test_app_output_draw(self):
        output_app = App(['Tester', 'Tester'], 5, False, False, False)
        result = output_app.run()
        out, err = self.capsys.readouterr()
        lines = out.split('\n')
        self.assertEqual('Tester vs Tester', lines[0])
        self.assertEqual('  000000000011111', lines[1])
        self.assertEqual('Place X (0, 0) steps from the center', lines[19])
        self.assertEqual('Draw!', lines[-3])
