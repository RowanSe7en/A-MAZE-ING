from algorithm.theme_palette import themes, theme_mapper
import random
import time
import os

def clear():
    os.system("clear")  # linux/mac
    # os.system("cls")  # windows

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
        from algorithm.maze_generator import ft_coords

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


def printer(what_to_print, is_end):
    if is_end:
        print(what_to_print, end="")
    else:
        print(what_to_print)

is_changed = False
previous_color = None

def ansi_render(width, height, entry, exit_, maze, path_coords, is_solved, is_colored, theme_id):
    
    global is_changed
    global previous_color

    if is_colored:

        if theme_id == "7":

            random.seed(time.time())
            random_theme_key = random.choice(list(themes.keys()))
            theme = themes[random_theme_key]
            previous_color = theme
            is_changed = True

        else:

            theme_mapper_id = theme_mapper.get(theme_id, None)

            if theme_mapper_id:

                theme = themes[theme_mapper_id]
                previous_color = theme
                is_changed = True

            else:
                print("Invalid Choise")

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
        printer(wall_color, 1)
        from algorithm.maze_generator import ft_coords

        for x in range(width):
            if maze[y][x] & 1 or ((y, x) in ft_coords and maze[y - 1][x] != 16):
                printer(wall_color + wall_color, 1)
            else:
                if maze[y][x] == 16:
                    left = entery_color
                elif (y, x) in path_coords and (
                    (y > 0 and (y - 1, x) in path_coords) or (y - 1, x) == entry
                ) and is_solved:
                    left = path_color
                else:
                    left = road_color

                printer(left + wall_color, 1)
                
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

            printer(left + content, 1)

        right = wall_color if maze[y][width - 1] & (1 << 1) else ""
        printer(right, 0)

    for x in range(width):
        if maze[height - 1][x] & (1 << 2):
            printer(wall_color + wall_color, 1)
        else:
            printer(road_color + road_color, 1)
    printer(wall_color, 0)


def MazeRenderer(width, height, entry, exit_, maze, parents, is_solved, is_colored, theme_id):

    path_coords = set()
    path_coords_list = []
    cur = exit_

    while cur in parents:

        py, px, _ = parents[cur]
        path_coords.add(cur)
        if cur not in path_coords_list:
            path_coords_list.append(cur)
        cur = (py, px)

    path_coords.add(entry)
    path_coords_list.reverse()

    # ascii_render(width, height, entry, exit_, maze, path_coords, is_solved)
    # emoji_render(width, height, entry, exit_, maze, path_coords, is_solved)

    animated_path_coords = set()
    for i in range(len(path_coords_list)):
        clear()
        animated_path_coords.add(path_coords_list[i])
        ansi_render(width, height, entry, exit_, maze, animated_path_coords, is_solved, is_colored, theme_id)
        time.sleep(0.1)
