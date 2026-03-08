import random

class MazeGenerator:

    def __init__(self, width: int, height: int, seed: int | None = None):
        self.width = width
        self.height = height
        self.seed = seed
        self.maze = [[0xF for _ in range(width)] for _ in range(height)]
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

        stack = [(y, x)]

        while stack:
            x, y = stack[-1]

            neighbors = []

            for dy, dx, wall in directions:
                ny = y + dy
                nx = x + dx

                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if not self.visited[ny][nx]:
                        neighbors.append((ny, nx, wall))

            if neighbors:
                ny, nx, wall = random.choice(neighbors)

                self.maze[y][x] &= ~wall
                self.maze[ny][nx] &= ~opposite[wall]

                self.visited[ny][nx] = True
                stack.append((ny, nx))

            else:
                stack.pop()

        return self.maze

width = 9
height = 5

p = MazeGenerator(width, height)
maze = p.generate()

for i in range(0, height):
    for j in range(0, width):
        print((maze[i][j]), end=" ")
    print()

def bfs():

    directions = [
        (-1, 0, 1 << 0, "N"),  # North
        (0, 1, 1 << 1, "E"),   # East
        (1, 0, 1 << 2, "S"),   # South
        (0, -1, 1 << 3, "W")   # West
    ]

    opposite = {
        1 << 0: 1 << 2,
        1 << 1: 1 << 3,
        1 << 2: 1 << 0,
        1 << 3: 1 << 1
    }

    entry = (0, 0)
    exit_ = (2, 3)
    en_y, en_x = entry
    ex_y, ex_x = exit_

    visited = [[False for _ in range(width)] for _ in range(height)]

    visited[en_y][en_x] = True
    # print(en_x)
    # print(en_y)

    queue = [entry]
    parent = {}

    while queue:
        
        y, x = queue[0]
        # print(y)
        # print(x)
        queue.pop(0)
        

        if (y, x) == exit_:
            print(x)
            print(y)
            break

        for dy, dx, wall, direc in directions:
            ny = y + dy
            nx = x + dx
            # print(f"ny {ny}")
            # print(f"nx {nx}")

            if nx >= 0 and ny >= 0 and nx <= width and ny <= height:
                if not visited[ny][nx]:
                    if not (maze[y][x] & wall):
                        # print("ttttttttt")
                        visited[ny][nx] = True
                        parent[(ny, nx)] = (y, x, direc)
                        queue.append((ny, nx))

        # print("hw")
    print(x)
    print(y)





bfs()