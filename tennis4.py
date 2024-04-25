# -*- coding: utf-8 -*-

class TennisGame4:
    def __init__(self, player1Name, player2Name):
        self.server = player1Name
        self.receiver = player2Name
        self.serverScore = 0
        self.receiverScore = 0

    def won_point(self, playerName):
        if self.server == playerName:
            self.serverScore += 1
        else:
            self.receiverScore += 1

    def score(self):
        # La méthode score est complexe on pourrait la simplifiée pour une meilleure lisibilité.
        # utilise beaucoup d'objets et de méthodes
        result = Deuce(
            self, GameServer(
                self, GameReceiver(
                    self, AdvantageServer(
                        self, AdvantageReceiver(
                            self, DefaultResult(self)))))).getResult()
        return result.format()
    
    #  def score(self):
    #     # Si c'est un Deuce
    #     if self.is_deuce():
    #         return "Deuce"
    #     # Si quelqu'un a gagné
    #     if self.server_has_won():
    #         return "Win for " + self.server
    #     if self.receiver_has_won():
    #         return "Win for " + self.receiver
    #     # Si quelqu'un a un avantage
    #     if self.server_has_advantage():
    #         return "Advantage " + self.server
    #     if self.receiver_has_advantage():
    #         return "Advantage " + self.receiver
    #     # Sinon, retourne le score actuel
    #     return TennisResult(
    #         self.scores[self.server_score],
    #         self.scores[self.receiver_score]
    #     ).format()

   # Dans cet exemple, j'ai supprimé les appels imbriqués à différentes classes et méthodes, 
   # ce qui simplifie grandement la logique de la méthode score. 

    # il faudrait revoir le nommage des def pour harmoniser et avoir du snake_case : en minuscules avec des underscores entre les mots (c frutrant XD)
    def receiverHasAdvantage(self):
        return self.receiverScore >= 4 and (self.receiverScore - self.serverScore) == 1

    def serverHasAdvantage(self):
        return self.serverScore >= 4 and (self.serverScore - self.receiverScore) == 1

    def receiverHasWon(self):
        return self.receiverScore >= 4 and (self.receiverScore - self.serverScore) >= 2

    def serverHasWon(self):
        return self.serverScore >= 4 and (self.serverScore - self.receiverScore) >= 2

    def isDeuce(self):
        return self.serverScore >= 3 and self.receiverScore >= 3 and (self.serverScore == self.receiverScore)


class TennisResult:
    def __init__(self, serverScore, receiverScore):
        self.serverScore = serverScore
        self.receiverScore = receiverScore

    def format(self):
        if "" == self.receiverScore:
            return self.serverScore
        if self.serverScore == self.receiverScore:
            return self.serverScore + "-All"
        return self.serverScore + "-" + self.receiverScore

    #  L'initialisation de TennisResult est faite avec "" dans le cas où receiverScore est vide. 
    # Cette vérification est inutile, car receiverScore est toujours initialisé. 
    # Il suffit de vérifier si receiverScore est égal à "".
    
    # Ex : correction
    
    # class TennisResult:
    # def __init__(self, server_score, receiver_score):
    #     self.server_score = server_score
    #     self.receiver_score = receiver_score

    # def format(self):
    #     if self.receiver_score == "":
    #         # Correction : Utilisation de la chaîne vide directement sans vérification.
    #         return self.server_score
    #     if self.server_score == self.receiver_score:
    #         return self.server_score + "-All"
    #     return self.server_score + "-" + self.receiver_score


class Deuce:
    def __init__(self, game, nextResult):
        self.game = game
        self.nextResult = nextResult

    def getResult(self):
        if (self.game.isDeuce()):
            return TennisResult("Deuce", "")
        return self.nextResult.getResult()


class GameServer:
    def __init__(self, game, nextResult):
        self.game = game
        self.nextResult = nextResult

    def getResult(self):
        if (self.game.serverHasWon()):
            return TennisResult("Win for " + self.game.server, "")
        return self.nextResult.getResult()


class GameReceiver:
    def __init__(self, game, nextResult):
        self.game = game
        self.nextResult = nextResult

    def getResult(self):
        if (self.game.receiverHasWon()):
            return TennisResult("Win for " + self.game.receiver, "")
        return self.nextResult.getResult()


class AdvantageServer:
    def __init__(self, game, nextResult):
        self.game = game
        self.nextResult = nextResult

    def getResult(self):
        if (self.game.serverHasAdvantage()):
            return TennisResult("Advantage " + self.game.server, "")
        return self.nextResult.getResult()


class AdvantageReceiver:
    def __init__(self, game, nextResult):
        self.game = game
        self.nextResult = nextResult

    def getResult(self):
        if (self.game.receiverHasAdvantage()):
            return TennisResult("Advantage " + self.game.receiver, "")
        return self.nextResult.getResult()


class DefaultResult:
    def __init__(self, game):
        self.game = game
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def getResult(self):
        return TennisResult(self.scores[self.game.serverScore], self.scores[self.game.receiverScore])
