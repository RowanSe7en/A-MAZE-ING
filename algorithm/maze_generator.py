import random

parents = {}
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

        def __init__(self, width, height, seed, entry, exit_):

            self.width = width
            self.height = height
            self.seed = seed
            self.entry = entry
            self.exit_ = exit_
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

            y, x = self.exit_
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

def generator_entery(width, height, seed, entry, exit_, is_perfect):

    maze_gen = MazeGenerator(width, height, seed, entry, exit_)

    maze_gen.where_is_42()
    maze = maze_gen.generate_perfect_maze()

    if not is_perfect:
        maze = maze_gen.generate_non_perfect_maze()

    return maze
