from typing import List, Tuple, Set, Dict, Optional
from algorithm.theme_palette import themes, theme_mapper
from algorithm.clear import clear
import random
import time


def ascii_render(width: int, height: int,
                 entry: Tuple[int, int],
                 exit_: Tuple[int, int],
                 maze: List[List[int]],
                 path_coords: Set[Tuple[int, int]]) -> None:

    for y in range(height):

        for x in range(width):

            print("+", end="")

            if maze[y][x] & (1 << 0) or maze[y][x] == 16:
                print("---", end="")
            else:
                print("   ", end="")

        print("+")

        for x in range(width):

            left = (
                "|"
                if (maze[y][x] & (1 << 3) or maze[y][x] == 16)
                else " "
                )
            if (y, x) == entry:
                content = " S "
            elif (y, x) == exit_:
                content = " E "
            elif (y, x) in path_coords:
                content = " P "
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


def emoji_render(width: int, height: int,
                 entry: Tuple[int, int],
                 exit_: Tuple[int, int],
                 maze: List[List[int]],
                 path_coords: Set[Tuple[int, int]],
                 ft_coords: Set[Tuple[int, int]]) -> None:

    for y in range(height):

        print("⬛", end="")

        for x in range(width):

            if (
                maze[y][x] & 1
                or ((y, x) in ft_coords and maze[y - 1][x] != 16)
            ):
                print("⬛⬛", end="")
            else:

                content = "⬛"
                if maze[y][x] == 16:
                    left = "🟦"
                elif (
                    (y, x) in path_coords
                    and (
                        (y > 0 and (y - 1, x) in path_coords)
                        or (y - 1, x) == entry
                    )
                ):
                    left = "🟩"
                else:
                    left = "⬜"

                print(left + content, end="")

        print("")

        for x in range(width):

            if (
                (y, x) in path_coords
                and (
                    x > 0
                    and ((y, x - 1) in path_coords or (y, x - 1) == entry)
                )
                and not maze[y][x] & (1 << 3)
            ):
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


def printer(what_to_print: str, is_end: bool) -> None:
    if is_end:
        print(what_to_print, end="")
    else:
        print(what_to_print)


is_changed: bool = False
previous_color: Dict[str, str] = themes['ash_lava']


def ansi_render(width: int, height: int,
                entry: Tuple[int, int], exit_: Tuple[int, int],
                maze: List[List[int]],
                path_coords: Set[Tuple[int, int]], is_solved: bool,
                is_colored: bool, theme_id: str,
                parents: Dict[Tuple[int, int], Tuple[int, int, int]],
                ft_coords: Set[Tuple[int, int]]) -> None:

    global is_changed
    global previous_color

    if is_colored:

        if theme_id == "8":

            random.seed(time.time())
            random_theme_key = random.choice(list(themes.keys()))
            theme = themes[random_theme_key]
            previous_color = theme
            is_changed = True
            theme_mapper["8"] = random_theme_key

        else:

            theme_mapper_id = theme_mapper.get(theme_id, None)

            theme = themes[theme_mapper_id]
            previous_color = theme
            is_changed = True


    elif not is_colored and is_changed:
        theme = previous_color
    else:
        theme = themes['ash_lava']

    wall_color = theme['wall_color']
    road_color = theme['road_color']
    path_color = theme['path_color']
    entery_color = theme['entery_color']
    exit_color = theme['exit_color']
    ft_pattern = theme['ft_pattern']

    for y in range(height):

        printer(wall_color, True)

        for x in range(width):

            py, px, _ = parents.get((y, x), (0, 0, 0))
            fy, fx, _ = parents.get((y - 1, x), (0, 0, 0))

            if (
                maze[y][x] & 1
                or ((y, x) in ft_coords and maze[y - 1][x] != 16)
            ):
                printer(wall_color + wall_color, True)
            else:
                if maze[y][x] == 16:
                    left = ft_pattern
                elif (
                    (y, x) in path_coords
                    or ((y, x) == entry and (y, x) in path_coords)
                    or ((y, x) == exit_ and (y, x) in path_coords)
                ) and (
                    (
                        y > 0
                        and (
                            (y - 1, x) == (py, px)
                            or (fy, fx) == (y, x)
                        )
                    )
                    or (y - 1, x) == entry
                ) and is_solved:
                    left = path_color
                else:
                    left = road_color

                printer(left + wall_color, True)

        print()

        for x in range(width):

            py, px, _ = parents.get((y, x), (0, 0, 0))
            fy, fx, _ = parents.get((y, x - 1), (0, 0, 0))

            if (
                (
                    (y, x) in path_coords
                    or ((y, x) == entry and (y, x) in path_coords)
                    or ((y, x) == exit_ and (y, x) in path_coords)
                )
                and (
                    (
                        x > 0
                        and (
                            (
                                (
                                    (y, x - 1) == (py, px)
                                    or (fy, fx) == (y, x)
                                )
                                and (y, x - 1) != exit_
                            )
                            or (y, x - 1) == entry
                            or (y, x - 1) == exit_
                        )
                    )
                    or (
                        x < width
                        and (
                            (y, x + 1) == exit_
                            or (y, x + 1) == entry
                        )
                    )
                )
                and not maze[y][x] & (1 << 3)
                and is_solved
            ):
                left = path_color
            elif maze[y][x] == 16 and maze[y][x - 1] == 16:
                left = ft_pattern
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
                content = ft_pattern
            else:
                content = road_color

            printer(left + content, True)

        right = wall_color if maze[y][width - 1] & (1 << 1) else ""
        printer(right, False)

    for x in range(width):

        if maze[height - 1][x] & (1 << 2):
            printer(wall_color + wall_color, True)
        else:
            printer(road_color + road_color, True)

    printer(wall_color, False)


def MazeRenderer(width: int, height: int,
                 entry: Tuple[int, int], exit_: Tuple[int, int],
                 maze: List[List[int]],
                 parents: Dict[Tuple[int, int], Tuple[int, int, int]],
                 is_solved: bool, is_colored: bool, theme_id: str,
                 solve_time: Optional[float],
                 ft_coords: Set[Tuple[int, int]]) -> None:

    path_coords: Set[Tuple[int, int]] = set()
    path_coords_list: List[Tuple[int, int]] = []
    cur = exit_

    while cur in parents:

        py, px, _ = parents[cur]
        path_coords.add(cur)
        if cur not in path_coords_list:
            path_coords_list.append(cur)
        cur = (py, px)

    path_coords.add(entry)
    path_coords_list.reverse()

    # ascii_render(width, height, entry, exit_, maze, path_coords)
    # emoji_render(width, height, entry, exit_, maze, path_coords, is_solved)

    if solve_time:

        animated_path_coords: Set[Tuple[int, int]] = set()
        for i in range(len(path_coords_list)):
            clear()
            animated_path_coords.add(path_coords_list[i])
            ansi_render(width, height, entry, exit_, maze,
                        animated_path_coords, is_solved, is_colored,
                        theme_id, parents, ft_coords)
            if is_solved:
                time.sleep(solve_time)

    else:

        clear()
        ansi_render(width, height, entry, exit_, maze,
                    path_coords, is_solved, is_colored,
                    theme_id, parents, ft_coords)
