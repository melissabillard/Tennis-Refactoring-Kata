# -*- coding: utf-8 -*-

# noms de variables plus conformes aux conventions Python
class TennisGame6:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Score = 0
        self.player2Score = 0

    def won_point(self, playerName):
        # playerName devrait être validé contre les noms réels des joueurs
        if (playerName == "player1"): 
            self.player1Score += 1
        # On suppose implicitement que tout non-"player1" est "player2", ce qui peut introduire des erreurs
        else:
            self.player2Score += 1 
    def score(self):
        # La déclaration de variables locales pas habituelle en Python, peut être omise
        result: str

        if (self.player1Score == self.player2Score):
            # tie score
            # La déclaration de variables locales pas habituelle en Python, peut être omise
            tieScore: str
            match self.player1Score:
                case 0:
                    tieScore = "Love-All"
                case 1:
                    tieScore = "Fifteen-All"
                case 2:
                    tieScore = "Thirty-All"
                case _:
                    tieScore = "Deuce"

            result = tieScore
        elif (self.player1Score >= 4 or self.player2Score >= 4):
            # end-game score
            endGameScore: str

            if (self.player1Score - self.player2Score == 1):
                endGameScore = "Advantage " + self.player1Name
            elif (self.player1Score - self.player2Score == -1):
                endGameScore = "Advantage " + self.player2Name
            elif (self.player1Score - self.player2Score >= 2):
                endGameScore = "Win for " + self.player1Name
            else:
                endGameScore = "Win for " + self.player2Name

            # On pourrait directement affecter à result pour éviter une variable en plus   
            result = endGameScore
        else:
            # regular score
            # On pourrait directement manipuler result
            regularScore: str

            # On pourrai extraire la logique répétitive des match dans une méthode séparée
            match (self.player1Score):
                case 0:
                    score1 = "Love"
                case 1:
                    score1 = "Fifteen"
                case 2:
                    score1 = "Thirty"
                case _:
                    score1 = "Forty"

            match (self.player2Score):
                case 0:
                    score2 = "Love"
                case 1:
                    score2 = "Fifteen"
                case 2:
                    score2 = "Thirty"
                case _:
                    score2 = "Forty"

            # Encore une fois, on pourrait affecter directement result (variable regularScore pas trop necessaire)
            regularScore = score1 + "-" + score2

            result = regularScore

        return result
