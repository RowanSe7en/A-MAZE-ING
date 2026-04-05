#!/usr/bin/env python3

from parsing.parse_data import check_prop, check_all_available
from parsing.parse_data import open_file, parse_data
from algorithm.ascii_landing import ascii_landing
from menu import menu, color_menu
import algorithm
import sys


def get_data():

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


def renderer(is_solved, data, is_colored, maze, parents, theme_id=None):
    algorithm.MazeRenderer(
        data["width"],
        data["height"],
        data["entry"],
        data["exit"],
        maze,
        parents,
        is_solved,
        is_colored,
        theme_id,
        data["solve_time"]
        )


def entery_point(data, is_ft_printable):

    algorithm.clear()

    maze = algorithm.generator_entery(
        data["width"],
        data["height"],
        data.get("seed", None),
        data["entry"],
        data["exit"],
        data["perfect"],
        data["generate_time"],
        is_ft_printable
        )
    parents = algorithm.solver_entery(
        data["width"],
        data["height"],
        data["entry"],
        data["exit"],
        data["output_file"],
        data.get("solve", None),
        maze
        )

    return {"maze": maze, "parents": parents}


def main():

    ascii_landing()

    try:

        data_dict = get_data()
        data = data_dict["data"]

        is_ft_printable = data_dict["is_ft_printable"]
        is_solved = False
        is_colored = False

        input("Press ENTER key to start... ")
        maze_data = entery_point(data, is_ft_printable)

        while (True):

            try:
                num = menu()

                if num == "":
                    print("YOU LEFT THE MAZE, SEE YOU LATER ALLIGATOR")
                    exit(0)
                else:
                    num = int(num)

            except Exception:
                raise ValueError("choise Not Valid number")

            if num == 1:
                is_solved = False
                maze_data = entery_point(data, is_ft_printable)

            elif num == 2:

                if is_solved:
                    is_solved = False
                else:
                    is_solved = True

                renderer(
                    is_solved,
                    data,
                    is_colored,
                    maze_data['maze'], maze_data['parents'])

            elif num == 3:

                theme_id = color_menu()

                is_colored = True
                renderer(
                    is_solved,
                    data,
                    is_colored,
                    maze_data['maze'], maze_data['parents'], theme_id)
                is_colored = False

            elif num == 4:
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
