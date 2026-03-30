#!/usr/bin/env python3
import sys
from parsing.parse_data import open_file, parse_data, check_prop, check_all_available
from menu import menu
from algorithm.maze_generator import *
from algorithm.maze_solver import *
from algorithm.maze_renderer import *

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

def rendering(is_solved, data, is_colored):
    maze = generator_entery(data["width"], data["height"], data.get("seed",None), data["entry"], data["exit"], data["perfect"])
    parents = solver_entery(data["width"], data["height"], data["entry"], data["exit"], data["output_file"], data.get("solve", None), maze)
    MazeRenderer(data["width"], data["height"], data["entry"], data["exit"], maze, parents, is_solved, is_colored)
    
def main():
    try:
        data = get_data()
        is_solved = False
        is_colored = False
        rendering(is_solved, data, is_colored)
        while(True):
            try:
                num = menu()
                if num == "":
                    print("YOU LEFT THE MAZE, SEE YOU LATER ALLIGATOR")
                    exit(1)
                num = int(menu())
            except Exception:
                raise ValueError ("choise Not Valid number")
            if num ==  1:
                rendering(is_solved, data)
            elif num ==  2:
                if is_solved:
                    is_solved = False
                else:
                    is_solved = True
                rendering(is_solved, data, is_colored)
            elif num == 3:
                is_colored = True
                rendering(is_solved,data, is_colored)
                is_colored = False 
            elif num == 4:
                break
    except KeyboardInterrupt:
        print("dhf")
        exit(1)
    except Exception as error:

        print(f"Error: {error}")

main()