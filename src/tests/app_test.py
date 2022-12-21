import unittest
from app import App
from ai_player import AIPlayer


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App(['Tester', 'Tester'], 5, True, False, False)

    def test_app_is_created(self):
        self.assertEqual(self.app.names, ['Tester', 'Tester'])
        self.assertIsInstance(self.app.players[0], AIPlayer)

    def test_app_can_run_short_game(self):
        result = self.app.run()
        self.assertEqual(result.split(',')[4], 'draw')
