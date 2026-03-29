import random
def run(data: dict):
    entry = data["entry"]
    exit_ = data["exit"]

    parents = {}
    path_list = []
    ft_coords = []

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
    if not data["perfect"]:
        maze = p.generate_non_perfect_maze()

    output_file = data["output_file"]
    if data["solve"] == "dfs":
        p.dfs_solve_maze(output_file)
    elif data["solve"] == "bfs":
        p.bfs_solve_maze(output_file)





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
