import random
from mazegen.maze_generator import MazeGenerator
from typing import List, Tuple, Dict


class MazeSolver:
    """
    Maze solving engine using BFS and DFS algorithms.

    This class is responsible for exploring a generated maze and finding a
    path from the entry cell to the exit cell. It stores visited cells to
    avoid revisiting them and builds a parent dictionary that allows the
    reconstruction of the final solution path.
    """
    def __init__(self, width: int, height: int, entry: Tuple[int, int],
                 exit_: Tuple[int, int]) -> None:
        """
        Initialize the MazeSolver.

        Parameters
        ----------
        width : int
            Width of the maze.
        height : int
            Height of the maze.
        entry : Tuple[int, int]
            Starting cell coordinates (row, column).
        exit_ : Tuple[int, int]
            Exit cell coordinates (row, column).
        """
        self.width: int = width
        self.height: int = height
        self.entry: Tuple[int, int] = entry
        self.exit_: Tuple[int, int] = exit_
        self.visited: List[List[bool]] = [
            [False for _ in range(self.width)]
            for _ in range(self.height)
        ]

    def bfs_solve_maze(self, maze: List[List[int]]
                       ) -> Dict[Tuple[int, int], Tuple[int, int, str]]:
        """
        Solve the maze using Breadth-First Search (BFS).

        BFS explores the maze level by level and guarantees finding the
        shortest path in an unweighted maze.

        Parameters
        ----------
        maze : List[List[int]]
            Maze grid encoded using wall bitmasks.

        Returns
        -------
        Dict[Tuple[int, int], Tuple[int, int, str]]
            A dictionary mapping each visited cell to its parent cell and the
            direction taken to reach it.
        """
        en_y, en_x = self.entry
        ex_y, ex_x = self.exit_

        self.visited[en_y][en_x] = True

        queue: List[Tuple[int, int]] = [self.entry]
        parents: Dict[Tuple[int, int], Tuple[int, int, str]] = {}

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

    def dfs_solve_maze(self, maze: List[List[int]]
                       ) -> Dict[Tuple[int, int], Tuple[int, int, str]]:
        """
        Solve the maze using Depth-First Search (DFS).

        DFS explores one branch deeply before backtracking. The solution
        found is not guaranteed to be the shortest path but is usually
        faster in exploration.

        Parameters
        ----------
        maze : List[List[int]]
            Maze grid.

        Returns
        -------
        Dict[Tuple[int, int], Tuple[int, int, str]]
            Parent dictionary used to reconstruct the solution path.
        """
        en_y, en_x = self.entry
        ex_y, ex_x = self.exit_

        self.visited[en_y][en_x] = True

        queue: List[Tuple[int, int]] = [self.entry]
        parents: Dict[Tuple[int, int], Tuple[int, int, str]] = {}

        while queue:

            y, x = queue[-1]

            neighbors: List[Tuple[int, int, int, str]] = []

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

    def extract_the_path(self, output_file: str, maze: List[List[int]],
                         parents: Dict[Tuple[int, int], Tuple[int, int, str]]
                         ) -> Dict[Tuple[int, int], Tuple[int, int, str]]:
        """
        Reconstruct the solution path and export the solved maze to a file.

        The function:
        1. Rebuilds the path from the parents dictionary.
        2. Writes the maze in hexadecimal format.
        3. Writes entry and exit coordinates.
        4. Writes the solution path directions.

        Parameters
        ----------
        output_file : str
            Path to the output file.
        maze : List[List[int]]
            Maze grid.
        parents : Dict[Tuple[int,int], Tuple[int,int,str]]
            Parent mapping returned by the solver.

        Returns
        -------
        Dict[Tuple[int,int], Tuple[int,int,str]]
            Ordered dictionary representing the solution path.
        """
        path_list: List[str] = []
        path_cords: Dict[Tuple[int, int], Tuple[int, int, str]] = {}
        current: Tuple[int, int] = self.exit_

        while current != self.entry:

            py, px, direction = parents[current]
            path_list.append(direction)
            path_cords[current] = (py, px, direction)
            current = (py, px)

        path_list.reverse()
        path_str: str = "".join(path_list)

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
            output_maze.write(f"\n{en_y},{en_x}\n")
            output_maze.write(f"{ex_y},{ex_x}\n")
            output_maze.write(path_str)

        return dict(reversed(list(path_cords.items())))


def solver_entery(width: int, height: int, entry: Tuple[int, int],
                  exit_: Tuple[int, int], out_file: str,
                  solve: str, maze: List[List[int]]
                  ) -> Dict[Tuple[int, int], Tuple[int, int, str]]:
    """
    Entry point for maze solving.

    Creates a MazeSolver instance, runs the selected algorithm,
    exports the solved maze, and returns the solution path.

    Parameters
    ----------
    width, height : int
        Maze dimensions.
    entry, exit_ : Tuple[int, int]
        Start and exit cells.
    out_file : str
        Output file path.
    solve : str
        Solving algorithm ("BFS" or "DFS").
    maze : List[List[int]]
        Maze grid.

    Returns
    -------
    Dict[Tuple[int,int], Tuple[int,int,str]]
        Solution path coordinates.
    """
    maze_solver = MazeSolver(width, height, entry, exit_)

    if solve.upper() == "DFS":
        parents = maze_solver.dfs_solve_maze(maze)
    elif solve.upper() == "BFS":
        parents = maze_solver.bfs_solve_maze(maze)

    path_cords = maze_solver.extract_the_path(out_file, maze, parents)

    return path_cords
