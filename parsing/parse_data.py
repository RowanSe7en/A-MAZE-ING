#!/usr/bin/env python3


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
            raise ValueError(
                f"in line {line_num}: Invalid format '{line}'. Use KEY=VALUE"
                )

        parts = line.split("=", 1)
        data_dict[parts[0].strip().lower()] = parts[1].strip()

    return data_dict


def check_prop(dict_data: dict) -> dict:

    data_parsed = {}

    for key, val in dict_data.items():

        if key in ["width", "height"]:
            try:
                data_parsed[key] = int(float(val))
            except Exception:
                raise ValueError(f"Invalid value for '{key}': must be a positive integer.")

            if data_parsed[key] <= 0:
                raise ValueError(f"Invalid value for '{key}': must be a positive integer.")

        elif key in ["entry", "exit"]:
            
            try:
                cords = [int(x.strip()) for x in val.split(',')]
            except ValueError:
                raise ValueError(f"Invalid value for '{key}': the keys x and y are not integers.")

            if len(cords) != 2:
                raise ValueError(f"Invalid value for '{key}': must be in this format (<y>, <x>).")

            if cords[0] < 0 or cords[1] < 0:
                raise ValueError(f"Invalid value for '{key}': coordinates cannot be negative.")

            data_parsed[key] = tuple(cords)

        elif key == "output_file":

            if not val.endswith(".txt"):
                raise ValueError(f"Invalid value for '{key}': must end with '.txt'")

            data_parsed[key] = val

        elif key == "perfect":

            if val.lower() not in ['true', 'false']:
                raise ValueError(f"Invalid value for '{key}': must be 'true' or 'false'")
            data_parsed[key] = val.lower() == "true"

        elif key == "seed":

            try:
                data_parsed[key] = int(val)
            except Exception:
                data_parsed[key] = None

        elif key == "animation":

            if val.lower() in ['true', 'false']:
                data_parsed[key] = val.lower() == "true"

        elif key == "solve":

            if val.lower() in ['dfs', 'bfs']:
                data_parsed[key] = val.lower()
            else:
                data_parsed[key] = "dfs"

        elif key == "generate_time":

            try:
                data_parsed[key] = float(val)
            except Exception:
                data_parsed[key] = -1

        elif key == "solve_time":

            try:
                data_parsed[key] = float(val)
            except Exception:
                data_parsed[key] = -1

    if not data_parsed.get("animation", False):

        data_parsed["solve_time"] = 0
        data_parsed["generate_time"] = 0

    else:

        if float(data_parsed.get("solve_time", -1)) < 0:
            data_parsed["solve_time"] = 0.1

        if float(data_parsed.get("generate_time", -1)) < 0:
            data_parsed["generate_time"] = 0.05
            


    return data_parsed


def check_all_available(data: dict):

    required = ["width", "height", "entry", "exit", "output_file", "perfect"]
    missing = [k for k in required if k not in data]
    is_ft_printable = True

    if missing:

        for item in missing:
            raise ValueError(f"Missing mandatory key: {item}")

    if data["entry"] == data["exit"]:
        raise ValueError(f"Invalid value for '{data['exit']}' and '{data['entry']}': entry and exit cannot be the same.")

    if data['width'] < 9 or data['height'] < 7:
        is_ft_printable = False

    w, h = data["width"], data['height']
    en_x, en_y = data["entry"]
    ex_x, ex_y = data["exit"]

    if not (0 <= en_y < w and 0 <= en_x < h):
        raise ValueError(f"The entry {data['entry']} is outside the maze bounds.")
    elif not (0 <= ex_y < w and 0 <= ex_x < h):
        raise ValueError(f"The exit {data['exit']} is outside the maze bounds.")

    return {"data": data, "is_ft_printable": is_ft_printable}
