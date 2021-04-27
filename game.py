from turns import Turns
from board import Board

class Game:
    __turns = Turns()
    __board = Board()

    def play(self):
        while not self.__board.isWon():
            if self.__turns.getPlayer():
                self.__board.printBoardPlayer()
            else:
                print("El contrincante ha jugado su turno!")
            self.__board.chooseMove(self.__turns.getPlayer())
            self.__turns.nextTurn()

        print("Winner winner chicken dinner")
        self.__board.printBoard()
        print("Thanks for playing!")

    def __init__(self, username):
        self.username = username
