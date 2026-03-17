import random

entry = (0, 0)
exit_ = (14, 13)

parents = {}
path_list = []

class MazeGenerator:

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

    def generate_maze(self): #dfs

        if self.seed is not None:
            random.seed(self.seed)

        y, x = 0, 0
        self.visited[y][x] = True
        stack = [(y, x)]

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

                self.maze[y][x] &= ~wall # break the current cell wall
                self.maze[ny][nx] &= ~MazeGenerator.opposite[wall] # break the neibor cell wall

                stack.append((ny, nx))
                self.visited[ny][nx] = True

            else:
                stack.pop()
            
        return self.maze

    def solve_maze(self, output_file): #bfs

        en_y, en_x = entry
        ex_y, ex_x = exit_

        visited = [[False for _ in range(width)] for _ in range(height)]
        visited[en_y][en_x] = True

        queue = [entry]

        while queue:

            y, x = queue[0]
            queue.pop(0)

            if (y, x) == exit_:
                break

            for dy, dx, wall, direc in MazeGenerator.directions:

                ny = y + dy
                nx = x + dx

                if nx >= 0 and ny >= 0 and nx < width and ny < height:

                    if not visited[ny][nx]:

                        if not (self.maze[y][x] & wall):

                            visited[ny][nx] = True
                            parents[(ny, nx)] = (y, x, direc)
                            queue.append((ny, nx))

        global path_list

        current = exit_

        while current != entry:

            py, px, direction = parents[current]
            path_list.append(direction)
            current = (py, px)

        path_list.reverse()
        path_str = "".join(path_list)

        with open(output_file, 'w') as output_maze:

            for row in self.maze:

                output_maze.write("".join(f"{cell:X}" for cell in row))
                output_maze.write("\n")

            output_maze.write(f"\n{en_y}, {en_x}\n")
            output_maze.write(f"{ex_y}, {ex_x}\n")
            output_maze.write(path_str)

        return path_str


width = 15
height = 15
# seed = 22
seed = 10

p = MazeGenerator(width, height, seed)
maze = p.generate_maze()

output_file = "output_maze.txt"
path = p.solve_maze(output_file)
vis = p.visited


# with open(output_file, 'r') as output_maze:
#     print(output_maze.read())

# for i in range(0, height):
#     for j in range(0, width):
#         print(f"{maze[i][j]:b}", end=" ")
#     print()
# print()
# print()
# for i in range(0, height):
#     for j in range(0, width):
#         print((vis[i][j]), end=" ")
#     print()

# print(parents)

path_coords = []

for cell in parents.values():

    y, x, d = cell
    path_coords.append((y, x))

print(path_list)


def ascii_render():

    path_coords = set()
    cur = exit_

    while cur in parents:

        py, px, _ = parents[cur]
        path_coords.add(cur)
        cur = (py, px)

    path_coords.add(entry)

    for y in range(height):

        for x in range(width):

            print("+", end="")

            if maze[y][x] & (1 << 0): 
                print("---", end="")
            else:
                print("   ", end="")

        print("+") 

        for x in range(width):

            left = "|" if maze[y][x] & (1 << 3) else " "  # West wall
            if (y, x) == entry:
                content = " S "
            elif (y, x) == exit_:
                content = " E "
            elif (y, x) in path_coords:
                content = " . "
            else:
                content = "   "
            print(left + content, end="")

        # Rightmost east wall
        right = "|" if maze[y][width - 1] & (1 << 1) else " "
        print(right)

    for x in range(width):
        print("+---", end="")

    print("+")

ascii_render()
