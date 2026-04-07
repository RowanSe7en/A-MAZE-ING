from algorithm.theme_palette import themes, theme_mapper
from algorithm.ascii_landing import ascii_landing
from typing import List, Tuple, Dict, Optional
from algorithm.theme_palette import themes
from algorithm.clear import clear
from typing import TypedDict
import random
import time


class MazeData(TypedDict):

    maze: List[List[int]]
    ft_coords: List[Tuple[int, int]]


class MazeGenerator:

    directions: List[Tuple[int, int, int, str]] = [
        (-1, 0, 1 << 0, "N"),
        (0, 1, 1 << 1, "E"),
        (1, 0, 1 << 2, "S"),
        (0, -1, 1 << 3, "W"),
    ]

    opposite: Dict[int, int] = {
        1 << 0: 1 << 2,
        1 << 1: 1 << 3,
        1 << 2: 1 << 0,
        1 << 3: 1 << 1,
    }

    def __init__(
        self,
        width: int,
        height: int,
        seed: Optional[int],
        entry: Tuple[int, int],
        exit_: Tuple[int, int],
        is_ft_printable: bool = True,
    ) -> None:

        self.width: int = width
        self.height: int = height
        self.seed: Optional[int] = seed
        self.entry: Tuple[int, int] = entry
        self.exit_: Tuple[int, int] = exit_
        self.is_ft_printable: bool = is_ft_printable
        self.ft_coords: List[Tuple[int, int]] = []

        self.maze: List[List[int]] = [
            [0xF for _ in range(self.width)]
            for _ in range(self.height)
        ]

        self.visited: List[List[bool]] = [
            [False for _ in range(self.width)]
            for _ in range(self.height)
        ]

    def where_is_42(self) -> None:

        ft_y = int((self.height / 2) - 2.5)
        ft_x = int((self.width / 2) - 3.5)

        ft_y -= 1
        for _ in range(3):
            ft_y += 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1
            self.ft_coords.append((ft_y, ft_x))

        for _ in range(2):
            ft_x += 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1
            self.ft_coords.append((ft_y, ft_x))

        for _ in range(2):
            ft_y -= 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1
            self.ft_coords.append((ft_y, ft_x))

        ft_y += 2
        for _ in range(2):
            ft_y += 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1
            self.ft_coords.append((ft_y, ft_x))

        ft_x += 5

        for _ in range(3):
            ft_x -= 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1
            self.ft_coords.append((ft_y, ft_x))

        for _ in range(2):
            ft_y -= 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1
            self.ft_coords.append((ft_y, ft_x))

        for _ in range(2):
            ft_x += 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1
            self.ft_coords.append((ft_y, ft_x))

        for _ in range(2):
            ft_y -= 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1
            self.ft_coords.append((ft_y, ft_x))

        for _ in range(2):
            ft_x -= 1
            self.visited[ft_y][ft_x] = True
            self.maze[ft_y][ft_x] += 1
            self.ft_coords.append((ft_y, ft_x))

    def maze_render(self, theme_id: Optional[str] = None) -> None:

        theme_mapper_id = theme_mapper.get(theme_id, None)
        theme = themes[theme_mapper_id]

        wall_color = theme['wall_color']
        road_color = theme['road_color']
        path_color = theme['path_color']
        entery_color = theme['entery_color']
        exit_color = theme['exit_color']
        ft_pattern = theme['ft_pattern']

        for y in range(self.height):
            print(wall_color, end="")

            for x in range(self.width):
                if (
                    self.maze[y][x] & 1
                    or (
                        (y, x) in self.ft_coords
                        and self.maze[y - 1][x] != 16
                    )
                ):
                    print(wall_color + wall_color, end="")
                else:
                    left = ft_pattern if self.maze[y][x] == 16 else road_color
                    print(left + wall_color, end="")

            print()

            for x in range(self.width):

                if self.maze[y][x] == 16 and self.maze[y][x - 1] == 16:
                    left = ft_pattern
                elif (
                    self.maze[y][x] & (1 << 3)
                    or self.maze[y][x] & (1 << 4)
                ):
                    left = wall_color
                else:
                    left = road_color

                if (y, x) == self.entry:
                    content = entery_color
                elif (y, x) == self.exit_:
                    content = exit_color
                elif self.maze[y][x] == 16:
                    content = ft_pattern
                else:
                    content = road_color

                print(left + content, end="")

            right = (
                wall_color
                if self.maze[y][self.width - 1] & (1 << 1)
                else ""
            )
            print(right)

        for x in range(self.width):
            if self.maze[self.height - 1][x] & (1 << 2):
                print(wall_color + wall_color, end="")
            else:
                print(road_color + road_color, end="")
        print(wall_color)

    def generate_perfect_maze(
        self,
        generator_time: float,
        is_perfect: bool,
        theme_id: Optional[str] = None
    ) -> List[List[int]]:

        if self.seed is not None:
            random.seed(self.seed)

        y, x = 0, 0
        self.visited[y][x] = True
        stack: List[Tuple[int, int]] = [(y, x)]

        while stack:
            y, x = stack[-1]
            neighbors: List[Tuple[int, int, int, str]] = []

            for dy, dx, wall, dire in MazeGenerator.directions:
                ny = y + dy
                nx = x + dx

                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if not self.visited[ny][nx] and self.maze[ny][nx] != 16:
                        neighbors.append((ny, nx, wall, dire))

            if neighbors:
                ny, nx, wall, dire = random.choice(neighbors)

                self.maze[y][x] &= ~wall
                self.maze[ny][nx] &= ~MazeGenerator.opposite[wall]

                stack.append((ny, nx))
                self.visited[ny][nx] = True

                if generator_time:
                    clear(self.is_ft_printable)
                    self.maze_render(theme_id)
                    time.sleep(generator_time)
            else:
                stack.pop()

        if not generator_time and not is_perfect:
            clear(self.is_ft_printable)
            self.maze_render(theme_id)

        return self.maze

    def generate_non_perfect_maze(
        self,
        generator_time: float,
        theme_id: Optional[str] = None
    ) -> List[List[int]]:

        if self.seed is not None:
            random.seed(self.seed + 1)

        y, x = self.exit_
        randomizer = [True]
        non_perfect_visited: List[List[bool]] = [
            [False for _ in range(self.width)]
            for _ in range(self.height)
        ]

        non_perfect_visited[y][x] = True
        stack: List[Tuple[int, int]] = [(y, x)]

        while stack:
            y, x = stack[-1]
            neighbors: List[Tuple[int, int, int, str]] = []

            for dy, dx, wall, dire in MazeGenerator.directions:
                ny = y + dy
                nx = x + dx

                if 0 <= nx < self.width and 0 <= ny < self.height:
                    random_choice = random.choice(randomizer)
                    if (
                        not non_perfect_visited[ny][nx]
                        and random_choice
                        and self.maze[ny][nx] != 16
                    ):
                        neighbors.append((ny, nx, wall, dire))

            if neighbors:

                ny, nx, wall, dire = random.choice(neighbors)

                cells_with_one_wall_only = [1, 2, 4, 8]
                cells_with_two_walls_only = [3, 5, 6, 9, 10, 12]

                cell_value = self.maze[y][x]
                is_inner_cell = (0 < y < self.height - 1 and
                                 0 < x < self.width - 1)
                is_edge_cell = (0 <= y <= self.height - 1 and
                                0 < x < self.width - 1)

                safe_inner = (is_inner_cell and
                              cell_value not in cells_with_one_wall_only)
                safe_edge = (
                    is_edge_cell
                    and cell_value not in cells_with_two_walls_only
                    and cell_value not in cells_with_one_wall_only
                )

                if safe_inner or safe_edge:

                    empty = 0

                    for i in range(1, 4):

                        if wall in (1, 4):

                            if (x + i < self.width and
                                    not (self.maze[y][x + i] & wall)):
                                empty += 1

                            if (x - i >= 0 and
                                    not (self.maze[y][x - i] & wall)):
                                empty += 1

                        elif wall in (2, 8):

                            if (y + i < self.height and
                                    not (self.maze[y + i][x] & wall)):
                                empty += 1

                            if (y - i >= 0 and
                                    not (self.maze[y - i][x] & wall)):
                                empty += 1

                    if empty < 3:

                        self.maze[y][x] &= ~wall
                        self.maze[ny][nx] &= ~MazeGenerator.opposite[wall]

                stack.append((ny, nx))
                non_perfect_visited[ny][nx] = True

                if generator_time:
                    clear(self.is_ft_printable)
                    self.maze_render(theme_id)
                    time.sleep(generator_time)
            else:
                stack.pop()

        if not generator_time:
            clear(self.is_ft_printable)
            self.maze_render(theme_id)

        return self.maze


def generator_entery(
    width: int,
    height: int,
    seed: Optional[int],
    entry: Tuple[int, int],
    exit_: Tuple[int, int],
    is_perfect: bool,
    generator_time: float,
    is_ft_printable: bool,
    theme_id: Optional[str] = None
) -> MazeData:

    maze_gen = MazeGenerator(
        width,
        height,
        seed,
        entry,
        exit_,
        is_ft_printable,
    )

    if is_ft_printable:
        maze_gen.where_is_42()

    for cord in maze_gen.ft_coords:

        if cord == entry:

            ascii_landing()
            print(
                "The entery is placed inside of the 42 pattern, "
                "please enter another cords"
            )
            exit(0)

        elif cord == exit_:

            ascii_landing()
            print(
                "The exit is placed inside of the 42 pattern, "
                "please enter another cords"
            )
            exit(0)

    maze = maze_gen.generate_perfect_maze(generator_time, is_perfect, theme_id)

    if not is_perfect:
        maze = maze_gen.generate_non_perfect_maze(generator_time, theme_id)

    return {"maze": maze, "ft_coords": maze_gen.ft_coords}
