#!/usr/bin/env python3

# data = ["width", "height", "entry", "exit", "output_file", "perfect"]
import sys

def open_file():
    with open("config.txt", "r") as f:
        data_list = f.read()
    return data_list


def parse_data(file_data: list) -> dict:
    data_dict = {}
    for line_num, item in enumerate(file_data, 1):
        line = item.strip()
        if not line or line.startswith("#"):
            continue
        
        if "=" not in line:
            print(f"Error in line {line_num}: Invalid format '{line}'. Use KEY=VALUE")
            exit(1) 

        parts = line.split("=", 1)
        data_dict[parts[0].strip().lower()] = parts[1].strip()
    return data_dict

def check_prop(dict_data: dict) -> dict:
    data_parsed = {}
    
    for key, val in dict_data.items():
        try:
            if key in ["width", "height"]:
                data_parsed[key] = int(float(val))
                if data_parsed[key] < 0:
                    raise ValueError
            elif key in ["entry", "exit"]:
                coords = [int(x.strip()) for x in val.split(',')]
                if len(coords) != 2:
                    raise ValueError
                data_parsed[key] = tuple(coords)
                
            elif key == "output_file":
                if not val.endswith(".txt"):
                    print(f"Error: {val} must end with .txt")
                    sys.exit(1)
                data_parsed[key] = val
                
            elif key == "perfect":
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



f = open_file().split('\n')
d = parse_data(f)
a = check_prop(d)
e = check_all_available(a)
