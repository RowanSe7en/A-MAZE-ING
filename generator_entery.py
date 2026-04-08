import mazegen
import algorithm
from typing import List, Tuple, Optional, TypedDict


class MazeData(TypedDict):
    """
    TypedDict representing the output of the maze generator.

    Attributes:
        maze (List[List[int]]): 2D list representing the maze cells.
        ft_coords (List[Tuple[int, int]]): Coordinates of the "42 pattern".
    """
    maze: List[List[int]]
    ft_coords: List[Tuple[int, int]]


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
    """
    Generates a maze with optional visual
    features and validation for entry and exit points.

    Args:
        width (int): Width of the maze.
        height (int): Height of the maze.
        seed (Optional[int]): Random seed for deterministic maze generation.
        entry (Tuple[int, int]): Coordinates (y, x) of the maze entry point.
        exit_ (Tuple[int, int]): Coordinates (y, x) of the maze exit point.
        is_perfect (bool): If True, generates a perfect maze;
                           otherwise, adds loops to create a non-perfect maze.
        generator_time (float): Time delay (in seconds)
        between each step for animation.
        is_ft_printable (bool): If True adds a "42 pattern" to the maze center.
        theme_id (Optional[str]): theme identifier for rendering the maze.

    Raises:
        SystemExit: If the entry or exit coordinates
        are placed inside the "42 pattern".

    Returns:
        MazeData: A dictionary containing:
            - 'maze': 2D list of maze cells.
            - 'ft_coords': Coordinates of the "42 pattern" cells.
    """
    maze_gen = mazegen.MazeGenerator(
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

            algorithm.ascii_landing()
            print(
                "The entery is placed inside of the 42 pattern, "
                "please enter another cords"
            )
            exit(0)

        elif cord == exit_:

            algorithm.ascii_landing()
            print(
                "The exit is placed inside of the 42 pattern, "
                "please enter another cords"
            )
            exit(0)

    maze = maze_gen.generate_perfect_maze(generator_time, is_perfect, theme_id)

    if not is_perfect:
        maze = maze_gen.generate_non_perfect_maze(generator_time, theme_id)

    return {"maze": maze, "ft_coords": maze_gen.ft_coords}
