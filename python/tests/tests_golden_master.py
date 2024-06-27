import unittest
from tennis6 import TennisGame6

class TestGoldenMaster(unittest.TestCase):
    def setUp(self):
        self.game = TennisGame6("player1", "player2")

    def test_golden_master(self):
        test_cases = [
            {"points": [], "expected_score": "Love-All"},
            {"points": ["player1"], "expected_score": "Fifteen-Love"},
            {"points": ["player1", "player1"], "expected_score": "Thirty-Love"},
            {"points": ["player1", "player1", "player1"], "expected_score": "Forty-Love"},
            {"points": ["player1", "player1", "player1", "player1"], "expected_score": "Win for player1"},
            {"points": ["player2"], "expected_score": "Love-Fifteen"},
            {"points": ["player2", "player2"], "expected_score": "Love-Thirty"},
            {"points": ["player2", "player2", "player2"], "expected_score": "Love-Forty"},
            {"points": ["player2", "player2", "player2", "player2"], "expected_score": "Win for player2"},
            {"points": ["player1", "player2"], "expected_score": "Fifteen-All"},
            {"points": ["player1", "player1", "player2"], "expected_score": "Thirty-Fifteen"},
            {"points": ["player1", "player1", "player2", "player2"], "expected_score": "Thirty-All"},
            {"points": ["player1", "player1", "player2", "player2", "player1"], "expected_score": "Forty-Thirty"},
            {"points": ["player1", "player1", "player2", "player2", "player1", "player2"], "expected_score": "Deuce"},
            {"points": ["player1", "player1", "player2", "player2", "player1", "player2", "player1"], "expected_score": "Advantage player1"},
            {"points": ["player1", "player1", "player2", "player2", "player1", "player2", "player1", "player2"], "expected_score": "Deuce"},
            {"points": ["player1", "player1", "player2", "player2", "player1", "player2", "player1", "player2", "player1"], "expected_score": "Advantage player1"},
            {"points": ["player1", "player1", "player2", "player2", "player1", "player2", "player1", "player2", "player1", "player1"], "expected_score": "Win for player1"}
        ]

        for case in test_cases:
            with self.subTest(case=case):
                self.game = TennisGame6("player1", "player2")
                for point in case["points"]:
                    self.game.won_point(point)
                self.assertEqual(self.game.score(), case["expected_score"])

if __name__ == "__main__":
    unittest.main()
