#!/usr/bin/env python3
from typing import Any, Dict, Optional, Union
from parsing.parse_data import check_prop, check_all_available
from parsing.parse_data import open_file, parse_data
from algorithm.ascii_landing import ascii_landing
from menu import menu, color_menu, change_config
import algorithm
import sys


def get_data() -> Dict[str, Any]:

    if len(sys.argv) != 2:
        print("Error: must Entre valid args 'a_maze_ing.py config.txt'")
        sys.exit(0)

    if not sys.argv[1].endswith(".txt"):
        print(f"Error : {sys.argv[1]} not a valid file")
        sys.exit(0)

    f = open_file(sys.argv[1])

    parse = parse_data(f)
    check_proprety = check_prop(parse)
    require = check_all_available(check_proprety)

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
    theme_id: Optional[str] = None
) -> None:
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
        ft_coords
    )


def entery_point(data: Dict[str, Any],
                 is_ft_printable: bool,
                 theme_id: Optional[str] = None) -> Dict[str, Any]:

    algorithm.clear()

    print(theme_id)

    maze = algorithm.generator_entery(
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

    global theme_id

    ascii_landing()

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

                if num == "":
                    print("YOU LEFT THE MAZE, SEE YOU LATER ALLIGATOR")
                    exit(0)
                else:
                    num = int(num)

            except Exception:
                raise ValueError("choise Not Valid number")

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

                is_colored = True
                renderer(
                    is_solved,
                    data,
                    is_colored,
                    maze_data['maze']['maze'],
                    maze_data['parents'],
                    maze_data['maze']['ft_coords'],
                    theme_id
                )
                is_colored = False

            elif num == 4:

                key_change: Dict[str, Any] = change_config()

                if key_change:

                    dict_key = list(key_change.keys())[0]

                    if dict_key in ["generate_time", "solve_time"]:
                        data["animation"] = True

                    new_dict = check_prop(key_change, True)
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
        ascii_landing()
        print(f"Handeled Error: {error}")


main()
