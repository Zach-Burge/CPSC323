from copy import deepcopy
from queue import Empty
import random


class NimPlayer:
    def __init__(self) -> None:
        pass

    def play(self, boardstate):
        new_boardstate = []
        possible_moves = []
        best_moves = []
        # Get the possible moves from boardstate
        for idx, row in enumerate(boardstate):
            for i in list(range(row + 1)):
                temp_board = deepcopy(boardstate)
                new_row = row - i
                temp_board[idx] = new_row
                if temp_board != boardstate:
                    possible_moves.append(temp_board)
        # use nim sum to get the best moves from the possible moves
        # ie if the nim sum is 0, it goes in best moves
        for move in possible_moves:
            nim_sum = move[0] ^ move[1] ^ move[2] ^ move[3]
            if nim_sum == 0:
                best_moves.append(move)

        # if none of the possible moves have a nim sum of 0, check if the binary sum of any of the row values and the nim sum is less than the length of that row, 
        # and if so, set that row to be its new row nim value and add it to best moves
        temp_board = deepcopy(boardstate) 
        for idx, row in enumerate(temp_board):
            row_nim = nim_sum ^ row
            if row_nim < row:
                temp_board[idx] = row_nim
                if temp_board not in best_moves:
                    best_moves.append(temp_board)
                    break       
        if best_moves != []:
            new_boardstate = best_moves[0]
        else:
            # if there are no best moves, choose a random move from the possible moves and make that
            new_boardstate = possible_moves[random.randrange(0, len(possible_moves)-1)]
        return new_boardstate