#!/usr/bin/env python3
import sys
from parsing.parse_data import open_file, parse_data, check_prop, check_all_available
from menu import menu, color_menu
import algorithm
import os

def get_data():
    if len(sys.argv) != 2:
        print("Error: must Entre valid args 'a_maze_ing.py config.txt'")
        sys.exit(1)
    if not sys.argv[1].endswith(".txt"):
        print(f"Error : {sys.argv[1]} not a valid file")
        sys.exit(1)
    f = open_file(sys.argv[1])
    parse = parse_data(f)
    check_proprety = check_prop(parse)
    require = check_all_available(check_proprety)
    if require["output_file"] == sys.argv[1]:
        raise ValueError(f"The output file cannot be the same name as the config file ")
    return require

def renderer(is_solved, data, is_colored, maze, parents, theme_id=None):
    algorithm.MazeRenderer(data["width"], data["height"], data["entry"], data["exit"], maze, parents, is_solved, is_colored, theme_id)


def entery_point(data, is_colored, theme_id=None):
    os.system("clear")
    maze = algorithm.generator_entery(data["width"], data["height"], data.get("seed",None), data["entry"], data["exit"], data["perfect"], is_colored, theme_id)
    parents = algorithm.solver_entery(data["width"], data["height"], data["entry"], data["exit"], data["output_file"], data.get("solve", None), maze)

    return { "maze": maze, "parents": parents}
    
def main():

    os.system("clear")

    print(r"""
    ╔══════════════════════════════════════════════════════════════════════════════════╗
    ║                                                                                  ║
    ║      █████╗     ███╗   ███╗ █████╗ ███████╗███████╗    ██╗███╗   ██╗ ██████╗     ║
    ║     ██╔══██╗    ████╗ ████║██╔══██╗╚══███╔╝██╔════╝    ██║████╗  ██║██╔════╝     ║
    ║     ███████║    ██╔████╔██║███████║  ███╔╝ █████╗      ██║██╔██╗ ██║██║  ███╗    ║
    ║     ██╔══██║    ██║╚██╔╝██║██╔══██║ ███╔╝  ██╔══╝      ██║██║╚██╗██║██║   ██║    ║
    ║     ██║  ██║    ██║ ╚═╝ ██║██║  ██║███████╗███████╗    ██║██║ ╚████║╚██████╔╝    ║
    ║     ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝╚═╝  ╚═══╝ ╚═════╝     ║
    ║                                                                                  ║
    ║                           🧩  A - M A Z E - I N G  🧩                            ║
    ║                                                                                  ║
    ║                         Created by brouane / bmarbouh                            ║
    ╠══════════════════════════════════════════════════════════════════════════════════╣
    ║                                                                                  ║
    ║   • Generate perfect & imperfect mazes                                           ║
    ║   • Visualize solving algorithms                                                 ║
    ║   • Optional colored rendering                                                   ║
    ║                                                                                  ║
    ╚══════════════════════════════════════════════════════════════════════════════════╝
""")
    try:

        data = get_data()
        is_solved = False
        is_colored = False

        input("Press any key to start...")
        maze_data = entery_point(data, is_colored)

        while(True):

            try:

                num = menu()

                if num == "":
                    print("YOU LEFT THE MAZE, SEE YOU LATER ALLIGATOR")
                    exit(1)
                else:
                    num = int(num)

            except Exception:
                raise ValueError ("choise Not Valid number")

            if num ==  1:
                maze_data = entery_point(data, is_colored)

            elif num ==  2:

                if is_solved:
                    is_solved = False
                else:
                    is_solved = True
                renderer(is_solved, data, is_colored, maze_data['maze'], maze_data['parents'])

            elif num == 3:

                color_choise = color_menu()

                is_colored = True
                renderer(is_solved, data, is_colored, maze_data['maze'], maze_data['parents'], color_choise)
                is_colored = False 

            elif num == 4:
                break

    except KeyboardInterrupt:

        print("\nYOU LEFT THE MAZE, SEE YOU LATER ALLIGATOR")
        exit(1)

    except Exception as error:
        print(f"Error: {error}")

main()