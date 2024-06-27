# -*- coding: utf-8 -*-
class TennisGame6:
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

    def score(self):
        if self.player1Score == self.player2Score:
            return self._get_tie_score()
        elif self.player1Score >= 4 or self.player2Score >= 4:
            return self._get_end_game_score()
        else:
            return self._get_regular_score()

    def _get_tie_score(self):
        if self.player1Score < 3:
            return f"{self._score_to_string(self.player1Score)}-All"
        else:
            return "Deuce"

    def _get_end_game_score(self):
        score_difference = self.player1Score - self.player2Score
        if score_difference == 1:
            return f"Advantage {self.player1Name}"
        elif score_difference == -1:
            return f"Advantage {self.player2Name}"
        elif score_difference >= 2:
            return f"Win for {self.player1Name}"
        else:
            return f"Win for {self.player2Name}"

    def _get_regular_score(self):
        return f"{self._score_to_string(self.player1Score)}-{self._score_to_string(self.player2Score)}"
