#!/usr/bin/env python3
import sys
import parsing
import algorithm
from generator_entery import generator_entery
from typing import Any, Dict, Optional, Union
from menu import menu, color_menu, change_config


def get_data() -> Dict[str, Any]:
    """
    Load, parse, and validate the configuration
    file provided as a CLI argument.

    This function ensures the program is
    executed with a valid configuration file,
    parses its content, validates the
    configuration properties, and checks for
    mandatory parameters.

    Returns:
        A dictionary containing:
            - "data": validated configuration values.
            - "is_ft_printable": boolean indicating if
            the maze can display the "42" pattern.

    Raises:
        ValueError: If the output file has
        the same name as the configuration file.
        SystemExit: If the CLI arguments are invalid.
    """
    if len(sys.argv) != 2:
        print("Error: must Entre valid args 'a_maze_ing.py config.txt'")
        sys.exit(0)

    if not sys.argv[1].endswith(".txt"):
        print(f"Error : {sys.argv[1]} not a valid file")
        sys.exit(0)

    f = parsing.open_file(sys.argv[1])

    parse = parsing.parse_data(f)
    check_proprety = parsing.check_prop(parse)
    require = parsing.check_all_available(check_proprety)

    if require["data"]["output_file"] == sys.argv[1]:
        raise ValueError(
            "The output file cannot be the same name as the config file "
        )

    return require


def renderer(
    is_solved: bool,
    data: Dict[str, Any],
    is_colored: bool,
    maze: Any,
    parents: Any,
    ft_coords: Any,
    theme_id: Optional[str] = None,
    is_already_changed: bool = False
) -> None:
    """
    Render the maze using the MazeRenderer from the algorithm module.

    Args:
        is_solved: Whether the solution path should be displayed.
        data: Configuration dictionary containing maze parameters.
        is_colored: Whether colored rendering is enabled.
        maze: Generated maze structure.
        parents: Parent mapping used for solution path reconstruction.
        ft_coords: Coordinates used for rendering the "42" pattern.
        theme_id: Optional theme identifier for wall colors.
    """
    algorithm.MazeRenderer(
        data["width"],
        data["height"],
        data["entry"],
        data["exit"],
        maze,
        parents,
        is_solved,
        is_colored,
        theme_id or "",  # <-- ensure it's always a string
        data["solve_time"],
        ft_coords,
        is_already_changed
    )


def entery_point(data: Dict[str, Any],
                 is_ft_printable: bool,
                 theme_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Generate a maze and compute its solution.

    This function clears the screen, generates a new maze, and runs the solver
    algorithm to compute the shortest path between entry and exit.

    Args:
        data: Validated configuration dictionary.
        is_ft_printable: Indicates if the
        maze is large enough to include the "42" pattern.
        theme_id: Optional theme identifier for rendering.

    Returns:
        A dictionary containing:
            - "maze": Generated maze data and metadata.
            - "parents": Parent mapping representing the solution path.
    """
    algorithm.clear()
    maze = generator_entery(
        data["width"],
        data["height"],
        data.get("seed", None),
        data["entry"],
        data["exit"],
        data["perfect"],
        data["generate_time"],
        is_ft_printable,
        theme_id
    )

    solve_value: str = str(data.get("solve", ""))
    parents = algorithm.solver_entery(
        data["width"],
        data["height"],
        data["entry"],
        data["exit"],
        data["output_file"],
        solve_value,
        maze["maze"]
    )

    return {"maze": maze, "parents": parents}


theme_id = "1"


def main() -> None:
    """
    Entry point of the application.

    Handles the full program lifecycle:
    - Displays the landing screen.
    - Loads configuration.
    - Generates the maze and runs the solver.
    - Provides an interactive menu for regenerating mazes, toggling solutions,
      changing colors, and updating configuration parameters.
    """
    global theme_id

    algorithm.ascii_landing()

    try:

        data_dict = get_data()
        data = data_dict["data"]

        is_ft_printable = data_dict["is_ft_printable"]
        is_solved = False
        is_colored = False

        input("Press ENTER key to start... ")
        maze_data = entery_point(data, is_ft_printable, theme_id)

        while True:

            try:

                num: Union[int, str] = menu()
                num = int(num)

            except Exception:
                pass

            if num == 1:
                is_solved = False
                maze_data = entery_point(data, is_ft_printable, theme_id)

            elif num == 2:

                if is_solved:
                    is_solved = False
                else:
                    is_solved = True

                renderer(
                    is_solved,
                    data,
                    is_colored,
                    maze_data['maze']['maze'],
                    maze_data['parents'],
                    maze_data['maze']['ft_coords']
                )

            elif num == 3:

                theme_id = color_menu()

                is_not_party_mode = True
                if theme_id == "9":
                    is_not_party_mode = False

                is_colored = True
                renderer(
                    is_solved,
                    data,
                    is_colored,
                    maze_data['maze']['maze'],
                    maze_data['parents'],
                    maze_data['maze']['ft_coords'],
                    theme_id,
                    is_not_party_mode
                )
                is_colored = False

            elif num == 4:

                key_change: Dict[str, Any] = change_config()

                if key_change:

                    dict_key = list(key_change.keys())[0]

                    if dict_key in ["generate_time", "solve_time"]:
                        data["animation"] = True

                    new_dict = parsing.check_prop(key_change, True)
                    data[dict_key] = new_dict[dict_key]

                    is_colored = False
                    is_solved = False

                    all_keys = [
                        "width", "height", "entry", "exit",
                        "seed", "perfect"
                    ]

                    if dict_key in all_keys:

                        if data['width'] < 9 or data['height'] < 7:
                            maze_data = entery_point(data, False, theme_id)
                        else:
                            maze_data = entery_point(data, True, theme_id)

                    else:

                        renderer(
                            is_solved,
                            data,
                            is_colored,
                            maze_data['maze']['maze'],
                            maze_data['parents'],
                            maze_data['maze']['ft_coords']
                            )

            elif num == 5:
                print("\nYOU LEFT THE MAZE, SEE YOU LATER ALLIGATOR")
                break

            else:
                print("Invalid choice, please try again. (1-4)")

    except KeyboardInterrupt:

        print("\nYOU LEFT THE MAZE, SEE YOU LATER ALLIGATOR")
        exit(0)

    except Exception as error:
        algorithm.ascii_landing()
        print(f"Handeled Error: {error}")


if __name__ == "__main__":
    main()
