import os
import time
class GameOfLife:
    def __init__(self, width, height, initial_state=None):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        if initial_state:
            for r, c in initial_state:
                if 0 <= r < height and 0 <= c < width:
                    self.grid[r][c] = 1
    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Grid Size: {self.width}x{self.height}")
        print("+" + "-" * (self.width * 2) + "+")
        for row in self.grid:
            row_str = "|" + "".join(["■ " if cell == 1 else ". " for cell in row]) + "|"
            print(row_str)
        print("+" + "-" * (self.width * 2) + "+")
    def count_neighbors(self, r, c):
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                nr, nc = r + i, c + j
                if 0 <= nr < self.height and 0 <= nc < self.width:
                    neighbors += self.grid[nr][nc]
        return neighbors
    def update_generation(self):
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for r in range(self.height):
            for c in range(self.width):
                live_neighbors = self.count_neighbors(r, c)
                current_state = self.grid[r][c]
                if current_state == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[r][c] = 0
                    else:
                        new_grid[r][c] = 1
                else:
                    if live_neighbors == 3:
                        new_grid[r][c] = 1
                    else:
                        new_grid[r][c] = 0
        self.grid = new_grid
    def run(self, generations=50, delay=0.5):
        for gen in range(generation := generations):
            self.display()
            print(f"Generation: {gen + 1}")
            self.update_generation()
            time.sleep(delay)


# ==========================================
# ا(Blinker / Glider pattern)
# ==========================================
if __name__ == "__main__":
    initial_blinker = [(5, 5), (5, 6), (5, 7)]
    game = GameOfLife(width=15, height=15, initial_state=initial_blinker)
    game.run(generations=20, delay=0.4)