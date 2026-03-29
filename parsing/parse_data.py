#!/usr/bin/env python3

import sys

def open_file(filename: str):
    try:
        with open(filename, "r") as f:
            data_list = f.read().splitlines()
        return data_list
    except (FileNotFoundError, PermissionError):
        raise ValueError(f"File '{filename}' not found.")


def parse_data(file_data: list) -> dict:
    data_dict = {}
    for line_num, item in enumerate(file_data, 1):
        line = item.strip()
        if not line or line.startswith("#"):
            continue
        
        if "=" not in line:
            raise ValueError(f"in line {line_num}: Invalid format '{line}'. Use KEY=VALUE")

        parts = line.split("=", 1)
        data_dict[parts[0].strip().lower()] = parts[1].strip()
    return data_dict

def check_prop(dict_data: dict) -> dict:
    data_parsed = {}
    for key, val in dict_data.items():
        if key in ["width", "height"]:
            data_parsed[key] = int(float(val))
            if data_parsed[key] <= 0:
                raise ValueError
        elif key in ["entry", "exit"]:
            cords = [int(x.strip()) for x in val.split(',')]
            if len(cords) != 2:
                raise ValueError
            if cords[0] < 0 or cords[1] < 0:
                raise ValueError(f"{key} coordinates cannot be negative.")
                sys.exit(1)
            data_parsed[key] = tuple(cords)
            
        elif key == "output_file":
            if not val.endswith(".txt"):
                raise ValueError(f"{val} must end with .txt")
            if val == "config.txt":
                raise ValueError(f"The output file cannot be the same name as the config file 'config.txt'")
            data_parsed[key] = val
        elif key == "perfect":
            if val.lower() not in ['true','false']:
                raise ValueError
            data_parsed[key] = val.lower() == "true"
        elif key == "seed":
            try:
                data_parsed[key] = int(val)
            except Exception:
                data_parsed[key] = None
        elif key == "animation":
            if val.lower() in ['true','false']:
                data_parsed[key] = val.lower() == "true"
        elif key == "solve":
            if val.lower() in ['dfs','bfs']:
                data_parsed[key] = val.lower()
            else:
                data_parsed[key] = "dfs"
    return data_parsed

def check_all_available(data: dict):
    required = ["width", "height", "entry", "exit", "output_file","perfect"]
    missing = [k for k in required if k not in data]

    if missing:
        for item in missing:
            raise ValueError(f"Missing mandatory key: {item}")
    if data["entry"] == data["exit"]:
        raise ValueError("(entry == exit)")
    if data['width'] < 5 or data['height'] < 7:
        raise ValueError('The maze is so tiny')
    elif data['width'] > 50 or data['height'] > 25:
        raise ValueError('The maze is so huge')
         
    w, h = data["width"], data['height']
    en_x, en_y = data["entry"]
    ex_x, ex_y = data["exit"]
    if not (0 <= en_y < w and 0 <= en_x < h):
        raise ValueError(f"Entry {data['entry']} is outside the maze bounds.")
    elif not (0 <= ex_y < w and 0 <= ex_x < h):
        raise ValueError(f"Exit {data['exit']} is outside the maze bounds.")
    return data