from copy import deepcopy
import random

class Game:
    def __init__(self, num_blocks):
        self.num_blocks = num_blocks
        self.grid = []
        for i in range(num_blocks):
            self.grid.append([])

    # Method to print the grid
    # Learned how to use end= from 'https://www.toppr.com/guides/python-guide/questions/what-does-end-do-in-python/#:~:text=The%20end%20parameter%20in%20the,the%20print%20statement%20in%20python.'
    # Which gave me the idea to print the lists this way
    def show_grid(self):
        for row in self.grid:
            print(row)
        print()
        
    # Initial game state 
    def setup_blocks(self):
        for i in range(1, self.num_blocks + 1):
            rand_loc = random.randrange(self.num_blocks)
            self.grid[rand_loc].append(i)
    
    # If the state of the blocks is [1, 2, 3, ..., num_blocks], the game is solved and this will return true
    def is_solved(self):
        solved = list(range(1, self.num_blocks + 1)) # [1, 2, 3, ..., num_blocks]
        for row in self.grid:
            if row == solved:
                return True
        return False

    # moves the top value in the from_idx row to the top of the to_idx row 
    def move_block(self, state, from_idx, to_idx):
        return state[to_idx].append(state[from_idx].pop())

    # Main game loop that counts the number of moves taken to solve the game
    def solve(self):
        moves = 0
        while(self.is_solved() == False):
            self.show_grid()
            self.find_possible_moves()
            moves += 1
        print("Blocks world solved in", moves, "moves.")

    def calculate_h(self, state):
        h = 0
        for row in state:
            if len(state) > 0:
                # find where 1 is, if it is not at the beginning of the row, add penalty
                if 1 in row:
                    if row.index(1) != 0:
                        # we have to move all the blocks on top of 1 plus we have to move 1
                        h += (self.num_blocks + row.index(1))
                    else:
                        # 1 is at the beginning of the row, so the rest in that row should be in ascending order
                        ascending = True
                        for block in range(len(row)-1):
                            if ascending and (row[block]+1 == row[block+1]): # the row is in order
                                # so we don't have to move any of those blocks, which is good for the heuristic
                                h -= self.num_blocks
                            else:
                                ascending = False
                                h += self.num_blocks # we have to move every block above the one out of order plus the one out of order
                elif len(row) > 1: # these blocks are in the wrong row, so at a minimum we have to move one block
                    # we want any row that doesn't have 1 to be in descending order, so we can move all of them onto the correct stack with just 1 move each
                    h += 1
                    desc_sorted = True
                    idx = -1
                    for block in range(len(row)-1):
                        if desc_sorted and (row[block] > row[block+1]):
                            # if the row is in descending order, only a small penalty since we have to make less moves
                            h += 1
                        else:
                            desc_sorted = False
                            if idx < 0:
                                idx = row[block]
                            # now we have to move all of the blocks on top of the one that is out of descending order, so the penalty is higher
                            h += (self.num_blocks - idx) 
        return h           

    def find_possible_moves(self):
        possible_moves = []
        h_vals = []
        for idx, row in enumerate(self.grid):
            if len(row) > 0:
                for row_idx in range(len(self.grid)):
                    state = deepcopy(self.grid)
                    if row_idx != idx:
                        self.move_block(state, idx, row_idx)
                        possible_moves.append(state)
                        h = self.calculate_h(state)
                        h_vals.append(h)
        self.grid = possible_moves[h_vals.index(min(h_vals))]


            
