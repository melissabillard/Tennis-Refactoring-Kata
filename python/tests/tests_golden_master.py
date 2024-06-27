import unittest
import json
from tennis6 import TennisGame6

class TestGoldenMaster(unittest.TestCase):
    def setUp(self):
        self.game = TennisGame6("player1", "player2")

    def generate_test_cases(self):
        test_cases = []

        # Scores égaux
        equal_scores = ["Love-All", "Fifteen-All", "Thirty-All", "Deuce"]
        for i in range(4):
            points = ["player1"] * i + ["player2"] * i
            test_cases.append({"points": points, "expected_score": equal_scores[i]})
        # Scores égaux au-delà de 3-3 (Deuce)
        test_cases.append({"points": ["player1", "player1", "player2", "player2", "player1", "player2"], "expected_score": "Deuce"})
        test_cases.append({"points": ["player1", "player1", "player2", "player2", "player1", "player2", "player1", "player2"], "expected_score": "Deuce"})

        # Avantage et victoire
        advantage_victory_cases = [
            (["player1", "player1", "player2", "player2", "player1", "player2", "player1"], "Advantage player1"),
            (["player1", "player1", "player2", "player2", "player1", "player2", "player1", "player2", "player1"], "Advantage player1"),
            (["player1", "player1", "player2", "player2", "player1", "player2", "player1", "player2", "player1", "player1"], "Win for player1"),
            (["player1", "player1", "player2", "player2", "player1", "player2", "player2"], "Advantage player2"),
            (["player1", "player1", "player2", "player2", "player1", "player2", "player2", "player1", "player2"], "Advantage player2"),
            (["player1", "player1", "player2", "player2", "player1", "player2", "player2", "player1", "player2", "player2"], "Win for player2"),
        ]
        for points, expected_score in advantage_victory_cases:
            test_cases.append({"points": points, "expected_score": expected_score})

        # Scores réguliers
        regular_scores = [("Love", "Fifteen", "Thirty", "Forty")]
        for i, player1_score in enumerate(regular_scores[0]):
            for j, player2_score in enumerate(regular_scores[0]):
                if i == j:
                    continue
                points = ["player1"] * i + ["player2"] * j
                expected_score = f"{player1_score}-{player2_score}"
                test_cases.append({"points": points, "expected_score": expected_score})

        return test_cases

    def test_golden_master_record(self):
        test_cases = self.generate_test_cases()
        with open('golden_master.json', 'w') as f:
            json.dump(test_cases, f, indent=4)

    def test_golden_master_replay(self):
        with open('golden_master.json', 'r') as f:
            test_cases = json.load(f)

        for case in test_cases:
            with self.subTest(case=case):
                self.game = TennisGame6("player1", "player2")
                for point in case["points"]:
                    self.game.won_point(point)
                self.assertEqual(self.game.score(), case["expected_score"])

    def test_player_names(self):
        game = TennisGame6("Alice", "Bob")
        self.assertEqual(game.player1Name, "Alice")
        self.assertEqual(game.player2Name, "Bob")

if __name__ == "__main__":
    unittest.main()
