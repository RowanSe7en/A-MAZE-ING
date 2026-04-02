from algorithm.maze_generator import MazeGenerator
import random


class MazeSolver:

    def __init__(self, width, height, entry, exit_):

        self.width = width
        self.height = height
        self.entry = entry
        self.exit_ = exit_
        self.visited = [
            [False for _ in range(self.width)]
            for _ in range(self.height)
            ]

    def bfs_solve_maze(self, maze):

        en_y, en_x = self.entry
        ex_y, ex_x = self.exit_

        self.visited[en_y][en_x] = True

        queue = [self.entry]
        parents = {}

        while queue:

            y, x = queue[0]
            queue.pop(0)

            if (y, x) == self.exit_:
                break

            for dy, dx, wall, direc in MazeGenerator.directions:

                ny = y + dy
                nx = x + dx

                if (
                    nx >= 0
                    and ny >= 0
                    and nx < self.width
                    and ny < self.height
                ):

                    if not self.visited[ny][nx]:

                        if not (maze[y][x] & wall):

                            self.visited[ny][nx] = True
                            parents[(ny, nx)] = (y, x, direc)
                            queue.append((ny, nx))

        return parents

    def dfs_solve_maze(self, maze):

        en_y, en_x = self.entry
        ex_y, ex_x = self.exit_

        self.visited[en_y][en_x] = True

        queue = [self.entry]
        parents = {}

        while queue:

            y, x = queue[-1]

            neighbors = []

            if (y, x) == self.exit_:
                break

            for dy, dx, wall, direc in MazeGenerator.directions:

                ny = y + dy
                nx = x + dx

                if (
                    nx >= 0
                    and ny >= 0
                    and nx < self.width
                    and ny < self.height
                ):

                    if not self.visited[ny][nx]:

                        if not (maze[y][x] & wall):

                            neighbors.append((ny, nx, wall, direc))

            if neighbors:

                random_true = random.Random()
                ny, nx, wall, direc = random_true.choice(neighbors)

                self.visited[ny][nx] = True
                parents[(ny, nx)] = (y, x, direc)
                queue.append((ny, nx))

            else:
                queue.pop()

        return parents

    def extract_the_path(self, output_file, maze, parents):

        path_list = []
        path_cords = {}
        current = self.exit_

        while current != self.entry:

            py, px, direction = parents[current]
            path_list.append(direction)
            path_cords[current] = (py, px, direction)
            current = (py, px)

        path_list.reverse()
        path_str = "".join(path_list)

        with open(output_file, 'w') as output_maze:

            for row in maze:

                output_maze.write(
                            "".join(
                                f"{cell-1:X}" if cell == 16 else f"{cell:X}"
                                for cell in row
                            )
                        )
                output_maze.write("\n")

            en_y, en_x = self.entry
            ex_y, ex_x = self.exit_
            output_maze.write(f"\n{en_y}, {en_x}\n")
            output_maze.write(f"{ex_y}, {ex_x}\n")
            output_maze.write(path_str)
        
        return dict(reversed(list(path_cords.items())))

def solver_entery(width, height, entry, exit_, out_file, solve, maze):

    maze_solver = MazeSolver(width, height, entry, exit_)

    if solve.upper() == "DFS":
        parents = maze_solver.dfs_solve_maze(maze)
    elif solve.upper() == "BFS":
        parents = maze_solver.bfs_solve_maze(maze)

    path_cords = maze_solver.extract_the_path(out_file, maze, parents)

    return path_cords
