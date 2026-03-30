from algorithm.maze_generator import ft_coords
import random
import time

def ascii_render(width, height, entry, exit_, maze, path_coords, is_solved):

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

def emoji_render(width, height, entry, exit_, maze, path_coords, is_solved):

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


themes = {
    "ash_lava":{
        "wall_color":"\033[40m  \033[0m",
        "road_color": "\033[100m  \033[0m",
        "path_color": "\033[103m  \033[0m",
        "entery_color": "\033[101m  \033[0m",
        "exit_color": "\033[105m  \033[0m"
    },
    "forest": {
        "wall_color": "\033[42m  \033[0m",    # dark green trees
        "road_color": "\033[102m  \033[0m",   # bright grass
        "path_color": "\033[100m  \033[0m",   # rocks
        "entery_color": "\033[44m  \033[0m",  # river start
        "exit_color": "\033[46m  \033[0m"     # water glow
    },

    "ice": {
        "wall_color": "\033[107m  \033[0m",   # snow white
        "road_color": "\033[47m  \033[0m",    # light snow
        "path_color": "\033[106m  \033[0m",   # icy blue
        "entery_color": "\033[104m  \033[0m", # cold blue
        "exit_color": "\033[46m  \033[0m"     # cyan exit
    },

    "neon": {
        "wall_color": "\033[45m  \033[0m",    # neon purple
        "road_color": "\033[105m  \033[0m",   # bright magenta
        "path_color": "\033[46m  \033[0m",    # neon cyan
        "entery_color": "\033[102m  \033[0m", # neon green
        "exit_color": "\033[103m  \033[0m"    # neon yellow
    },

    "sunset": {
        "wall_color": "\033[41m  \033[0m",    # red sky
        "road_color": "\033[101m  \033[0m",   # bright red
        "path_color": "\033[43m  \033[0m",    # orange sun
        "entery_color": "\033[103m  \033[0m", # bright orange
        "exit_color": "\033[45m  \033[0m"     # purple dusk
    },

    "matrix": {
        "wall_color": "\033[40m  \033[0m",    # black void
        "road_color": "\033[42m  \033[0m",    # green code
        "path_color": "\033[102m  \033[0m",   # bright green
        "entery_color": "\033[100m  \033[0m", # dark grey
        "exit_color": "\033[47m  \033[0m"     # white portal
    },
}

is_changed = False
previous_color = None

def ansi_render(width, height, entry, exit_, maze, path_coords, is_solved, is_colored):
    
    global is_changed
    global previous_color

    if is_colored:
    
        random.seed(time.time())
        random_theme_key = random.choice(list(themes.keys()))
        theme = themes[random_theme_key]
        previous_color = theme
        is_changed = True

    elif not is_colored and is_changed:
        theme = previous_color
    else:
        theme = themes['ash_lava']

    wall_color   = theme['wall_color']
    road_color   = theme['road_color']
    path_color   = theme['path_color']
    entery_color    = theme['entery_color']
    exit_color = theme['exit_color']

    for y in range(height):
        print(wall_color, end="")

        for x in range(width):
            if maze[y][x] & 1 or ((y, x) in ft_coords and maze[y - 1][x] != 16):
                print(wall_color + wall_color, end="")
            else:
                if maze[y][x] == 16:
                    left = entery_color
                elif (y, x) in path_coords and (
                    (y > 0 and (y - 1, x) in path_coords) or (y - 1, x) == entry
                ) and is_solved:
                    left = path_color
                else:
                    left = road_color

                print(left + wall_color, end="")
                
        print()

        for x in range(width):
            if (
                (y, x) in path_coords
                and (x > 0 and ((y, x - 1) in path_coords or (y, x - 1) == entry))
                and not maze[y][x] & (1 << 3) and is_solved
            ):
                left = path_color
            elif maze[y][x] == 16 and maze[y][x - 1] == 16:
                left = entery_color
            elif maze[y][x] & (1 << 3) or maze[y][x] & (1 << 4):
                left = wall_color
            else:
                left = road_color

            if (y, x) == entry:
                content = entery_color
            elif (y, x) == exit_:
                content = exit_color
            elif (y, x) in path_coords and is_solved:
                content = path_color
            elif maze[y][x] == 16:
                content = entery_color
            else:
                content = road_color

            print(left + content, end="")

        right = wall_color if maze[y][width - 1] & (1 << 1) else ""
        print(right)
        # time.sleep(0.10)

    for x in range(width):
        if maze[height - 1][x] & (1 << 2):
            print(wall_color + wall_color, end="")
        else:
            print(road_color + road_color, end="")
    print(wall_color)


def MazeRenderer(width, height, entry, exit_, maze, parents, is_solved, is_colored):

    path_coords = set()
    cur = exit_

    while cur in parents:

        py, px, _ = parents[cur]
        path_coords.add(cur)
        cur = (py, px)

    path_coords.add(entry)

    # ascii_render(width, height, entry, exit_, maze, path_coords, is_solved)
    # emoji_render(width, height, entry, exit_, maze, path_coords, is_solved)
    ansi_render(width, height, entry, exit_, maze, path_coords, is_solved, is_colored)