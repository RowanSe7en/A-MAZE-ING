#!/usr/bin/env python3
import sys
from parsing.parse_data import open_file, parse_data, check_prop, check_all_available
from menu import menu
from algorithm.maze_generator import *
from algorithm.maze_solver import *

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
    return require


def main():
    try:
        data = get_data()
        maze = generator_entery(data["width"], data["height"], data.get("seed",None), data["entry"], data["exit"], data["perfect"])
        solver_entery(data["width"], data["height"], data["entry"], data["exit"], data["output_file"], data.get("solve", None), maze)
        # while(True):
        #     if int(num) ==  1:
        #         r.run(data)
        #     elif int(num) == 4:
        #         break
    except Exception as error:
        print(f"Error: {error}")

main()