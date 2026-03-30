from algorithm.maze_renderer import MazeRenderer
from algorithm.theme_palette import themes, theme_mapper


import random
import time
import os

def clear():
    os.system("clear")  # linux/mac
    # os.system("cls")  # windows

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
















        def ansi_render(self, is_colored, theme_id):
            

            theme = themes['ash_lava']
            wall_color   = theme['wall_color']
            road_color   = theme['road_color']
            entery_color    = theme['entery_color']
            exit_color = theme['exit_color']

            for y in range(self.height):
                print(wall_color, end="")

                for x in range(self.width):
                    if self.maze[y][x] & 1 or ((y, x) in ft_coords and self.maze[y - 1][x] != 16):
                        print(wall_color + wall_color, end="")
                    else:
                        if self.maze[y][x] == 16:
                            left = entery_color
                        # elif (y, x) in path_coords and (
                        #     (y > 0 and (y - 1, x) in path_coords) or (y - 1, x) == self.entry
                        # ) and is_solved:
                        #     left = path_color
                        else:
                            left = road_color

                        print(left + wall_color, end="")
                        
                print()

                for x in range(self.width):
                    # if (
                    #     (y, x) in path_coords
                    #     and (x > 0 and ((y, x - 1) in path_coords or (y, x - 1) == self.entry))
                    #     and not self.maze[y][x] & (1 << 3) and is_solved
                    # ):
                    #     left = path_color
                    if self.maze[y][x] == 16 and self.maze[y][x - 1] == 16:
                        left = entery_color
                    elif self.maze[y][x] & (1 << 3) or self.maze[y][x] & (1 << 4):
                        left = wall_color
                    else:
                        left = road_color

                    if (y, x) == self.entry:
                        content = entery_color
                    elif (y, x) == self.exit_:
                        content = exit_color
                    # elif (y, x) in path_coords and is_solved:
                    #     content = path_color
                    elif self.maze[y][x] == 16:
                        content = entery_color
                    else:
                        content = road_color

                    print(left + content, end="")

                right = wall_color if self.maze[y][self.width - 1] & (1 << 1) else ""
                print(right)
                # time.sleep(0.09)

            for x in range(self.width):
                if self.maze[self.height - 1][x] & (1 << 2):
                    print(wall_color + wall_color, end="")
                else:
                    print(road_color + road_color, end="")
            print(wall_color)


































        def generate_perfect_maze(self, is_colored, theme_id): #dfs

            if self.seed is not None:
                random.seed(self.seed)

            y, x = 0, 0
            self.visited[y][x] = True
            stack = [(y, x)]

            while stack:

                y, x = stack[-1]

                neighbors = []

                clear()
                self.ansi_render(is_colored, theme_id)
                time.sleep(0.003)


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

def generator_entery(width, height, seed, entry, exit_, is_perfect, is_colored, theme_id):

    maze_gen = MazeGenerator(width, height, seed, entry, exit_)

    maze_gen.where_is_42()
    maze = maze_gen.generate_perfect_maze(is_colored, theme_id)

    if not is_perfect:
        maze = maze_gen.generate_non_perfect_maze()

    return maze
