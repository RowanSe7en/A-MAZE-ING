import time
import random
import algorithm
from typing import List, Tuple, Dict, Optional


class MazeGenerator:
    """
    Maze generation class supporting perfect and non-perfect mazes.

    Each cell in the maze uses a bitmask to represent walls in the four
    cardinal directions (N, E, S, W). The class allows real-time rendering
    with a theme and can optionally seed randomness for reproducible mazes.
    """
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
        """
        Initialize the MazeGenerator.

        Parameters
        ----------
        width : int
            Width of the maze in cells.
        height : int
            Height of the maze in cells.
        seed : Optional[int]
            Random seed for reproducibility.
        entry : Tuple[int,int]
            Starting cell coordinates (row, col).
        exit_ : Tuple[int,int]
            Exit cell coordinates (row, col).
        is_ft_printable : bool
            Whether to allow printing the maze in real-time.
        """
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
        """
        Mark a special pattern ("42") in the middle of the maze.

        This sets certain cells as visited and changes their values
        to a special marker (16) to prevent the generator from
        modifying them.
        """
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
        """
        Render the maze to the terminal using ANSI colors.

        Parameters
        ----------
        theme_id : Optional[str]
            ID of the theme to apply. Falls back to 'ash_lava' if invalid.
        """
        if theme_id is None:
            theme_id = '1'   # or your default theme id

        theme_mapper_id = algorithm.theme_mapper.get(theme_id)

        if theme_mapper_id is None:
            theme_mapper_id = 'ash_lava'  # fallback only for typing safety

        theme = algorithm.themes[theme_mapper_id]

        wall_color = theme['wall_color']
        road_color = theme['road_color']
        # path_color = theme['path_color']
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
        """
        Generate a perfect maze using DFS backtracking.

        Perfect maze: exactly one path exists between any two cells.

        Parameters
        ----------
        generator_time : float
            Time delay in seconds for visualization.
        is_perfect : bool
            Whether to render the final maze.
        theme_id : Optional[str]
            Theme ID for rendering.

        Returns
        -------
        List[List[int]]
            Generated maze with walls removed.
        """
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
                    algorithm.clear(self.is_ft_printable)
                    self.maze_render(theme_id)
                    time.sleep(generator_time)
            else:
                stack.pop()

        if not generator_time and is_perfect:
            algorithm.clear(self.is_ft_printable)
            self.maze_render(theme_id)

        return self.maze

    def generate_non_perfect_maze(
        self,
        generator_time: float,
        theme_id: Optional[str] = None
    ) -> List[List[int]]:
        """
        Generate a non-perfect maze by selectively removing walls.

        Non-perfect maze: may contain loops, multiple paths between cells.

        Parameters
        ----------
        generator_time : float
            Time delay in seconds for visualization.
        theme_id : Optional[str]
            Theme ID for rendering.

        Returns
        -------
        List[List[int]]
            Generated maze allowing loops.
        """
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

                    for i in range(1, 3):

                        if wall in (1, 3):

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

                    if empty < 2:

                        self.maze[y][x] &= ~wall
                        self.maze[ny][nx] &= ~MazeGenerator.opposite[wall]

                stack.append((ny, nx))
                non_perfect_visited[ny][nx] = True

                if generator_time:
                    algorithm.clear(self.is_ft_printable)
                    self.maze_render(theme_id)
                    time.sleep(generator_time)

            else:
                stack.pop()

        if not generator_time:
            algorithm.clear(self.is_ft_printable)
            self.maze_render(theme_id)

        return self.maze
