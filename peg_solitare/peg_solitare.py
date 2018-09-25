from copy import deepcopy as copy
import numpy as np


class linkedlist():
    def __init__(self, board):
        self.val = copy(board)
        self.child = None  # jump to this child from current board
        self.jumpfrom = None
        self.jumpto = None


class board:
    def __init__(self, row_of_hole, col_of_hole):
        self.size = 5
        self.HolePos = [row_of_hole, col_of_hole]
        # 1 is peg. 0 is hole.
        self.board = [[1 for j in range(i + 1)] for i in range(self.size)]
        self.board[row_of_hole][col_of_hole] = 0
        self.start = linkedlist(self.board)
        self.current = self.start

    def drawBoard(self, board):
        for i in range(self.size):
            for j in range(self.size - i - 1):
                print('', end=' ')
            for j in board[i]:
                if j == 1:
                    print('+', end=' ')
                else:
                    print('o', end=' ')
            print()

    def success(self):
        tmp = sum([sum(i) for i in self.board])
        if tmp == 1:
            # Uncomment these two lines if you want to test that the last peg is in the original hole position.
            # if self.board[self.HolePos[0]][self.HolePos[1]] == 1:
            #    return True
            return True
        return False

    def printSolution(self):
        if self.success():
            self.current = self.start
            while self.current.child:
                self.drawBoard(self.current.val)
                print(self.current.jumpfrom, "to ", self.current.jumpto)
                self.current = self.current.child
            self.drawBoard(self.current.val)
        else:
            print("No solution has been found yet!")

    def solve(self):
        if self.success():
            return True
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:

                    # checking right
                    if col + 2 <= row:
                        # print 'checking right'
                        if self.board[row][col + 1] == 1 and self.board[row][col + 2] == 1:
                            parent = self.current
                            self.board[row][col + 1] = 0
                            self.board[row][col + 2] = 0
                            self.board[row][col] = 1
                            self.current = linkedlist(self.board)
                            parent.child = self.current
                            parent.jumpfrom = '[%s][%s]' % (row, col + 2)
                            parent.jumpto = '[%s][%s]' % (row, col)
                            if self.solve():
                                return True
                            else:
                                self.current = parent
                                self.board = copy(parent.val)

                    # checking left
                    if col - 2 >= 0:
                        # print 'checking left'
                        if self.board[row][col - 1] == 1 and self.board[row][col - 2] == 1:
                            parent = self.current
                            self.board[row][col - 1] = 0
                            self.board[row][col - 2] = 0
                            self.board[row][col] = 1
                            self.current = linkedlist(self.board)
                            parent.child = self.current
                            parent.jumpfrom = '[%s][%s]' % (row, col - 2)
                            parent.jumpto = '[%s][%s]' % (row, col)
                            if self.solve():
                                return True
                            else:
                                self.current = parent
                                self.board = copy(parent.val)

                        # checking top-left
                    if row - 2 >= 0 and col - 2 >= 0:
                        # print 'checking top-left'
                        if self.board[row - 1][col - 1] == 1 and self.board[row - 2][col - 2] == 1:
                            parent = self.current
                            self.board[row - 1][col - 1] = 0
                            self.board[row - 2][col - 2] = 0
                            self.board[row][col] = 1
                            self.current = linkedlist(self.board)
                            parent.child = self.current
                            parent.jumpfrom = '[%s][%s]' % (row - 2, col - 2)
                            parent.jumpto = '[%s][%s]' % (row, col)
                            if self.solve():
                                return True
                            else:
                                self.current = parent
                                self.board = copy(parent.val)

                    # checking top-right
                    if row - 2 >= 0 and col <= row - 2:
                        # print 'checking top-right'
                        if self.board[row - 1][col] == 1 and self.board[row - 2][col] == 1:
                            parent = self.current
                            self.board[row - 1][col] = 0
                            self.board[row - 2][col] = 0
                            self.board[row][col] = 1
                            self.current = linkedlist(self.board)
                            parent.child = self.current
                            parent.jumpfrom = '[%s][%s]' % (row - 2, col + 2)
                            parent.jumpto = '[%s][%s]' % (row, col)
                            if self.solve():
                                return True
                            else:
                                self.current = parent
                                self.board = copy(parent.val)

                    # checking bottom-left
                    if row + 2 < len(self.board) and col <= row + 2:
                        # print 'checking bottom-left'
                        if self.board[row + 1][col] == 1 and self.board[row + 2][col] == 1:
                            parent = self.current
                            # print self.board
                            self.board[row + 1][col] = 0
                            self.board[row + 2][col] = 0
                            self.board[row][col] = 1
                            self.current = linkedlist(self.board)
                            parent.child = self.current
                            parent.jumpfrom = '[%s][%s]' % (row + 2, col - 2)
                            parent.jumpto = '[%s][%s]' % (row, col)
                            if self.solve():
                                return True
                            else:
                                self.current = parent
                                self.board = copy(parent.val)

                    # checking bottom-right
                    if row + 2 < len(self.board) and col + 2 <= row + 2:
                        # print 'checking bottom-right'
                        if self.board[row + 1][col + 1] == 1 and self.board[row + 2][col + 2] == 1:
                            parent = self.current
                            self.board[row + 1][col + 1] = 0
                            self.board[row + 2][col + 2] = 0
                            self.board[row][col] = 1
                            self.current = linkedlist(self.board)
                            parent.child = self.current
                            parent.jumpfrom = '[%s][%s]' % (row + 2, col + 2)
                            parent.jumpto = '[%s][%s]' % (row, col)
                            if self.solve():
                                return True
                            else:
                                self.current = parent
                                self.board = copy(parent.val)

        return False

        # if one peg can be jumped from this position:
        # update self.board and .child, .jumpfrom, .jumpto of current parent node

        # recursively call self.solve()
        # return true if it finds one solution

        # withdraw the previous updating if it does not find one solution

        # return false if no available position on current board


startHoleRow, startHoleCol = np.inf, np.inf
while startHoleRow > 4:
    startHoleRow = int(input("Please input row of the hole (<=4):"))
while startHoleCol > startHoleRow:
    startHoleCol = int(input("Please input column of the hole (<=row):"))

game = board(startHoleRow, startHoleCol)
game.solve()
game.printSolution()
