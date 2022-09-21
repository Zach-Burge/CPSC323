import random

class Game:
    def __init__(self, num_blocks):
        self.num_blocks = num_blocks
        self.grid = []
        for i in range(num_blocks):
            self.grid.append([])

    def show_grid(self):
        for i in range(self.num_blocks):
            print("[ ", end="")
            for j in range(len(self.grid[i])):
                print(self.grid[i][j], end=" ")
            print("]")
        print()
        
    def setup_blocks(self):
        for i in range(1, self.num_blocks + 1):
            rand_loc = random.randrange(self.num_blocks)
            self.grid[rand_loc].append(i)
    
    def is_solved(self):
        solved = list(range(1, self.num_blocks + 1))
        for row in self.grid:
            if row == solved:
                return True
        return False

    def move_blocks(self):
        while True:
            rand_loc = random.randrange(self.num_blocks)
            if self.grid[rand_loc]:
                move_val = self.grid[rand_loc].pop()
                break
        new_rand_loc = random.randrange(self.num_blocks)
        self.grid[new_rand_loc].append(move_val)

    def solve(self):
        moves = 0
        while(self.is_solved() == False):
            self.move_blocks()
            moves += 1
        print("Blocks world solved in", moves, "moves!")

            
