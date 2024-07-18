# -*- coding: utf-8 -*-
from translations import translations

class ScoreCalculator:
    def __init__(self, player1_name, player2_name, language="en"):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.language = language

    def calculate_score(self, player1_score, player2_score):
        """
        Calcule le score en fonction des scores des deux joueurs.

        Args:
            player1_score (int): Le score du premier joueur.
            player2_score (int): Le score du deuxième joueur.

        Returns:
            str: Le score formaté en fonction de la situation de jeu.
        """
        if player1_score == player2_score:
            return self._get_tie_score(player1_score)
        elif player1_score >= 4 or player2_score >= 4:
            return self._get_end_game_score(player1_score, player2_score)
        else:
            return self._get_regular_score(player1_score, player2_score)

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

    def _get_end_game_score(self, player1_score, player2_score):
        """
        Obtenu le score en fin de partie.

        Args:
            player1_score (int): Le score du premier joueur.
            player2_score (int): Le score du deuxième joueur.

        Returns:
            str: Le score formaté pour la fin de partie.
        """
        score_diff = player1_score - player2_score
        if score_diff == 1:
            return f"{self._translate('Advantage player1')}"
        elif score_diff == -1:
            return f"{self._translate('Advantage player2')}"
        elif score_diff >= 2:
            return f"{self._translate('Win for player1')}"
        else:
            return f"{self._translate('Win for player2')}"

    def _get_regular_score(self, player1_score, player2_score):
        """
        Obtenu le score régulier en fonction des points des joueurs.

        Args:
            player1_score (int): Le score du premier joueur.
            player2_score (int): Le score du deuxième joueur.

        Returns:
            str: Le score formaté pour un jeu régulier.
        """
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        score1 = self._translate(score_names[player1_score])
        score2 = self._translate(score_names[player2_score])
        return f"{score1}-{score2}"

class TennisGame6:
    def __init__(self, player1_name, player2_name, language="en"):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score_calculator = ScoreCalculator(player1_name, player2_name, language)

    def won_point(self, player_name):
        """
        Incrémente le score du joueur ayant gagné un point.

        Args:
            player_name (str): Le nom du joueur ayant gagné le point.
        """
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score(self):
        """
        Calcule et retourne le score actuel.

        Returns:
            str: Le score actuel formaté.
        """
        return self.score_calculator.calculate_score(self.player1_score, self.player2_score)