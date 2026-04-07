*This project has been created as part of the 42 curriculum by \<login1\>[, \<login2\>].*

```
 █████╗       ███╗   ███╗ █████╗ ███████╗███████╗      ██╗███╗   ██╗  ██████╗
██╔══██╗      ████╗ ████║██╔══██╗╚══███╔╝██╔════╝      ██║████╗  ██║ ██╔════╝
███████║█████╗██╔████╔██║███████║  ███╔╝ █████╗  █████╗██║██╔██╗ ██║ ██║  ███╗
██╔══██║╚════╝██║╚██╔╝██║██╔══██║ ███╔╝  ██╔══╝  ╚════╝██║██║╚██╗██║ ██║   ██║
██║  ██║      ██║ ╚═╝ ██║██║  ██║███████╗███████╗      ██║██║ ╚████║ ╚██████╔╝
╚═╝  ╚═╝      ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝      ╚═╝╚═╝  ╚═══╝  ╚═════╝
```

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![42 School](https://img.shields.io/badge/42-School-000000?style=for-the-badge&logo=42&logoColor=white)](https://42.fr/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Finished-success?style=for-the-badge)](.)
[![Score](https://img.shields.io/badge/Score-125%2F100-gold?style=for-the-badge&logo=starship&logoColor=white)](.)

</div>

---

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Project Structure](#project-structure)
- [Instructions](#instructions)
- [Configuration File](#configuration-file)
- [Maze Generation Algorithm](#maze-generation-algorithm)
- [Maze Solving Algorithms](#maze-solving-algorithms)
- [Cell Wall Encoding](#cell-wall-encoding)
- [The Hidden "42" Easter Egg](#the-hidden-42-easter-egg)
- [Interactive Menu](#interactive-menu)
- [Themes](#themes)
- [Reusable Components](#reusable-components)
- [Advanced Features](#advanced-features)
- [Team & Project Management](#team--project-management)
- [Resources](#resources)

---

## Description

**A-MAZE-ING** is a configurable Python maze playground — a full pipeline that generates, displays, and solves mazes right in your terminal. It was built as a project for the 42 School curriculum and is designed to be both a learning tool for algorithms and graph theory, and a fun interactive experience.

Mazes have fascinated humans for thousands of years — from the legendary Labyrinth of Knossos in Greek mythology to modern puzzle games. In computer science, maze generation is a direct application of graph traversal, spanning trees, and randomness. **Perfect mazes** (with exactly one path between any two points) are mathematically equivalent to spanning trees of a grid graph — making this project a hands-on exploration of those concepts.

Feed it a config file and A-MAZE-ING will:

1. Parse your dimensions, entry/exit, and generation options.
2. Generate a maze using a **Recursive Backtracker (DFS)** algorithm.
3. Optionally produce a **perfect maze** (spanning tree) or a **braided maze** (with loops).
4. Secretly embed a **"42" pattern** made of fully enclosed cells in the center.
5. Solve it using **BFS** (shortest path) or **DFS** (any valid path).
6. Save the result in a compact **hexadecimal wall encoding**.
7. Render a **live, animated, colorful display** in your terminal with multiple themes.

> *"A labyrinth is not a place to be lost, but a path to be found."* — Anonymous

---

## Features

- ✅ Driven entirely by a simple key-value config file
- ✅ Perfect maze generation (spanning tree — no loops, no isolated cells)
- ✅ Imperfect / braided maze generation (adds loops and multiple valid paths)
- ✅ BFS solver for guaranteed shortest path
- ✅ DFS solver for an exploratory, animated path
- ✅ Compact hexadecimal wall encoding per cell
- ✅ Embedded "42" easter egg pattern (tribute to 42 School)
- ✅ Three render modes: ASCII, Emoji, and ANSI color themes
- ✅ 7 color themes: Lava, Forest, Ice, Neon, Sunset, Matrix, Party Mode
- ✅ Live animated generation and solving in the terminal
- ✅ Reproducible output via random seed support
- ✅ Reusable `MazeGenerator` module (importable in other projects)
- ✅ pip-installable package

---

## Project Structure

```text
a-maze-ing/
├── a_maze_ing.py       # Entry point — run this file
├── maze_generator.py   # Reusable MazeGenerator module
├── config.txt          # Example configuration file
├── setup.py            # pip-installable package setup
└── README.md           # This file
```

---

## Instructions

### Requirements

- Python 3.8 or higher
- No external dependencies (standard library only)

### Installation

Clone the repository and install as a pip package:

```bash
git clone https://github.com/yourname/a-maze-ing.git
cd a-maze-ing
pip install .
```

Or simply run without installing:

```bash
git clone https://github.com/yourname/a-maze-ing.git
cd a-maze-ing
python3 a_maze_ing.py config.txt
```

### Running the Program

Pass a configuration file as the sole argument:

```bash
python3 a_maze_ing.py config.txt
```

The program will:

1. Read and validate `config.txt`
2. Generate the maze (with optional live animation)
3. Solve the maze (BFS or DFS)
4. Write the output file specified in the config
5. Display the interactive menu for further exploration

### Reproducible Runs

Set `SEED=42` (or any integer) in your config file to get the exact same maze every time. Useful for sharing mazes or comparing solver outputs.

---

## Configuration File

The config is a plain `KEY=VALUE` text file. Lines starting with `#` are treated as comments and are ignored. Keys are **case-insensitive**.

### Complete Structure — Full Example `config.txt`

```ini
# A-MAZE-ING configuration file
# Lines starting with # are ignored.
# Keys are case-insensitive.

HEIGHT=17
WIDTH=19
ENTRY=0,8
EXIT=15,0
OUTPUT_FILE=maze.txt
PERFECT=False
SEED=42
SOLVE=BFS
ANIMATION=True
GENERATE_TIME=0.04
SOLVE_TIME=0.01
```

### Required Keys

| Key           | Type    | Description                                                             |
|:--------------|:--------|:------------------------------------------------------------------------|
| `WIDTH`       | Integer | Number of columns in the maze (must be ≥ 5)                             |
| `HEIGHT`      | Integer | Number of rows in the maze (must be ≥ 5)                                |
| `ENTRY`       | `x,y`   | Starting cell coordinate — must be inside maze bounds                   |
| `EXIT`        | `x,y`   | Ending cell coordinate — must differ from ENTRY                         |
| `OUTPUT_FILE` | String  | File path where the solved maze will be saved                           |
| `PERFECT`     | Bool    | `True` for a perfect maze (no loops); `False` for a braided (loopy) one |

### Optional Keys

| Key             | Default | Description                                                |
|:----------------|:--------|:-----------------------------------------------------------|
| `SEED`          | Random  | Integer seed for fully reproducible generation             |
| `SOLVE`         | `BFS`   | Solver: `BFS` (shortest path) or `DFS` (any path)         |
| `ANIMATION`     | `False` | Animate generation and solving step-by-step                |
| `GENERATE_TIME` | `0.04`  | Delay (seconds) per generation animation frame             |
| `SOLVE_TIME`    | `0.01`  | Delay (seconds) per solving animation frame                |

> Setting `ANIMATION=False` disables all delays and renders the final state instantly.

### Validation Rules

The parser validates your config before anything is generated:

- Maze dimensions must be within a valid range (minimum 5×5).
- `ENTRY` and `EXIT` must be different cells.
- Both coordinates must fall inside the maze bounds.
- Numbers, booleans, and `x,y` coordinate formats are strictly validated — invalid values produce a clear error message.
- If `ENTRY` or `EXIT` overlaps with the embedded "42" pattern, the program stops and asks you to choose different coordinates.

### Output File Format

The maze is saved as a grid of hexadecimal values — one per cell — each representing the 4-bit wall state of that cell. Value `10` (hex) marks cells belonging to the "42" pattern.

Example output (9×7 maze):

```
D 5 1 5 3 D 5 5 3
B 10 A 10 A 10 10 10 A
A 10 E 10 8 5 7 10 A
A 10 10 10 A 10 10 10 A
8 5 3 10 A 10 D 5 2
8 3 E 10 A 10 10 10 A
E C 5 5 4 5 5 5 6
```

---

## Maze Generation Algorithm

### Chosen Algorithm: Recursive Backtracker (DFS)

The maze is generated using the **Recursive Backtracker** algorithm — a randomized depth-first search on the grid:

1. Start from a random (or seeded) cell and mark it as visited.
2. While there are unvisited cells:
   - Look at the current cell's unvisited neighbors.
   - If any exist, pick one at random, remove the wall between them, and move into it (push to stack).
   - If no unvisited neighbors exist, backtrack to the previous cell (pop from stack).
3. Continue until every cell has been visited exactly once.

The result is a **spanning tree of the grid** — a perfect maze with exactly one path between any two cells, no loops, and no isolated cells.

```python
# Simplified generation logic
stack = [start_cell]
visited = {start_cell}

while stack:
    current = stack[-1]
    neighbors = get_unvisited_neighbors(current, visited)
    if neighbors:
        next_cell = random.choice(neighbors)
        remove_wall(current, next_cell)
        visited.add(next_cell)
        stack.append(next_cell)
    else:
        stack.pop()  # backtrack
```

### Why This Algorithm?

We chose the Recursive Backtracker for several reasons:

- **Simplicity:** Easy to implement correctly from scratch without any external libraries.
- **Output quality:** Produces long, winding corridors with relatively few dead ends — visually interesting and challenging to solve by hand.
- **Animation-friendly:** The DFS traversal maps directly to a satisfying carving animation in the terminal.
- **Guaranteed correctness:** Every cell is visited exactly once. The output is always a valid, connected perfect maze.
- **Clean extension point:** The perfect maze is a solid base for the braided variant — imperfect mode simply removes additional walls from the finished spanning tree.

### Imperfect / Braided Variant

After generating a perfect maze, the braided variant selectively removes extra walls to introduce loops, making the maze less predictable and more natural. Safety constraints are applied to prevent large open areas:

- Edge cells always retain at least 2 walls.
- Interior cells always retain at least 1 wall.
- A 6-cell directional scan ensures corridors stay tight and readable.

---

## Maze Solving Algorithms

### BFS (Breadth-First Search)

Explores the maze level by level using a queue (`collections.deque`). Guarantees the **shortest path** from entry to exit. Parent cells are stored during traversal to reconstruct the full solution path, encoded as N/E/S/W direction symbols.

Best for: finding the optimal solution with minimum steps.

### DFS (Depth-First Search)

Explores the maze using a stack. Finds **any valid path** — not necessarily the shortest. Neighbor selection is randomized, so each run may produce a different valid solution. Looks spectacular when animated because it explores deeply before backtracking.

Best for: animated visualizations and exploratory solving.

---

## Cell Wall Encoding

Every cell stores its four walls as a **4-bit integer**:

```
Bit:  3    2    1    0
Dir:  W    S    E    N
```

| Walls Present | Binary  | Hex  |
|:--------------|:--------|:-----|
| None          | `0000`  | `0`  |
| North only    | `0001`  | `1`  |
| East only     | `0010`  | `2`  |
| South only    | `0100`  | `4`  |
| West only     | `1000`  | `8`  |
| All walls     | `1111`  | `F`  |
| "42" cell     | `10000` | `10` |

Every cell starts fully walled (`0xF = 15`). Generation progressively clears bits to carve paths. The value `16` (`0x10`) is reserved for cells that belong to the "42" easter egg and are never modified by the generation algorithm.

---

## The Hidden "42" Easter Egg

A "42" digit pattern is carved at the center of every maze using cells marked with value `16`. This region is **protected throughout generation** — no walls are ever removed inside it, and `ENTRY`/`EXIT` coordinates cannot be placed within its bounds.

During rendering, "42" cells are drawn with a dedicated color or emoji (🟦) to make the digits visible while remaining structurally embedded in the maze.

### The Rendering Challenge and Fix

The maze renderer was originally cell-centric: each cell is drawn independently, treating its walls and content without awareness of neighboring cells. This caused adjacent "42" cells to appear fragmented — separated by wall artifacts that broke the shape of the digits.

**Before fix — broken digits:**
```
⬛⬜⬛🟦⬛⬜⬛🟦⬛  ⬛🟦⬛🟦⬛🟦⬛⬜⬛
```

**After fix — solid, connected digits:**
```
⬛⬜⬛🟦⬛⬜⬛🟦⬛  ⬛🟦🟦🟦🟦🟦⬛⬜⬛
```

The fix introduced **context-aware rendering**: before drawing a "42" cell, the renderer checks if its neighbors are also "42" cells. If so, the shared boundary between them is suppressed, making the digits read as solid, continuous shapes.

This introduced a second semantic layer on top of the maze geometry:

- **Layer 1** — Maze topology (walls and paths)
- **Layer 2** — Visual pattern (the "42" shape)

Layer 2 takes rendering priority when the two conflict.

---

## Interactive Menu

After generation and solving, the program enters an interactive loop — no need to restart between runs:

```
  ┌──────────────────────────────┐
  │         A-MAZE-ING           │
  │                              │
  │  1. Generate a new maze      │
  │  2. Toggle solution path     │
  │  3. Change color theme       │
  │  4. Quit                     │
  │                              │
  │  Press ENTER to exit         │
  └──────────────────────────────┘
```

| Option | Action                                                            |
|:-------|:------------------------------------------------------------------|
| **1**  | Generate a brand new maze using current config                    |
| **2**  | Toggle visibility of solved path (maze data is never modified)    |
| **3**  | Open theme selector                                               |
| **4**  | Exit cleanly                                                      |

Invalid input displays a clear error message. `Ctrl+C` or pressing `ENTER` exits gracefully.

---

## Themes

Option **3** opens the theme selector. Themes apply ANSI colors to walls, floors, paths, entry/exit markers, and the "42" pattern.

| ID | Theme      | Vibe                                        |
|:---|:-----------|:--------------------------------------------|
| 1  | Lava       | Deep reds and molten orange paths           |
| 2  | Forest     | Earthy greens and natural tones             |
| 3  | Ice        | Cool blues and frosty whites                |
| 4  | Neon       | Electric colors on a dark field             |
| 5  | Sunset     | Warm purples, pinks, and golds              |
| 6  | Matrix     | Classic green-on-black terminal             |
| 7  | Party Mode | Random theme on every render 🎉             |

ASCII and Emoji render modes work on any terminal with no ANSI support required.

---

## Reusable Components

### `MazeGenerator` module (`maze_generator.py`)

The core maze logic is fully decoupled from the display, CLI, and config layers and lives in a self-contained module. It has no external dependencies and can be dropped into any Python project.

**How to use it:**

```python
from maze_generator import MazeGenerator

# Create a generator
gen = MazeGenerator(width=19, height=17, seed=42, perfect=True)

# Generate the maze — returns a 2D list of integers
maze = gen.generate()

# Solve the maze — returns a list of (x, y) coordinate tuples
path = gen.solve(method="BFS")   # or "DFS"

# Serialize to hex for saving
hex_output = gen.to_hex()
```

**Public API:**

| Method / Attribute | Description                                              |
|:-------------------|:---------------------------------------------------------|
| `generate()`       | Run DFS generation algorithm; return 2D list of integers |
| `solve(method=)`   | Solve with `"BFS"` or `"DFS"`; return path as coordinates|
| `maze`             | The raw 2D grid (list of lists of int)                   |
| `entry`, `exit`    | Coordinates of entry and exit cells                      |
| `to_hex()`         | Serialize maze to a hex string for file output           |

**What makes it reusable:**
- No imports from display, config, or CLI modules — zero coupling.
- Copy `maze_generator.py` into any Python project and import immediately.
- Use `generate()` to get a raw grid you can render however you want.
- Use `to_hex()` to save the maze; parse the hex values back in to reload it.

---

## Advanced Features

### Multiple Render Modes

Three distinct render modes are available:

- **ASCII** — uses `+`, `-`, `|`, and space characters. Compatible with every terminal.
- **Emoji** — uses block emojis (⬛, ⬜, 🟩, 🟦, 🟪) for a pixel-art style display.
- **ANSI Color** — applies colored terminal backgrounds via escape codes. Pairs with any theme.

### Animated Generation and Solving

When `ANIMATION=True`, every step of the DFS carving and BFS/DFS solving is rendered in real time. `GENERATE_TIME` and `SOLVE_TIME` control the frame delay independently.

### Hexadecimal Maze Serialization

The output file stores wall states as hex values — compact, human-readable, and easy to version-control or compare between runs.

### Reproducible Mazes

Any maze can be reproduced exactly by preserving the config file with its `SEED` value. Useful for sharing puzzles with peers or running the same maze through multiple solvers.

---

## Team & Project Management

### Team Members and Roles

| Member      | Responsibilities                                                          |
|:------------|:--------------------------------------------------------------------------|
| `<login1>`  | Maze generation algorithm, 4-bit wall encoding, config parser, validation |
| `<login2>`  | BFS/DFS solvers, path reconstruction, output file serialization           |

*(Replace with actual logins and real responsibilities.)*

### Planning and How It Evolved

**Initial plan:**
- Week 1: Config parser, DFS generation, ASCII rendering.
- Week 2: BFS solver, hex output, basic theming.
- Week 3: Animation, braided maze, "42" easter egg.

**How it actually went:**

Config parsing took longer than anticipated due to edge-case validation (coordinate bounds, "42" overlap, type checking). The "42" rendering fragmentation was an unexpected problem — the cell-centric renderer had to be retrofitted with neighbor-awareness, which cost time but resulted in a cleaner architecture overall. Animation was easier than expected once the rendering loop was in place. The DFS solver was added late as a bonus after BFS was confirmed working.

The final scope matched the original plan closely. The main deviations were extra time on rendering correctness and the addition of the interactive menu, which was not originally planned but significantly improved usability.

### What Worked Well

- Decoupling `MazeGenerator` from the display layer early made debugging much easier — generation and solving could be tested in isolation.
- Using a seed from day one made every bug reproducible — any crash could be rerun exactly.
- The 4-bit wall encoding was the right abstraction: generation, solving, and rendering all operated on the same representation with no conversion needed.
- Peer code reviews caught the "42" fragmentation bug and the config validation gap early.

### What Could Be Improved

- The config parser could be more forgiving (e.g., allow `True`, `true`, and `TRUE` without explicit normalization).
- Adding a second generation algorithm (Prim's, Wilson's, or Eller's) would make the `MazeGenerator` module significantly more versatile.
- The interactive menu could support loading a different config file at runtime.
- Unit tests for the generation and solving logic would improve confidence during refactoring.

### Tools Used

| Tool             | Purpose                                                        |
|:-----------------|:---------------------------------------------------------------|
| Python 3.10      | Primary implementation language                               |
| Git / GitHub     | Version control, branching, and code review                   |
| VS Code          | Main editor (both members)                                    |
| Terminal (iTerm2)| Testing emoji and ANSI rendering behavior                     |
| ChatGPT / Claude | Debugging assistance and documentation drafting (see below)   |

---

## Resources

### Algorithm References

- [Maze Generation Algorithms — Jamis Buck](https://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracker) — the definitive reference for the recursive backtracker and related maze algorithms.
- [Breadth-First Search — Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Depth-First Search — Wikipedia](https://en.wikipedia.org/wiki/Depth-first_search)
- [Spanning Tree — Wikipedia](https://en.wikipedia.org/wiki/Spanning_tree) — explains the mathematical link between perfect mazes and spanning trees.
- [Prim's Maze Generation — Jamis Buck](https://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm)
- [Maze Classification — Think Labyrinth](http://www.astrolog.org/labyrnth/algrithm.htm) — overview of perfect vs. imperfect mazes and practical generation approaches.

### Python Documentation

- [Python 3 Standard Library](https://docs.python.org/3/library/)
- [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) — used for the BFS queue.
- [random module](https://docs.python.org/3/library/random.html) — seeded generation and neighbor selection.
- [ANSI Escape Codes — Wikipedia](https://en.wikipedia.org/wiki/ANSI_escape_code) — terminal color rendering reference.

### Books

- *Introduction to Algorithms* (Cormen, Leiserson, Rivest, Stein) — Chapter on graph traversal (BFS and DFS).

### AI Usage

AI tools (ChatGPT and Claude) were used in the following specific ways:

| Task | How AI was used |
|:-----|:----------------|
| ANSI escape code syntax | Queried AI for correct format; tested across multiple terminals |
| Config validation edge cases | Discussed coordinate overlap detection logic with AI; implementation was written independently |

All AI-generated content was critically reviewed and tested against the actual codebase. No code was copied without being fully understood. AI was used as a productivity tool, never as a substitute for understanding.

---

> *Every maze is unique. Every path is yours to find. Happy exploring!* 🌀
