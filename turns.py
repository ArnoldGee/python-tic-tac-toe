from random import randint

class Turns:
    __currentTurn = 1
    # True = you go first, False = the computer goes first
    __player = bool(randint(0, 1))

    def getCurrentTurn(self):
        return self.__currentTurn

    def getPlayer(self):
        return self.__player

    def nextTurn(self):
        self.__currentTurn += 1
        self.__player = not self.__player

    def reset(self):
        self.__currentTurn = 1