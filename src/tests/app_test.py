import unittest
from app import App
from ai_player import AIPlayer


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App(['Robert', 'Pierre'], 5, True, False)

    def test_app_is_created(self):
        self.assertEqual(self.app.names, ['Robert', 'Pierre'])
        self.assertIsInstance(self.app.players[0], AIPlayer)

    def test_app_can_run_short_game(self):
        pass