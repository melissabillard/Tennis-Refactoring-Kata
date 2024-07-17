# -*- coding: utf-8 -*-
from translations import translations


class ScoreCalculator:
    def __init__(self, player1Name, player2Name, language="en"):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.language = language

    def calculate_score(self, player1Score, player2Score):
        """
        Calcule le score en fonction des scores des deux joueurs.

        Args:
            player1Score (int): Le score du premier joueur.
            player2Score (int): Le score du deuxième joueur.

        Returns:
            str: Le score formaté en fonction de la situation de jeu.
        """
        if player1Score == player2Score:
            return self._get_tie_score(player1Score)
        elif player1Score >= 4 or player2Score >= 4:
            return self._get_end_game_score(player1Score, player2Score)
        else:
            return self._get_regular_score(player1Score, player2Score)

    def _translate(self, key):
        """
        Traduit une clé de score en utilisant le dictionnaire de traductions.

        Args:
            key (str): La clé de score à traduire.

        Returns:
            str: La traduction de la clé en fonction de la langue.
        """
        return translations[key][self.language]

    def _get_tie_score(self, score):
        """
        Obtenu le score en cas d'égalité.

        Args:
            score (int): Le score actuel des deux joueurs.

        Returns:
            str: Le score formaté pour une égalité.
        """
        tie_scores = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }
        return self._translate(tie_scores.get(score, "Deuce"))

    def _get_end_game_score(self, player1Score, player2Score):
        """
        Obtenu le score en fin de partie.

        Args:
            player1Score (int): Le score du premier joueur.
            player2Score (int): Le score du deuxième joueur.

        Returns:
            str: Le score formaté pour la fin de partie.
        """
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
        """
        Obtenu le score régulier en fonction des points des joueurs.

        Args:
            player1Score (int): Le score du premier joueur.
            player2Score (int): Le score du deuxième joueur.

        Returns:
            str: Le score formaté pour un jeu régulier.
        """
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
        """
        Incrémente le score du joueur ayant gagné un point.

        Args:
            playerName (str): Le nom du joueur ayant gagné le point.
        """
        if playerName == self.player1Name:
            self.player1Score += 1
        else:
            self.player2Score += 1

    def score(self):
        """
        Calcule et retourne le score actuel.

        Returns:
            str: Le score actuel formaté.
        """
        return self.score_calculator.calculate_score(self.player1Score, self.player2Score)
