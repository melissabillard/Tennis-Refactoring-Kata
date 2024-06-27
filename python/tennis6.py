# -*- coding: utf-8 -*-
from translations import translations


class ScoreCalculator:
    def __init__(self, player1Name, player2Name, language="en"):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.language = language

    def calculate_score(self, player1Score, player2Score):
        if player1Score == player2Score:
            return self._get_tie_score(player1Score)
        elif player1Score >= 4 or player2Score >= 4:
            return self._get_end_game_score(player1Score, player2Score)
        else:
            return self._get_regular_score(player1Score, player2Score)

    def _translate(self, key):
        return translations[key][self.language]

    def _get_tie_score(self, score):
        tie_scores = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }
        return self._translate(tie_scores.get(score, "Deuce"))

    def _get_end_game_score(self, player1Score, player2Score):
        score_diff = player1Score - player2Score
        if score_diff == 1:
            return f"{self._translate('Advantage player1')}"
        elif score_diff == -1:
            return f"{self._translate('Advantage player2')}"
        elif score_diff >= 2:
            return f"{self._translate('Win for player1')}"
        else:
            return f"{self._translate('Win for player2')}"

    def _get_regular_score(self, player1Score, player2Score):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        score1 = self._translate(score_names[player1Score])
        score2 = self._translate(score_names[player2Score])
        return f"{score1}-{score2}"


class TennisGame6:
    def __init__(self, player1Name, player2Name, language="en"):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Score = 0
        self.player2Score = 0
        self.score_calculator = ScoreCalculator(player1Name, player2Name, language)

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.player1Score += 1
        else:
            self.player2Score += 1

    def score(self):
        return self.score_calculator.calculate_score(self.player1Score, self.player2Score)
