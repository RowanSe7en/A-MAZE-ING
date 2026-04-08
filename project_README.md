*This project has been created as part of the 42 curriculum by [brouane], [bamrbouh].*

---

## Description

**A-MAZE-ING** is a configurable Python maze generator and solver. Feed it a plain-text config file and it will generate a random maze using a **Recursive Backtracker (DFS)** algorithm, optionally solve it with **BFS** (shortest path) or **DFS** (exploratory path), and render everything live in your terminal — with ANSI color themes.

Every maze embeds a **"42" pattern** at its center as a tribute to 42 School. The pattern is planted before generation begins, so the maze always adapts around it rather than overwriting it.

Key capabilities:
- Perfect maze generation (spanning tree — exactly one path between any two cells)
- Imperfect / braided maze generation (adds loops and multiple valid paths)
- BFS solver for the guaranteed shortest path; DFS solver for an animated exploratory path
- Compact hexadecimal wall encoding per cell
- Live animated generation and solving in the terminal
- Reproducible output via random seed support
- A reusable `MazeGenerator` module usable in other projects
- pip-installable package

---

## Instructions

```bash
python3 a_maze_ing.py config.txt
```

The program reads `config.txt`, generates the maze, writes the output file specified in the config, and optionally displays the maze in the terminal.

**Project structure:**

```
a-maze-ing/
├── a_maze_ing.py       # Entry point — run this file
├── maze_generator.py   # Reusable MazeGenerator module
├── config.txt          # Example configuration file
├── setup.py            # pip-installable package setup
└── README.md           # Documentation
```

---

## Configuration File

The config is a plain `KEY=VALUE` text file. Lines starting with `#` are comments and are ignored. Keys are **case-insensitive**.

**Example `config.txt`:**

```ini
# A-MAZE-ING configuration file

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

**Required keys:**

| Key | Description |
| :--- | :--- |
| `WIDTH` | Number of columns in the maze |
| `HEIGHT` | Number of rows in the maze |
| `ENTRY` | Starting cell coordinate as `x,y` |
| `EXIT` | Ending cell coordinate as `x,y` |
| `OUTPUT_FILE` | Path where the maze will be saved |
| `PERFECT` | `True` for a perfect maze; `False` for a braided (loopy) one |

**Optional keys:**

| Key | Default | Description |
| :--- | :--- | :--- |
| `SEED` | Random | Integer seed for reproducible generation |
| `SOLVE` | `BFS` | Solver: `BFS` (shortest path) or `DFS` (any path) |
| `ANIMATION` | `False` | Enable step-by-step animated generation/solving |
| `GENERATE_TIME` | `0.04` | Delay (seconds) between generation animation frames |
| `SOLVE_TIME` | `0.01` | Delay (seconds) between solving animation frames |

The parser validates the config before anything is generated: dimensions must be within a reasonable range, entry and exit must be different cells and fall inside the maze bounds, and if either coordinate overlaps the embedded "42" pattern, the program stops and asks for new coordinates.

---

## Maze Generation Algorithm

### Chosen Algorithm: Recursive Backtracker (DFS)

The default generation algorithm is the **Recursive Backtracker**, also known as a randomized depth-first search.

**How it works:**
1. Initialize all cells with all four walls (`0xF`).
2. Start from `ENTRY`. Mark it as visited.
3. Randomly pick an unvisited neighbor.
4. Remove the wall between the current cell and the chosen neighbor.
5. Move to the neighbor and repeat from step 3.
6. If no unvisited neighbors exist, backtrack up the stack.
7. Repeat until every cell has been visited.

The result is a **perfect maze** — a spanning tree where exactly one path exists between any two cells.

### Why This Algorithm?

The Recursive Backtracker was chosen for three reasons:

- **Simplicity:** The algorithm maps directly to a DFS traversal, making the code clean and easy to reason about.
- **Visual quality:** It produces long, winding corridors with relatively few dead ends, which makes for satisfying animated generation and interesting mazes to solve.
- **Flexibility as a base:** It generates a valid spanning tree that can then be augmented — by randomly removing additional walls — to produce imperfect (braided) mazes with loops. This makes one algorithm serve both the `PERFECT=True` and `PERFECT=False` modes.

### Imperfect (Braided) Maze Mode

When `PERFECT=False`, the program first generates a perfect maze using the Recursive Backtracker, then performs a second pass that removes additional walls between cells, introducing loops and multiple valid paths. A multi-layer safety check prevents large open areas from forming: edge cells must keep at least two walls, interior cells must keep at least one wall, and a 6-cell directional scan blocks any long open corridor strips from being created.

---


**Cell wall encoding:**

```
Bit:  3    2    1    0
Dir:  W    S    E    N
```

A cell with its West and South walls intact encodes as `binary 1100 → hex C`.

---

## Reusable Components

The `maze_generator.py` file is designed as a **standalone, reusable module**. It exposes the `MazeGenerator` class, which handles:

- Maze initialization and wall encoding
- Perfect maze generation (Recursive Backtracker)
- Imperfect maze generation (braided mode)
- BFS and DFS solving
- The "42" pattern embedding

To reuse it in another project, simply import the class and instantiate it with a width, height, entry, and exit:

```python
from maze_generator import MazeGenerator

