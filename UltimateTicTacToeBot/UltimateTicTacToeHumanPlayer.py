from math import floor
from re import L


class board:
    def __init__(self):
        self.array = [[0 for num in range(3)] for num in range(3)]
        self.isWon = False
        self.winningChar = -1

    def makeMove(self, char, num):
        x = num %3
        y = floor(num/3)
        """sets coord to char"""
        self.array[y][x] = char
        return self.updateWinState()
    
    def updateWinState(self):
        #check rows
        for y in range(3):
            if self.array[y][0] == self.array[y][1] and self.array[y][1] == self.array[y][2] and self.array[y][0] != 0:
                self.isWon = True
                self.winningChar = self.array[y][0]
                return self.isWon, self.winningChar
        #check columns
        for x in range(3):
            if self.array[0][x] == self.array[1][x] and self.array[1][x] == self.array[2][x] and self.array[0][x] != 0:
                self.isWon = True
                self.winningChar = self.array[0][x]
                return self.isWon, self.winningChar
        #check top left to bottom right diagonal
        if self.array[0][0] == self.array[1][1] and self.array[1][1] == self.array[2][2] and self.array[0][0] != 0:
            self.isWon = True
            self.winningChar = self.array[0][0]
            return self.isWon, self.winningChar
        if self.array[2][0] == self.array[1][1] and self.array[1][1] == self.array[0][2] and self.array[2][0] != 0:
            self.isWon = True
            self.winningChar = self.array[2][0]
            return self.isWon, self.winningChar
        return False, -1
    
    def isWonGet(self):
        return self.isWon

    def getArray(self):
        return self.array

class mainBoard():
    def __init__(self):
        self.array = [[board() for num in range(3)] for num in range(3)]
        self.controlBoard = board()
    
    def isWonGet(self):
        return self.controlBoard.isWonGet()

    def makeMove(self, char, num1, num2):
        x = num1 %3
        y = floor(num1/3)
        win, _ = self.array[y][x].makeMove(char, num2)
        if win:
            self.controlBoard.makeMove(char, num1)
        return self.isWonGet()

    def __str__(self):
        outstr = """"""
        fullarray = [[0 for num in range(9)] for num in range(9)]
        for y in range(3):
            for x in range(3):
                subarray = self.array[y][x].getArray()
                for suby in range(3):
                    for subx in range(3):
                        if subarray[suby][subx] != 0: fullarray[3*y+suby][3*x+subx] = subarray[suby][subx]
                        else: fullarray[3*y+suby][3*x+subx] = "-"

        for y in range(9):
            for x in range(9):
                if x == 2 or x ==5:
                    outstr += str(fullarray[y][x])+ " | "
                else:
                    outstr += str(fullarray[y][x]) + " "
            outstr+= "\n"
            if y == 2 or y ==5:
                outstr+= "---------------------\n"
        return outstr
        

    def getSubBoardState(self, subBoardIndex):
        x = subBoardIndex %3
        y = floor(subBoardIndex/3)
        return self.array[y][x].isWonGet()

class game():
    def __init__(self):
        self.board = mainBoard()
        self.currentChar = "X"
        self.constraint = -1
        self.gameOver = False

    def turn(self, num2):
        win = self.board.makeMove(self.currentChar, self.constraint, num2)
        if win:
            print(win)
            self.gameOver = True
            print("GAME OVER!!!")
            print("WINNER:", self.currentChar)
        else:
            if self.currentChar == "X": self.currentChar = "O"
            else: self.currentChar = "X"

            if self.board.getSubBoardState(num2):
                self.constraint = -1
            else:
                self.constraint = num2
    
    def runGame(self):
        while not(self.gameOver):
            print(self.board)
            if self.constraint == -1:
                self.constraint = int(input("Which board would you like to play on?"))
            num = int(input("Which square would you like to play?"))
            self.turn(num)



            

        








def __main__():
    mainGame = game()
    mainGame.runGame()



if __name__ == "__main__":
    __main__()