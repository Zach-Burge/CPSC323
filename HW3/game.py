import enum
import random

class Game:
    def __init__(self, num_blocks):
        self.num_blocks = num_blocks
        self.grid = []
        for i in range(num_blocks):
            self.grid.append([])

    # Method to print the grid
    def show_grid(self):
        for i in range(self.num_blocks):
            print("[ ", end="")
            for j in range(len(self.grid[i])):
                print(self.grid[i][j], end=" ")
            print("]")
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

    # Finds a random value in the "grid" and chooses a new random location in the grid to move the value to
    def move_blocks(self):
        found = False
        while not found:
            rand_loc = random.randrange(self.num_blocks)
            if self.grid[rand_loc] != []:
                found = True
                move_val = self.grid[rand_loc][-1]
                self.grid[rand_loc][-1] = None
        new_rand_loc = random.randrange(self.num_blocks)
        self.grid[new_rand_loc].append(move_val)

    # Main game loop that counts the number of moves taken to solve the game
    def solve(self):
        moves = 0
        while(self.is_solved() == False):
            self.move_blocks()
            moves += 1
        print("Blocks world solved in", moves, "moves!")

            