mg = MazeGenerator(width=19, height=17, entry=(0, 8), exit_=(15, 0))
mg.generate()
path = mg.solve_bfs()
```

No external dependencies are required. The module is also pip-installable via `setup.py`, so it can be added to any Python project as a package.

---

## Advanced Features

### Interactive Menu

After the maze is generated, the program enters an interactive loop — no need to restart between runs:

| Option | Action |
| :--- | :--- |
| **1** | Generate a new maze |
| **2** | Toggle solved path visibility |
| **3** | Change color theme |
| **4** | Quit |

### Themes

Option 3 opens a theme selector. Available themes:

| ID | Theme | Vibe |
| :--- | :--- | :--- |
| 1 | Lava | Deep reds and molten orange paths |
| 2 | Forest | Earthy greens and natural tones |
| 3 | Ice | Cool blues and frosty whites |
| 4 | Neon | Electric colors on a dark field |
| 5 | Sunset | Warm purples, pinks, and golds |
| 6 | Matrix | Classic green-on-black terminal |
| 7 | Party Mode | Random theme on every render 🎉 |

### Display Modes

- **ASCII:** Classic `+---+` walls and `|` dividers, path shown as `.`, entry as `S`, exit as `E`.
- **Emoji:** Walls as `⬛`, floor as `⬜`, path as `🟩`, entry/exit as `🟦`/`🟪`.
- **ANSI Color:** Same geometry as emoji mode but using colored terminal blocks with full theme support.

---

## Team and Project Management

### Roles

| Member     | Role                                                 |
| :--------- | :--------------------------------------------------- |
| [brouane]  | *generated and solved algorithms, handled rendering* |
| [bmarbouh] | *implemented parsing and interactive menus*          |


### Planning

We initially started by implementing the parsing system to handle inputs and configuration. Next, we worked on the core algorithms for generating and solving the mazes. After some progress, we began integrating the parsing with the algorithms so both could interact smoothly. Once the core functionality was stable, we added interactive menus, visual themes, and all remaining features to polish the user experience. 

### What Worked Well and What Could Be Improved

**What worked well:**

* *Parsing and input handling worked perfectly, allowing flexible configuration.*
* *The core algorithms (BFS and DFS) reliably solved both perfect and imperfect mazes.*
* *Output routines correctly displayed solutions and maze structures.*

**What could be improved:**

* *The hex-based map printing could be simplified and made more consistent.*
* *The structure of the code is somewhat messy with many imports; organizing modules would improve readability and maintainability.*
* *Handling of imperfect mazes could be more systematic, rather than relying on ad-hoc heuristics.*

### Tools Used

* **Python 3.8+** — sole language and runtime
* **Git** — version control and collaboration
* **draw.io** — designing flowcharts and maze structures

---

## Resources

**Documentation and references:**
- [Maze generation algorithms — Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Recursive backtracker (DFS maze) — Jamis Buck's blog](https://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracker)
- [Breadth-First Search — Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Spanning tree and perfect mazes — Buckblog](https://weblog.jamisbuck.org/2011/1/27/maze-generation-growing-tree-algorithm)
- [Python `collections.deque` for BFS queues](https://docs.python.org/3/library/collections.html#collections.deque)
- [ANSI escape codes reference](https://en.wikipedia.org/wiki/ANSI_escape_code)

**AI usage:**

AI (Claude / ChatGPT) was used in the following ways during this project:

- **Explaining algorithm choices:** AI was consulted to compare the properties of Recursive Backtracker, Prim's, and Kruskal's algorithms in order to make an informed decision about which suited this project best.
- **Writing and formatting the README:** AI assisted in structuring and drafting documentation sections.

AI was not used to write core maze generation, solving, or rendering logic — all algorithmic code was written by the team.