#!/usr/bin/env python3

import sys

def open_file(filename: str):
    try:
        with open(filename, "r") as f:
            data_list = f.read().splitlines()
        return data_list
    except (FileNotFoundError, PermissionError):
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)


def parse_data(file_data: list) -> dict:
    data_dict = {}
    for line_num, item in enumerate(file_data, 1):
        line = item.strip()
        if not line or line.startswith("#"):
            continue
        
        if "=" not in line:
            print(f"Error in line {line_num}: Invalid format '{line}'. Use KEY=VALUE")
            sys.exit(1) 

        parts = line.split("=", 1)
        data_dict[parts[0].strip().lower()] = parts[1].strip()
    return data_dict

def check_prop(dict_data: dict) -> dict:
    data_parsed = {}
    
    for key, val in dict_data.items():
        try:
            if key in ["width", "height"]:
                data_parsed[key] = int(float(val))
                if data_parsed[key] <= 0:
                    raise ValueError
            elif key in ["entry", "exit"]:
                cords = [int(x.strip()) for x in val.split(',')]
                if len(cords) != 2:
                    raise ValueError
                if cords[0] < 0 or cords[1] < 0:
                    print(f"Error: {key} coordinates cannot be negative.")
                    sys.exit(1)
                data_parsed[key] = tuple(cords)
                
            elif key == "output_file":
                if not val.endswith(".txt"):
                    print(f"Error: {val} must end with .txt")
                    sys.exit(1)
                data_parsed[key] = val
                
            elif key == "perfect":
                if val.lower() not in ['true','false']:
                    raise ValueError
                data_parsed[key] = val.lower() == "true"
                
        except Exception:
            print(f"Error: Invalid value for {key} = {val}")
            sys.exit(1)
    return data_parsed

def check_all_available(data: dict):
    required = ["width", "height", "entry", "exit", "output_file"]
    missing = [k for k in required if k not in data]
    
    if missing:
        for item in missing:
            print(f"Missing mandatory key: {item}")
        sys.exit(1)
    if data["entry"] == data["exit"]:
        print("Error: (entry == exit)")
        sys.exit(1)
    return data