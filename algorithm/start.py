import random

class MazeGenerator:

    def __init__(self, width: int, height: int, seed: int | None = None):
        self.width = width
        self.height = height
        self.seed = seed
        self.maze = [[15 for _ in range(width)] for _ in range(height)]
        self.visited = [[False for _ in range(width)] for _ in range(height)]

    def generate(self):

        if self.seed is not None:
            random.seed(self.seed)

        directions = [
            (-1, 0, 1 << 0),  # North
            (0, 1, 1 << 1),   # East
            (1, 0, 1 << 2),   # South
            (0, -1, 1 << 3)   # West
        ]

        opposite = {
            1 << 0: 1 << 2,
            1 << 1: 1 << 3,
            1 << 2: 1 << 0,
            1 << 3: 1 << 1
        }

        x = 0
        y = 0

        self.visited[y][x] = True

        stack = [(x, y)]

        while stack:
            x, y = stack[-1]

            neighbors = []

            for dy, dx, wall in directions:
                ny = y + dy
                nx = x + dx

                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if not self.visited[ny][nx]:
                        neighbors.append((nx, ny, wall))

            if neighbors:
                nx, ny, wall = random.choice(neighbors)

                self.maze[y][x] &= ~wall
                self.maze[ny][nx] &= ~opposite[wall]

                self.visited[ny][nx] = True
                stack.append((nx, ny))

            else:
                stack.pop()


        for i in range(self.width):
            for j in range(self.height):
                print(self.maze[i][j], end=" ")
            print()

p = MazeGenerator(5, 5)
p.generate()