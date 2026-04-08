from typing import List, Dict, Any


def open_file(filename: str) -> List[str]:
    """
    Read a configuration file and return its content as a list of lines.

    Args:
        filename: Path to the configuration file.

    Returns:
        A list of strings representing
        each line of the file without newline characters.

    Raises:
        ValueError: If the file does not exist or cannot be accessed.
    """
    try:
        with open(filename, "r") as f:
            data_list = f.read().splitlines()
        return data_list

    except (FileNotFoundError, PermissionError):
        raise ValueError(f"File '{filename}' not found.")


def parse_data(file_data: List[str]) -> Dict[str, str]:
    """
    Parse raw configuration lines into a dictionary of key-value pairs.

    Ignores empty lines and comments starting with '#'. Each valid line must
    follow the format KEY=VALUE.

    Args:
        file_data: List of raw lines read from the configuration file.

    Returns:
        A dictionary mapping configuration
        keys (lowercased) to their string values.

    Raises:
        ValueError: If a line does not follow the KEY=VALUE format.
    """
    data_dict: Dict[str, str] = {}

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


def check_prop(dict_data: Dict[str, str],
               is_animated: bool = False) -> Dict[str, Any]:
    """
    Validate and convert configuration values to their appropriate types.

    This function parses numeric values, booleans, coordinates, and optional
    parameters used for maze generation, solving, and animation.

    Args:
        dict_data: Dictionary containing raw configuration values as strings.
        is_animated: Flag indicating whether
        animation mode is forced externally.

    Returns:
        A dictionary containing validated
        and properly typed configuration values.

    Raises:
        ValueError: If a configuration value
        is invalid or incorrectly formatted.
    """
    data_parsed: Dict[str, Any] = {}

    for key, val in dict_data.items():

        if key in ["width", "height"]:
            try:
                data_parsed[key] = int(float(val))
            except Exception:
                raise ValueError(
                    f"Invalid value for '{key}': must be a positive integer."
                )

            if data_parsed[key] <= 0:
                raise ValueError(
                    f"Invalid value for '{key}': must be a positive integer."
                )

        elif key in ["entry", "exit"]:

            try:
                cords = [int(x.strip()) for x in val.split(',')]
            except ValueError:
                raise ValueError(
                    f"Invalid value for '{key}'"
                    ": the keys x and y are not integers."
                )

            if len(cords) != 2:
                raise ValueError(
                    f"Invalid value for '{key}'"
                    ": must be in this format (<y>, <x>)."
                )

            if cords[0] < 0 or cords[1] < 0:
                raise ValueError(
                    f"Invalid value for '{key}'"
                    ": coordinates cannot be negative."
                )

            data_parsed[key] = tuple(cords)

        elif key == "output_file":

            if not val.endswith(".txt"):
                raise ValueError(
                    f"Invalid value for '{key}': must end with '.txt'"
                )

            data_parsed[key] = val

        elif key == "perfect":

            if val.lower() not in ['true', 'false']:
                raise ValueError(
                    f"Invalid value for '{key}': must be 'true' or 'false'"
                )
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

    if not data_parsed.get("animation", False) and not is_animated:

        data_parsed["solve_time"] = 0
        data_parsed["generate_time"] = 0

    else:

        if float(data_parsed.get("solve_time", -1)) < 0:
            data_parsed["solve_time"] = 0.1

        if float(data_parsed.get("generate_time", -1)) < 0:
            data_parsed["generate_time"] = 0.05

    return data_parsed


def check_all_available(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Ensure that all mandatory configuration values are present and valid.

    This function validates the presence of required keys, verifies that entry
    and exit positions are different and inside the maze bounds, and determines
    whether the maze is large enough to display the "42" pattern.

    Args:
        data: Dictionary containing validated configuration values.

    Returns:
        A dictionary containing:
            - "data": The validated configuration dictionary.
            - "is_ft_printable": Boolean indicating if the maze is large enough
              to display the "42" pattern.

    Raises:
        ValueError: If mandatory keys are missing or coordinates are invalid.
    """
    required = ["width", "height", "entry", "exit", "output_file", "perfect"]
    missing = [k for k in required if k not in data]
    is_ft_printable = True

    if missing:

        for item in missing:
            raise ValueError(f"Missing mandatory key: {item}")

    if data["entry"] == data["exit"]:
        raise ValueError(
            f"Invalid value for '{data['exit']}'"
            f" and '{data['entry']}': entry and exit cannot be the same."
        )

    if data['width'] < 9 or data['height'] < 7:
        is_ft_printable = False

    w, h = data["width"], data['height']
    en_x, en_y = data["entry"]
    ex_x, ex_y = data["exit"]

    if not (0 <= en_y < w and 0 <= en_x < h):
        raise ValueError(
            f"The entry {data['entry']} is outside the maze bounds."
        )
    elif not (0 <= ex_y < w and 0 <= ex_x < h):
        raise ValueError(
            f"The exit {data['exit']} is outside the maze bounds."
        )

    return {"data": data, "is_ft_printable": is_ft_printable}
