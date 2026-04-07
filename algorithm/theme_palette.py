from typing import Dict

themes: Dict[str, Dict[str, str]] = {
    "ash_lava": {  # Original — unchanged
        "wall_color": "\033[40m  \033[0m",
        "road_color": "\033[100m  \033[0m",
        "path_color": "\033[103m  \033[0m",
        "entery_color": "\033[101m  \033[0m",
        "exit_color": "\033[105m  \033[0m",
        "ft_pattern": "\033[101m  \033[0m",
    },
    "deep_ocean": {
        "wall_color": "\033[48;5;17m  \033[0m",   # Near-black navy
        "road_color": "\033[48;5;24m  \033[0m",   # Deep ocean blue
        "path_color": "\033[48;5;31m  \033[0m",   # Mid ocean teal
        "entery_color": "\033[48;5;44m  \033[0m",   # Bioluminescent cyan
        "exit_color": "\033[48;5;87m  \033[0m",   # Electric aqua
        "ft_pattern": "\033[48;5;44m  \033[0m",   # Bioluminescent glow
    },
    "sakura": {
        "wall_color": "\033[48;5;52m  \033[0m",   # Deep plum
        "road_color": "\033[48;5;96m  \033[0m",   # Dusty mauve
        "path_color": "\033[48;5;217m  \033[0m",  # Soft cherry blossom
        "entery_color": "\033[48;5;218m  \033[0m",  # Warm petal pink
        "exit_color": "\033[48;5;231m  \033[0m",  # Petal white
        "ft_pattern": "\033[48;5;211m  \033[0m",  # Vivid blossom
    },
    "crimson_void": {
        # near-black with red hint (void background)
        "wall_color": "\033[48;5;232m  \033[0m",

        # very dark dried-blood red (maze floor)
        "road_color": "\033[48;5;124m  \033[0m",

        # rich crimson path (main route)
        "path_color": "\033[48;5;214m  \033[0m",

        # bright blood-red entry (strong contrast)
        "entery_color": "\033[48;5;160m  \033[0m",

        # glowing hell-red / neon exit (final goal pop)
        "exit_color": "\033[48;5;196m  \033[0m",

        # trail footprint slightly darker than entry
        "ft_pattern": "\033[48;5;196m  \033[0m",
    },
    "toxic_jungle": {
        "wall_color": "\033[48;5;232m  \033[0m",  # Pitch black
        "road_color": "\033[48;5;22m  \033[0m",   # Dark toxic green
        "path_color": "\033[48;5;34m  \033[0m",
        "entery_color": "\033[48;5;46m  \033[0m",   # Radioactive green entry
        "exit_color": "\033[48;5;190m  \033[0m",  # Toxic lime exit
        "ft_pattern": "\033[48;5;46m  \033[0m",   # Neon green trail
    },
    "sandstorm": {
        "wall_color": "\033[48;5;52m  \033[0m",   # Dark desert rock
        "road_color": "\033[48;5;94m  \033[0m",   # Dry sand brown
        "path_color": "\033[48;5;179m  \033[0m",  # Golden sand
        "entery_color": "\033[48;5;214m  \033[0m",  # Warm amber dune
        "exit_color": "\033[48;5;202m  \033[0m",  # Dusk orange
        "ft_pattern": "\033[48;5;214m  \033[0m",  # Amber footprint
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
