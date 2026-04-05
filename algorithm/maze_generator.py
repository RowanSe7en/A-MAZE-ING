from algorithm.theme_palette import themes
from algorithm.clear import clear
from algorithm.ascii_landing import ascii_landing
import random
import time

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

    def __init__(self, width, height, seed, entry, exit_, is_ft_printable=True):

        self.width = width
        self.height = height
        self.seed = seed
        self.entry = entry
        self.exit_ = exit_
        self.is_ft_printable = is_ft_printable

        self.maze = [
            [0xF for _ in range(self.width)]
            for _ in range(self.height)
            ]

        self.visited = [
            [False for _ in range(self.width)]
            for _ in range(self.height)
            ]

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

    def maze_render(self):

        theme = themes['ash_lava']
        wall_color = theme['wall_color']
        road_color = theme['road_color']
        entery_color = theme['entery_color']
        exit_color = theme['exit_color']
        ft_pattern = theme['ft_pattern']

        for y in range(self.height):
            print(wall_color, end="")

            for x in range(self.width):
                if (
                    self.maze[y][x] & 1
                    or (
                        (y, x) in ft_coords
                        and self.maze[y - 1][x] != 16
                    )
                ):
                    print(wall_color + wall_color, end="")
                else:
                    if self.maze[y][x] == 16:
                        left = ft_pattern
                    else:
                        left = road_color

                    print(left + wall_color, end="")

            print()

            for x in range(self.width):

                if self.maze[y][x] == 16 and self.maze[y][x - 1] == 16:
                    left = ft_pattern
                elif self.maze[y][x] & (1 << 3) or self.maze[y][x] & (1 << 4):
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

            right = right = (
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

    def generate_perfect_maze(self, generator_time, is_perfect):

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

                self.maze[y][x] &= ~wall
                self.maze[ny][nx] &= ~MazeGenerator.opposite[wall]

                stack.append((ny, nx))
                self.visited[ny][nx] = True

                if generator_time:
                    clear(self.is_ft_printable)
                    self.maze_render()
                    time.sleep(generator_time)

            else:
                stack.pop()

        if not generator_time and is_perfect:
            clear(self.is_ft_printable)
            self.maze_render()

        return self.maze

    def generate_non_perfect_maze(self, generator_time):

        if self.seed is not None:
            random.seed(self.seed + 1)

        y, x = self.exit_
        randomizer = [False, True]
        non_perfect_visited = [
            [False for _ in range(self.width)]
            for _ in range(self.height)
            ]
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
                    if (
                        not non_perfect_visited[ny][nx]
                        and random_choice
                        and self.maze[ny][nx] != 16
                    ):
                        neighbors.append((ny, nx, wall, dire))

            if neighbors:

                ny, nx, wall, dire = random.choice(neighbors)

                self.maze[y][x] &= ~wall
                self.maze[ny][nx] &= ~MazeGenerator.opposite[wall]

                stack.append((ny, nx))
                non_perfect_visited[ny][nx] = True

                if generator_time:
                    clear(self.is_ft_printable)
                    self.maze_render()
                    time.sleep(generator_time)

            else:
                stack.pop()

        if not generator_time:
            clear(self.is_ft_printable)
            self.maze_render()

        return self.maze


def generator_entery(width, height, seed, entry,
                     exit_, is_perfect, generator_time, is_ft_printable):

    maze_gen = MazeGenerator(width, height, seed, entry, exit_, is_ft_printable)

    if is_ft_printable:
        maze_gen.where_is_42()

    for cord in ft_coords:
        if cord == entry:
            ascii_landing()
            print(
                "The entery is placed inside of the 42 pattern,"
                " please enter another cords"
                )
            exit(1)
        elif cord == exit_:
            ascii_landing()
            print(
                "The exit is placed inside of the 42 pattern,"
                " please enter another cords"
                )
            exit(1)

    maze = maze_gen.generate_perfect_maze(generator_time, is_perfect)

    if not is_perfect:
        maze = maze_gen.generate_non_perfect_maze(generator_time)

    return maze
