from algorithm.maze_generator import ft_coords

def ascii_render(width, height, entry, exit_, maze, path_coords):

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

def emoji_render(width, height, entry, exit_, maze, path_coords):

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


def ansi_render(width, height, entry, exit_, maze, path_coords):

    BLACK   = "\033[40m  \033[0m"   # walls
    WHITE   = "\033[100m  \033[0m"  # floor (dark gray)
    GREEN   = "\033[103m  \033[0m"  # path (yellow = lava glow)
    BLUE    = "\033[101m  \033[0m"  # visited (red heat)
    MAGENTA = "\033[105m  \033[0m"  # exit (pink/purple core)

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


def MazeRenderer(width, height, entry, exit_, maze, parents):

    path_coords = set()
    cur = exit_

    while cur in parents:

        py, px, _ = parents[cur]
        path_coords.add(cur)
        cur = (py, px)

    path_coords.add(entry)

    # ascii_render(width, height, entry, exit_, maze, path_coords)
    # emoji_render(width, height, entry, exit_, maze, path_coords)
    ansi_render(width, height, entry, exit_, maze, path_coords)