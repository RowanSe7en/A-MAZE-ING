import random

class MazeGenerator: #dfs

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

    def __init__(self, width: int, height: int, seed: int | None = None):

        self.width = width
        self.height = height
        self.seed = seed
        self.maze = [[0xF for _ in range(width)] for _ in range(height)]
        self.visited = [[False for _ in range(width)] for _ in range(height)]

    def generate_maze(self):

        if self.seed is not None:
            random.seed(self.seed)

        y, x = 0, 0
        self.visited[y][x] = True
        stack = [(y, x)]

        i = 1

        while stack:

            y, x = stack[-1]

            neighbors = []

            for dy, dx, wall, dire in MazeGenerator.directions:

                ny = y + dy
                nx = x + dx

                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if not self.visited[ny][nx]:
                        neighbors.append((ny, nx, wall, dire))

            if neighbors:

                ny, nx, wall, dire = random.choice(neighbors)
                # print(i)
                # print(f"ny {ny}, nx {nx}, wall {wall}")
                # print(f"y {y}, x {x}, wall {wall}\n")
                self.maze[y][x] &= ~wall # break the current cell wall
                self.maze[ny][nx] &= ~MazeGenerator.opposite[wall] # break the neibor cell wall

                stack.append((ny, nx))
                self.visited[ny][nx] = True

                i += 1

            else:
                stack.pop()

    def solve_maze(self, output_file):

        entry = (0, 0)
        exit_ = (4, 3)

        en_y, en_x = entry
        ex_y, ex_x = exit_

        visited = [[False for _ in range(width)] for _ in range(height)]

        visited[en_y][en_x] = True
        # print(en_x)
        # print(en_y)

        queue = [entry]
        parents = {}

        while queue:

            # print(queue)
            y, x = queue[0]
            print(f"y {y}, x {x}")
            queue.pop(0)
            # print(queue)

            if (y, x) == exit_:
                break

            for dy, dx, wall, direc in MazeGenerator.directions:

                ny = y + dy
                nx = x + dx
                # print(f"ny {ny}, nx {nx}, {direc}")

                if nx >= 0 and ny >= 0 and nx < width and ny < height:
                    # print("a")
                    if not visited[ny][nx]:
                        # print("b")
                        if not (self.maze[y][x] & wall):
                            # print("c")

                            # print("ttttttttt")
                            visited[ny][nx] = True
                            parents[(ny, nx)] = (y, x, direc)
                            queue.append((ny, nx))
                            # print("------------------")
        
        path_list = [c for _, _, c in parents.values()]
        path_str = "".join(path_list)

        with open(output_file, 'w') as output_maze:
            for row in self.maze:
                output_maze.write("".join(f"{cell:X}" for cell in row))
                output_maze.write("\n")
            output_maze.write(f"\n{en_y}, {en_x}\n")
            output_maze.write(f"{ex_y}, {ex_x}\n")
            output_maze.write(path_str)
            

        

        return path_str


width = 5
height = 5
# seed = 22
seed = 10

p = MazeGenerator(width, height, seed)
p.generate_maze()

output_file = "output_maze.txt"
path = p.solve_maze(output_file)
vis = p.visited


with open(output_file, 'r') as output_maze:
    print(output_maze.read())

# for i in range(0, height):
#     for j in range(0, width):
#         print((maze[i][j]), end=" ")
#     print()
# print()
# print()
# for i in range(0, height):
#     for j in range(0, width):
#         print((vis[i][j]), end=" ")
#     print()




