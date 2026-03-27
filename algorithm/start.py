import random
def run(data: dict):
    entry = data["entry"]
    exit_ = data["exit"]

    parents = {}
    path_list = []
    ft_coords = []

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

        def __init__(self):

            self.width = data["width"]
            self.height = data["height"]
            self.seed = data["seed"]
            self.maze = [[0xF for _ in range(self.width)] for _ in range(self.height)]
            self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]

        def where_is_42(self):
            
            ft_y = int((self.height / 2) - 2.5)
            ft_x = int((self.width / 2) - 3.5)

            # 4
            ft_y -= 1
            for _ in range(3):
                ft_y += 1
                self.visited[ft_y][ft_x] = True
                self.maze[ft_y][ft_x] += 1
                ft_coords.append((ft_y, ft_x))

            for _ in range(2):
                ft_x += 1
                self.visited[ft_y][ft_x] = True
                self.maze[ft_y][ft_x] += 1
                ft_coords.append((ft_y, ft_x))

            for _ in range(2):
                ft_y -= 1
                self.visited[ft_y][ft_x] = True
                self.maze[ft_y][ft_x] += 1
                ft_coords.append((ft_y, ft_x))

            ft_y += 2
            for _ in range(2):
                ft_y += 1
                self.visited[ft_y][ft_x] = True
                self.maze[ft_y][ft_x] += 1
                ft_coords.append((ft_y, ft_x))

            # 2
            ft_x += 5
            
            for _ in range(3):
                ft_x -= 1
                self.visited[ft_y][ft_x] = True
                self.maze[ft_y][ft_x] += 1
                ft_coords.append((ft_y, ft_x))

            for _ in range(2):
                ft_y -= 1
                self.visited[ft_y][ft_x] = True
                self.maze[ft_y][ft_x] += 1
                ft_coords.append((ft_y, ft_x))

            for _ in range(2):
                ft_x += 1
                self.visited[ft_y][ft_x] = True
                self.maze[ft_y][ft_x] += 1
                ft_coords.append((ft_y, ft_x))

            for _ in range(2):
                ft_y -= 1
                self.visited[ft_y][ft_x] = True
                self.maze[ft_y][ft_x] += 1
                ft_coords.append((ft_y, ft_x))

            for _ in range(2):
                ft_x -= 1
                self.visited[ft_y][ft_x] = True
                self.maze[ft_y][ft_x] += 1
                ft_coords.append((ft_y, ft_x))

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
                random.seed(self.seed + 1)

            y, x = exit_
            randomizer = [0, 1]
            non_perfect_visited = [[False for _ in range(self.width)] for _ in range(self.height)]
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

            visited = [[False for _ in range(self.width)] for _ in range(self.height)]
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

                    if nx >= 0 and ny >= 0 and nx < self.width and ny < self.height:

                        if not visited[ny][nx]:

                            if not (self.maze[y][x] & wall):

                                visited[ny][nx] = True
                                parents[(ny, nx)] = (y, x, direc)
                                queue.append((ny, nx))

            nonlocal path_list

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

            visited = [[False for _ in range(self.width)] for _ in range(self.height)]
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

                    if nx >= 0 and ny >= 0 and nx < self.width and ny < self.height:

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

            nonlocal path_list

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




    p = MazeGenerator()
    p.where_is_42()
    maze = p.generate_perfect_maze()
    # if not data["perfect"]:
    maze = p.generate_non_perfect_maze()

    output_file = data["output_file"]
    if data["solve"] == "dfs":
        path = p.dfs_solve_maze(output_file)
    elif data["solve"] == "bfs":
        path = p.bfs_solve_maze(output_file)

    path_coords = []

    for cell in parents.values():
        y, x, d = cell
        path_coords.append((y, x))

    def ascii_render(width, height):

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

    # ascii_render(data["width"], data["height"])

    def emoji_render(width, height):
        path_coords = set()
        cur = exit_

        while cur in parents:
            py, px, _ = parents[cur]
            path_coords.add(cur)
            cur = (py, px)

        path_coords.add(entry)

        for y in range(height):
            print("⬛", end="")

            for x in range(width):
                if maze[y][x] & 1 or ((y, x) in ft_coords and maze[y - 1][x] != 16):
                    print("⬛⬛", end="")
                else:
                    content = "⬛"
                    if maze[y][x] == 16:
                        left = "🟦"
                    elif (y, x) in path_coords and ((y > 0 and (y - 1, x) in path_coords) or (y - 1, x) == entry):
                        left = "🟩"
                    else:
                        left = "⬜"

                    print(left + content, end="")
            print("")

            for x in range(width):
                if (y, x) in path_coords and (x > 0 and (y, x - 1) in path_coords or (y, x - 1) == entry) and not maze[y][x] & 1 << 3:
                    left = "🟩"
                elif maze[y][x] == 16 and maze[y][x - 1] == 16:
                    left = "🟦"
                elif maze[y][x] & 1 << 3 or maze[y][x] & 1 << 4:
                    left = "⬛"
                else:
                    left = "⬜"

                if (y, x) == entry:
                    content = "🟦"
                elif (y, x) == exit_:
                    content = "🟪"
                elif (y, x) in path_coords:
                    content = "🟩"
                elif maze[y][x] == 16:
                    content = "🟦"
                else:
                    content = "⬜"

                print(left + content, end="")

            right = "⬛" if maze[y][width - 1] & (1 << 1) else ""
            print(right)

        for x in range(width):
            if maze[height - 1][x] & (1 << 2):
                print("⬛⬛", end="")
            else:
                print("⬜⬜", end="")
        print("⬛")


    # emoji_render(data["width"], data["height"])

    def ansi_render(width, height):

        BLACK   = "\033[40m  \033[0m"   # walls
        WHITE   = "\033[100m  \033[0m"  # floor (dark gray)
        GREEN   = "\033[103m  \033[0m"  # path (yellow = lava glow)
        BLUE    = "\033[101m  \033[0m"  # visited (red heat)
        MAGENTA = "\033[105m  \033[0m"  # exit (pink/purple core)

        path_coords = set()
        cur = exit_

        while cur in parents:
            py, px, _ = parents[cur]
            path_coords.add(cur)
            cur = (py, px)

        path_coords.add(entry)

        for y in range(height):
            print(BLACK, end="")

            for x in range(width):
                if maze[y][x] & 1 or ((y, x) in ft_coords and maze[y - 1][x] != 16):
                    print(BLACK + BLACK, end="")
                else:
                    if maze[y][x] == 16:
                        left = BLUE
                    elif (y, x) in path_coords and (
                        (y > 0 and (y - 1, x) in path_coords) or (y - 1, x) == entry
                    ):
                        left = GREEN
                    else:
                        left = WHITE

                    print(left + BLACK, end="")
            print()

            for x in range(width):
                if (
                    (y, x) in path_coords
                    and (x > 0 and ((y, x - 1) in path_coords or (y, x - 1) == entry))
                    and not maze[y][x] & (1 << 3)
                ):
                    left = GREEN
                elif maze[y][x] == 16 and maze[y][x - 1] == 16:
                    left = BLUE
                elif maze[y][x] & (1 << 3) or maze[y][x] & (1 << 4):
                    left = BLACK
                else:
                    left = WHITE

                if (y, x) == entry:
                    content = BLUE
                elif (y, x) == exit_:
                    content = MAGENTA
                elif (y, x) in path_coords:
                    content = GREEN
                elif maze[y][x] == 16:
                    content = BLUE
                else:
                    content = WHITE

                print(left + content, end="")

            right = BLACK if maze[y][width - 1] & (1 << 1) else ""
            print(right)

        for x in range(width):
            if maze[height - 1][x] & (1 << 2):
                print(BLACK + BLACK, end="")
            else:
                print(WHITE + WHITE, end="")
        print(BLACK)

    ansi_render(data["width"], data["height"])
