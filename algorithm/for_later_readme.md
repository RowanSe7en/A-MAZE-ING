# A-MAZE-ING 🌀

```
 █████╗       ███╗   ███╗ █████╗ ███████╗███████╗      ██╗███╗   ██╗ ██████╗
██╔══██╗      ████╗ ████║██╔══██╗╚════██║██╔════╝      ██║████╗  ██║██╔════╝
███████║█████╗██╔████╔██║███████║    ██╔╝█████╗  █████╗██║██╔██╗ ██║██║  ███╗
██╔══██║╚════╝██║╚██╔╝██║██╔══██║   ██╔╝ ██╔══╝  ╚════╝██║██║╚██╗██║██║   ██║
██║  ██║      ██║ ╚═╝ ██║██║  ██║   ██║  ███████╗      ██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝      ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝  ╚══════╝      ╚═╝╚═╝  ╚═══╝ ╚═════╝
```

> **A Python maze generator that creates, solves, and displays mazes — with a hidden "42" inside.**

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration File](#configuration-file)
- [Maze Model & Encoding](#maze-model--encoding)
- [Algorithms](#algorithms)
  - [Maze Generation](#maze-generation)
  - [Shortest Path Solving](#shortest-path-solving)
  - [Non-Perfect Mazes](#non-perfect-mazes)
- [The "42" Pattern](#the-42-pattern)
- [Output File Format](#output-file-format)
- [Algorithm Reference Table](#algorithm-reference-table)

---

## Overview

**A-MAZE-ING** is a configurable, pip-installable Python maze generator. Given a plain-text configuration file, it:

1. Parses width, height, entry/exit coordinates, and generation options
2. Generates a random maze using a **Recursive Backtracker (DFS)** algorithm
3. Optionally enforces a **perfect maze** (a spanning-tree maze with exactly one path between any two cells)
4. Embeds a hidden **"42" pattern** made of fully closed cells
5. Solves the maze using **Breadth-First Search (BFS)** to find the shortest path
6. Saves the maze to a file using a **hexadecimal wall encoding**
7. Optionally renders a **visual display** of the maze in the terminal

---

## Features

- ✅ Configurable via a simple key-value text file
- ✅ Perfect maze generation (spanning tree, no loops, no isolated cells)
- ✅ Non-perfect maze generation via braiding (adds cycles/loops)
- ✅ Guaranteed shortest path via BFS
- ✅ Compact hexadecimal wall encoding per cell
- ✅ Embedded "42" easter egg pattern
- ✅ Optional terminal visual display
- ✅ Reproducible output via random seed support
- ✅ Reusable `MazeGenerator` module
- ✅ pip-installable package

---

## Project Structure

```
a-maze-ing/
├── a_maze_ing.py       # Entry point — run this file
├── maze_generator.py   # Reusable MazeGenerator module
├── config.txt          # Example configuration file
├── setup.py            # pip-installable package setup
└── README.md
```

---

## Installation

Clone the repository and install the package:

```bash
git clone https://github.com/yourname/a-maze-ing.git
cd a-maze-ing
pip install .
```

Or install directly for development:

```bash
pip install -e .
```

---

## Usage

Run the program by passing a configuration file as the sole argument:

```bash
python3 a_maze_ing.py config.txt
```

The program will:
- Read and parse `config.txt`
- Generate the maze
- Write the output file specified in the config
- Optionally display the maze in the terminal

---

## Configuration File

The configuration file is a plain key-value text file. Lines beginning with `#` are treated as comments and ignored.

### Example `config.txt`

```ini
# A-MAZE-ING configuration file

WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=42
ALGORITHM=backtracker
DISPLAY=True
```

### Required Keys

| Key           | Description                                      |
|---------------|--------------------------------------------------|
| `WIDTH`       | Number of columns in the maze                    |
| `HEIGHT`      | Number of rows in the maze                       |
| `ENTRY`       | Starting cell coordinate, formatted as `x,y`     |
| `EXIT`        | Ending cell coordinate, formatted as `x,y`       |
| `OUTPUT_FILE` | Path to the file where the maze will be saved    |
| `PERFECT`     | `True` to generate a perfect maze, `False` for a braided one |

### Optional Keys

| Key         | Description                                                  | Default        |
|-------------|--------------------------------------------------------------|----------------|
| `SEED`      | Integer seed for reproducible random generation              | Random         |
| `ALGORITHM` | Generation algorithm to use (e.g., `backtracker`)            | `backtracker`  |
| `DISPLAY`   | `True` to render the maze visually in the terminal           | `False`        |

---

## Maze Model & Encoding

### Cell Wall Representation

Each cell in the maze has **four walls**: North, East, South, and West. These are encoded as a **4-bit integer** (0–15), where each bit represents the presence (`1`) or absence (`0`) of a wall.

```
Bit position:  3    2    1    0
Direction:     W    S    E    N
```

| Bit | Direction |
|-----|-----------|
| 0   | North     |
| 1   | East      |
| 2   | South     |
| 3   | West      |

### Wall Encoding Table

| Walls Present | Binary | Hex |
|---------------|--------|-----|
| None          | `0000` | `0` |
| North only    | `0001` | `1` |
| East only     | `0010` | `2` |
| South only    | `0100` | `4` |
| West only     | `1000` | `8` |
| All walls     | `1111` | `F` |

### Example

A cell with its West and South walls intact:

```
binary: 1100  →  hex: C
         ││
         │└── South wall present
         └─── West wall present
```

### Grid Structure

The maze is stored as a 2D list:

```python
maze[y][x] = int  # value from 0 to 15
```

At initialization, every cell starts with all four walls intact (`0xF = 15`):

```
+-----+-----+-----+-----+-----+
| 0xF | 0xF | 0xF | 0xF | 0xF |
+-----+-----+-----+-----+-----+
| 0xF | 0xF | 0xF | 0xF | 0xF |
+-----+-----+-----+-----+-----+
| 0xF | 0xF | 0xF | 0xF | 0xF |
+-----+-----+-----+-----+-----+
| 0xF | 0xF | 0xF | 0xF | 0xF |
+-----+-----+-----+-----+-----+
| 0xF | 0xF | 0xF | 0xF | 0xF |
+-----+-----+-----+-----+-----+
```

The generation algorithm progressively removes walls between adjacent cells to carve out paths.

---

## Algorithms

### Maze Generation

#### Recursive Backtracker (DFS)

The default and primary generation algorithm is the **Recursive Backtracker**, also known as the **Depth-First Search (DFS) maze generator**.

**How it works:**

```
1. Initialize all cells with all walls present (value = 0xF).
2. Create a visited grid, all set to False.
3. Start from the entry cell. Mark it as visited.
4. Randomly choose an unvisited neighbouring cell.
5. Remove the wall between the current cell and the chosen neighbour.
6. Move to the neighbour and repeat from step 4.
7. If no unvisited neighbours exist, backtrack to the previous cell.
8. Repeat until all cells have been visited.
```

**Visited grid at start:**

```
+-----+-----+-----+-----+-----+
|  F  |  F  |  F  |  F  |  F  |   F = False (unvisited)
+-----+-----+-----+-----+-----+
|  F  |  F  |  F  |  F  |  F  |
+-----+-----+-----+-----+-----+
|  F  |  F  |  F  |  F  |  F  |
+-----+-----+-----+-----+-----+
|  F  |  F  |  F  |  F  |  F  |
+-----+-----+-----+-----+-----+
|  F  |  F  |  F  |  F  |  F  |
+-----+-----+-----+-----+-----+
```

**Properties:**

| Property              | Value                                      |
|-----------------------|--------------------------------------------|
| Maze type             | Perfect maze (spanning tree)               |
| Loops                 | None                                       |
| Isolated cells        | None                                       |
| Path between any two cells | Exactly one                          |
| Graph theory model    | Spanning tree                              |

**Why this algorithm?**

- Simple to implement
- Always produces perfect mazes
- Easy to control via a random seed for reproducibility

---

### Shortest Path Solving

#### Breadth-First Search (BFS)

The shortest path from `ENTRY` to `EXIT` is computed using **BFS**, which guarantees the shortest path in an unweighted graph.

**How it works:**

```
1. Start from ENTRY. Add it to a queue.
2. Explore all accessible neighbours level by level.
3. Track each cell's parent to reconstruct the path.
4. Stop when EXIT is reached.
5. Trace back through the parent map to build the path.
```

**Path encoding:**

Each step in the path is encoded as a cardinal direction:

| Symbol | Direction |
|--------|-----------|
| `N`    | North     |
| `E`    | East      |
| `S`    | South     |
| `W`    | West      |

**Example path:** `EESSWN`

```
Start →→ ↓↓ ← ↑ → End
         (E E S S W N)
```

---

### Non-Perfect Mazes

When `PERFECT=False`, a **braided maze** is produced. This starts from a perfect maze and then removes additional walls to introduce **loops and multiple valid paths** between cells.

**Approach:**

```
1. Generate a perfect maze using the Recursive Backtracker.
2. Identify dead-end cells (cells with only one open passage).
3. Randomly remove one of their remaining walls to create a loop.
4. Repeat for a configurable number of dead ends.
```

**Result:** A maze with cycles — there will be more than one path between some pairs of cells.

| Property       | Perfect Maze         | Non-Perfect (Braided) Maze     |
|----------------|----------------------|---------------------------------|
| Loops          | None                 | Yes                             |
| Dead ends      | Many                 | Fewer                           |
| Paths          | Exactly one per pair | Multiple possible               |
| Difficulty     | Clear challenge      | Can be easier to navigate       |

---

## The "42" Pattern

Every generated maze embeds a hidden **"42"** shape made of **fully closed cells** (all four walls intact, value `0xF`).

```
Example shape of "42" embedded in maze cells:

  ████  ██████
  █  █      █
  ████      █
     █  ██████
  ████
     █  ██████
  ████      █
     █  ██████
```

These closed cells form the outline of the digits **4** and **2** within the maze grid. If the maze dimensions are too small to embed the pattern, a warning is printed and the pattern is skipped.

---

## Output File Format

The output file consists of:

1. **Maze rows** — one row per line, each cell encoded as a single hex digit
2. A blank line separator
3. **ENTRY** coordinates
4. **EXIT** coordinates
5. **PATH** — the shortest path as a direction string

### Example Output File

```
9A3F
8C21
77B0

0,0
19,14
EESSWN
```

### Format Breakdown

```
┌──────────────────────────────────┐
│  9A3F          ← row 0 of maze   │
│  8C21          ← row 1 of maze   │
│  77B0          ← row 2 of maze   │
│                ← blank line       │
│  0,0           ← ENTRY           │
│  19,14         ← EXIT            │
│  EESSWN        ← shortest PATH   │
└──────────────────────────────────┘
```

Each character in a maze row is a **hexadecimal digit (0–F)** representing the wall configuration of that cell.

---

## Algorithm Reference Table

| Purpose                  | Algorithm                    | Guarantee                    |
|--------------------------|------------------------------|------------------------------|
| Perfect maze generation  | Recursive Backtracker (DFS)  | Exactly one path per pair    |
| Perfect maze generation  | Prim's Algorithm (random)    | Exactly one path per pair    |
| Perfect maze generation  | Kruskal's Algorithm (random) | Exactly one path per pair    |
| Non-perfect maze         | Braided maze / wall removal  | Multiple paths possible      |
| Shortest path            | BFS (Breadth-First Search)   | Guaranteed shortest path     |
| Any valid path           | DFS (Depth-First Search)     | A valid path, not necessarily shortest |

> **Generation algorithms** shape the structure of the maze.
> **Solving algorithms** navigate that structure.

---

```
+--+--+--+--+--+
|     |        |
+  +--+  +--+  +
|  |     |  |  |
+  +  +--+  +  +
|     |        |
+--+--+--+--+--+
     solved! ✓
```

---

*Built with Python. Powered by graphs. Hiding 42 since the beginning.*