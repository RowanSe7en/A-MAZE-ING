from typing import Dict

themes: Dict[str, Dict[str, str]] = {
    "ash_lava": {
        "wall_color": "\033[40m  \033[0m",
        "road_color": "\033[100m  \033[0m",
        "path_color": "\033[103m  \033[0m",
        "entery_color": "\033[101m  \033[0m",
        "exit_color": "\033[105m  \033[0m",
        "ft_pattern": "\033[101m  \033[0m",
    },
    "deep_ocean": {
        "wall_color": "\033[48;5;17m  \033[0m",
        "road_color": "\033[48;5;24m  \033[0m",
        "path_color": "\033[48;5;31m  \033[0m",
        "entery_color": "\033[48;5;44m  \033[0m",
        "exit_color": "\033[48;5;87m  \033[0m",
        "ft_pattern": "\033[48;5;44m  \033[0m",
    },
    "sakura": {
        "wall_color": "\033[48;5;52m  \033[0m",
        "road_color": "\033[48;5;96m  \033[0m",
        "path_color": "\033[48;5;217m  \033[0m",
        "entery_color": "\033[48;5;218m  \033[0m",
        "exit_color": "\033[48;5;231m  \033[0m",
        "ft_pattern": "\033[48;5;211m  \033[0m",
    },
    "crimson_void": {
        "wall_color": "\033[48;5;232m  \033[0m",
        "road_color": "\033[48;5;124m  \033[0m",
        "path_color": "\033[48;5;214m  \033[0m",
        "entery_color": "\033[48;5;160m  \033[0m",
        "exit_color": "\033[48;5;196m  \033[0m",
        "ft_pattern": "\033[48;5;196m  \033[0m",
    },
    "toxic_jungle": {
        "wall_color": "\033[48;5;232m  \033[0m",
        "road_color": "\033[48;5;22m  \033[0m",
        "path_color": "\033[48;5;34m  \033[0m",
        "entery_color": "\033[48;5;46m  \033[0m",
        "exit_color": "\033[48;5;190m  \033[0m",
        "ft_pattern": "\033[48;5;46m  \033[0m",
    },
    "sandstorm": {
        "wall_color": "\033[48;5;52m  \033[0m",
        "road_color": "\033[48;5;94m  \033[0m",
        "path_color": "\033[48;5;179m  \033[0m",
        "entery_color": "\033[48;5;214m  \033[0m",
        "exit_color": "\033[48;5;202m  \033[0m",
        "ft_pattern": "\033[48;5;214m  \033[0m",
    },
    "cotton_candy": {
        "wall_color": "\033[48;5;54m  \033[0m",
        "road_color": "\033[48;5;141m  \033[0m",
        "path_color": "\033[48;5;198m  \033[0m",
        "entery_color": "\033[48;5;212m  \033[0m",
        "exit_color": "\033[48;5;219m  \033[0m",
        "ft_pattern": "\033[48;5;199m  \033[0m",
    },
}

theme_mapper: Dict[str, str] = {
    "1": "ash_lava",
    "2": "deep_ocean",
    "3": "sakura",
    "4": "crimson_void",
    "5": "toxic_jungle",
    "6": "sandstorm",
    "7": "cotton_candy",
    "8": ""
}
