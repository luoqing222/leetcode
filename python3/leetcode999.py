__author__ = 'Qing'
#On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.
# These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces,
# and lowercase characters represent black pieces.
#The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south),
# then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving
# to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.
#Return the number of pawns the rook can capture in one move.

from typing import List
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        row, col, r, c = len(board), len(board[0]), 0, 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='R':
                    r, c = i, j
                    break
        dirs, steps = [(-1,0),(1,0),(0,1),(0,-1)], 0
        for dir in dirs:
            start = (r,c)
            while 0<=start[0]+dir[0]<row and 0<=start[1]+dir[1]<col:
                x,y = start[0]+dir[0], start[1]+dir[1]
                if board[x][y]=='p':
                    steps+=1
                    break
                if board[x][y]=='B':
                    break
                if board[x][y]=='.':
                    start =(x,y)
        return steps
