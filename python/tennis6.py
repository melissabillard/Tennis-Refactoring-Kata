# -*- coding: utf-8 -*-
from translations import translations

class TennisGame6:
    def __init__(self, player1Name, player2Name, language="en"):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Score = 0
        self.player2Score = 0
        self.language = language
        self.translations = translations[language]

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.player1Score += 1
        else:
            self.player2Score += 1

    def calculate_score(self):
        if self.player1Score == self.player2Score:
            if self.player1Score < 3:
                return self.translations["tie"][self.player1Score]
            else:
                return self.translations["tie"][3]  # "Deuce"
        elif self.player1Score >= 4 or self.player2Score >= 4:
            score_diff = self.player1Score - self.player2Score
            if score_diff == 1:
                return f"{self.translations['advantage']} {self.player1Name}"
            elif score_diff == -1:
                return f"{self.translations['advantage']} {self.player2Name}"
            elif score_diff >= 2:
                return f"{self.translations['win']} {self.player1Name}"
            else:
                return f"{self.translations['win']} {self.player2Name}"
        else:
            score1 = self.translations["regular"][self.player1Score]
            score2 = self.translations["regular"][self.player2Score]
            return f"{score1}-{score2}"

    def score(self):
        return self.calculate_score()
