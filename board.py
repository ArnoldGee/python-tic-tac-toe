from random import randint

class Board:
    __board = []
    __numbers = []

    def __init__(self):
        for i in range(1, 4):
            self.__board.append([" "] * 3)
            self.__numbers.append(range(i * 3 - 2, i * 3 + 1))

    def printArrayBoard(self, myArray):
        print("\n+-+-+-+")
        for row in myArray:
            rowString = "|"
            for symbol in row:
                rowString += (str(symbol) + "|")
            print(rowString)
            print("+-+-+-+")
    
    def printBoard(self):
        self.printArrayBoard(self.__board)

    def printBoardPlayer(self):
        self.printBoard()
        print("Elige un número:")
        self.printArrayBoard(self.__numbers)

    def printBoardEnemy(self):
        print("Jugada del contrincante")
        self.printBoard()

    def addMove(self, player, row, column):
        self.__board[row][column] = 'x' if player else 'o'

    def chooseMove(self, player):
        if player:
            playerInput = input()
            number = int(playerInput)
            row = (number - 1) // 3
            column = (number - 1) % 3
        else:
            row = randint(0, 2)
            column = randint(0, 2)
            while(self.__board[row][column] != ' '):
                row = randint(0, 2)
                column = randint(0, 2)
        self.addMove(player, row, column)

    def __areEqualSymbols(self, array):
        if array[0] == ' ':
            return False
        symbol = array[0]
        for element in array:
            if element != symbol:
                return False
        return True

    def isWon(self):  # The winner is the turn
        for column in self.__board:
            if self.__areEqualSymbols(column):
                return True

        for i in range(0, len(self.__board)):
            row = []
            for j in range(0, len(self.__board[0])):
                row.append(self.__board[j][i])
            if self.__areEqualSymbols(row):
                return True

        diagonalLine = []
        for i in range(0, len(self.__board)):
            diagonalLine.append(self.__board[i][i])
        if self.__areEqualSymbols(diagonalLine):
            return True

        reverseDiagonalLine = []
        for i in range(0, len(self.__board)):
            reverseDiagonalLine.append(
                self.__board[i][len(self.__board) - 1 - i])
        if self.__areEqualSymbols(reverseDiagonalLine):
            return True
        return False 