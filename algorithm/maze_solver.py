from maze_generator import *

path_list = []

class MazeSolver:

    def __init__(self, width, height, entry, exit_):

        self.width = width
        self.height = height
        self.entry = entry
        self.exit_ = exit_
        self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]

    def bfs_solve_maze(self, output_file): #bfs

        en_y, en_x = self.entry
        ex_y, ex_x = self.exit_

        self.visited[en_y][en_x] = True

        queue = [self.entry]

        while queue:

            y, x = queue[0]
            queue.pop(0)

            if (y, x) == self.exit_:
                break

            for dy, dx, wall, direc in MazeGenerator.directions:

                ny = y + dy
                nx = x + dx

                if nx >= 0 and ny >= 0 and nx < self.width and ny < self.height:

                    if not self.visited[ny][nx]:

                        if not (self.maze[y][x] & wall):

                            self.visited[ny][nx] = True
                            parents[(ny, nx)] = (y, x, direc)
                            queue.append((ny, nx))

        global path_list

        current = self.exit_

        while current != self.entry:

            py, px, direction = parents[current]
            path_list.append(direction)
            current = (py, px)

        path_list.reverse()
        path_str = "".join(path_list)

        with open(output_file, 'w') as output_maze:

            for row in self.maze:

                output_maze.write("".join(f"{cell:X}" for cell in row))
                output_maze.write("\n")

            output_maze.write(f"\n{en_y}, {en_x}\n")
            output_maze.write(f"{ex_y}, {ex_x}\n")
            output_maze.write(path_str)

    def dfs_solve_maze(self, output_file): #dfs

        en_y, en_x = self.entry
        ex_y, ex_x = self.exit_

        self.visited[en_y][en_x] = True

        queue = [self.entry]

        while queue:

            y, x = queue[-1]

            neighbors = []


            if (y, x) == self.exit_:
                break

            for dy, dx, wall, direc in MazeGenerator.directions:

                ny = y + dy
                nx = x + dx

                if nx >= 0 and ny >= 0 and nx < self.width and ny < self.height:

                    if not self.visited[ny][nx]:

                        if not (self.maze[y][x] & wall):

                            neighbors.append((ny, nx, wall, direc))

            if neighbors:

                random_true = random.Random()
                ny, nx, wall, direc = random_true.choice(neighbors)

                self.visited[ny][nx] = True
                parents[(ny, nx)] = (y, x, direc)
                queue.append((ny, nx))

            else:
                queue.pop()

        current = self.exit_

        global path_list

        while current != self.entry:

            py, px, direction = parents[current]
            path_list.append(direction)
            current = (py, px)

        path_list.reverse()
        path_str = "".join(path_list)

        with open(output_file, 'w') as output_maze:

            for row in self.maze:

                output_maze.write("".join(f"{cell:X}" for cell in row))
                output_maze.write("\n")

            output_maze.write(f"\n{en_y}, {en_x}\n")
            output_maze.write(f"{ex_y}, {ex_x}\n")
            output_maze.write(path_str)


def solver_entery(width, height, entry, exit_, out_file, solve):

    maze_solver = MazeSolver(width, height, entry, exit_)

    if solve.upper() == "DFS":
        maze_solver.dfs_solve_maze(out_file)
    elif solve.upper() == "BFS":
        maze_solver.bfs_solve_maze(out_file)
