import unittest
from tennis6 import TennisGame6

class TennisGame6:
    SCORES = {
        "tie": ["Love-All", "Fifteen-All", "Thirty-All", "Deuce"],
        "regular": ["Love", "Fifteen", "Thirty", "Forty"],
        "advantage": "Advantage",
        "win": "Win for"
    }

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Score = 0
        self.player2Score = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.player1Score += 1
        else:
            self.player2Score += 1

    def calculate_score(self):
        if self.player1Score == self.player2Score:
            if self.player1Score < 3:
                return TennisGame6.SCORES["tie"][self.player1Score]
            else:
                return TennisGame6.SCORES["tie"][3]  # "Deuce"
        elif self.player1Score >= 4 or self.player2Score >= 4:
            score_diff = self.player1Score - self.player2Score
            if score_diff == 1:
                return f"{TennisGame6.SCORES['advantage']} {self.player1Name}"
            elif score_diff == -1:
                return f"{TennisGame6.SCORES['advantage']} {self.player2Name}"
            elif score_diff >= 2:
                return f"{TennisGame6.SCORES['win']} {self.player1Name}"
            else:
                return f"{TennisGame6.SCORES['win']} {self.player2Name}"
        else:
            score1 = TennisGame6.SCORES["regular"][self.player1Score]
            score2 = TennisGame6.SCORES["regular"][self.player2Score]
            return f"{score1}-{score2}"

    def score(self):
        return self.calculate_score()

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
            {"points": ["player1", "player1", "player2", "player2", "player1", "player2", "player1", "player2", "player1", "player1"], "expected_score": "Win for player1"},
            {"points": ["player2", "player2", "player1", "player1"], "expected_score": "Thirty-All"},
            {"points": ["player2", "player2", "player2", "player1", "player1", "player1"], "expected_score": "Deuce"},
            {"points": ["player2", "player2", "player2", "player1", "player1", "player1", "player2"], "expected_score": "Advantage player2"},
            {"points": ["player2", "player2", "player2", "player1", "player1", "player1", "player2", "player1"], "expected_score": "Deuce"},
            {"points": ["player2", "player2", "player2", "player1", "player1", "player1", "player2", "player1", "player2"], "expected_score": "Advantage player2"},
            {"points": ["player2", "player2", "player2", "player1", "player1", "player1", "player2", "player1", "player2", "player2"], "expected_score": "Win for player2"}
        ]

        for case in test_cases:
            with self.subTest(case=case):
                self.game = TennisGame6("player1", "player2")
                for point in case["points"]:
                    self.game.won_point(point)
                self.assertEqual(self.game.score(), case["expected_score"])

if __name__ == "__main__":
    unittest.main()
