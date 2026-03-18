import random

entry = (0, 0)
exit_ = (1, 2)

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

    def where_is_42(self):
        
        ft_y = int((height / 2) - 2.5)
        ft_x = int((width / 2) - 3.5)

        # 4
        ft_y -= 1
        for i in range(3):
            ft_y += 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1

        for i in range(2):
            ft_x += 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1

        for i in range(2):
            ft_y -= 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1

        ft_y += 2
        for i in range(2):
            ft_y += 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1

        # 2
        ft_x += 5
        
        for i in range(3):
            ft_x -= 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1

        for i in range(2):
            ft_y -= 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1

        for i in range(2):
            ft_x += 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1

        for i in range(2):
            ft_y -= 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1

        for i in range(2):
            ft_x -= 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1

    def generate_perfect_maze(self): #dfs

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
                    if not self.visited[ny][nx] and self.maze[ny][nx] != 16:
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

    def generate_non_perfect_maze(self): #dfs

        if self.seed is not None:
            random.seed(self.seed)

        y, x = exit_
        randomizer = [0, 1]
        non_perfect_visited = [[False for _ in range(width)] for _ in range(height)]
        non_perfect_visited[y][x] = True
        stack = [(y, x)]

        while stack:

            y, x = stack[-1]

            neighbors = []

            for dy, dx, wall, dire in MazeGenerator.directions:

                ny = y + dy
                nx = x + dx

                if 0 <= nx < self.width and 0 <= ny < self.height:
                    random_choice = random.choice(randomizer)
                    if not non_perfect_visited[ny][nx] and random_choice and self.maze[ny][nx] != 16:
                        neighbors.append((ny, nx, wall, dire))

            if neighbors:

                ny, nx, wall, dire = random.choice(neighbors)

                self.maze[y][x] &= ~wall # break the current cell wall
                self.maze[ny][nx] &= ~MazeGenerator.opposite[wall] # break the neibor cell wall

                stack.append((ny, nx))
                non_perfect_visited[ny][nx] = True

            else:
                stack.pop()
            
        return self.maze

    def bfs_solve_maze(self, output_file): #bfs

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

    def dfs_solve_maze(self, output_file): #dfs

        en_y, en_x = entry
        ex_y, ex_x = exit_

        visited = [[False for _ in range(width)] for _ in range(height)]
        visited[en_y][en_x] = True

        queue = [entry]

        while queue:

            y, x = queue[-1]

            neighbors = []


            if (y, x) == exit_:
                break

            for dy, dx, wall, direc in MazeGenerator.directions:

                ny = y + dy
                nx = x + dx

                if nx >= 0 and ny >= 0 and nx < width and ny < height:

                    if not visited[ny][nx]:

                        if not (self.maze[y][x] & wall):

                          neighbors.append((ny, nx, wall, direc))

            if neighbors:

                random_true = random.Random()
                ny, nx, wall, direc = random_true.choice(neighbors)

                visited[ny][nx] = True
                parents[(ny, nx)] = (y, x, direc)
                queue.append((ny, nx))

            else:
                queue.pop()

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


width = 9
height = 7
# seed = 22
seed = 10

p = MazeGenerator(width, height)
p.where_is_42()
maze = p.generate_perfect_maze()
# maze = p.generate_non_perfect_maze()

output_file = "output_maze.txt"
path = p.dfs_solve_maze(output_file)

path_coords = []

for cell in parents.values():
    y, x, d = cell
    path_coords.append((y, x))

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

            if maze[y][x] & (1 << 0) or maze[y][x] == 16: 
                print("---", end="")
            else:
                print("   ", end="")

        print("+") 

        for x in range(width):

            left = "|" if (maze[y][x] & (1 << 3) or maze[y][x] == 16) else " "  # West wall
            if (y, x) == entry:
                content = " S "
            elif (y, x) == exit_:
                content = " E "
            elif (y, x) in path_coords:
                content = " . "
            elif maze[y][x] == 16:
                content = " # "
            else:
                content = "   "
            print(left + content, end="")

        right = "|" if maze[y][width - 1] & (1 << 1) else " "
        print(right)

    for x in range(width):
        print("+---", end="")

    print("+")

ascii_render()

def emoji_render():
    path_coords = set()
    cur = exit_

    while cur in parents:
        py, px, _ = parents[cur]
        path_coords.add(cur)
        cur = (py, px)

    path_coords.add(entry)

    for y in range(height):

        for x in range(width):
            print("🧱", end="")
            if maze[y][x] & (1 << 0):
                print("🧱" * 2, end="")
            else:
                print("⬜" * 2, end="")
        print("🧱")

        for x in range(width):
            left = "🧱" if maze[y][x] & (1 << 3) else "⬜"

            if (y, x) == entry:
                content = "🏂" + "⬜"
            elif (y, x) == exit_:
                content = "🚗" + "⬜"
            elif (y, x) in path_coords:
                content = "🔳" * 2
            else:
                content = "⬜" * 2

            print(left + content, end="")

        right = "🧱" if maze[y][width - 1] & (1 << 1) else "⬜"
        print(right)

    for x in range(width):
        print("🧱", end="")
        if maze[height - 1][x] & (1 << 2):
            print("🧱" * 2, end="")
        else:
            print("⬜" * 2, end="")
    print("🧱")


# emoji_render()