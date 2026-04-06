PYTHON = python3
PIP = pip3
MAIN = a_maze_ing.py
CONFIG = config.txt


all: run

run:
	$(PYTHON) $(MAIN) $(CONFIG)

debug:
	$(PYTHON) -m pdb $(MAIN) $(CONFIG)

clean:
	rm -rf __pycache__
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -f  output_maze.txt
	rm -rf algorithm/__pycache__
	rm -rf parsing/__pycache__


lint:
	python3 -m flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs --explicit-package-bases

lint-strict:
	python3 -m flake8 .
	mypy . --strict --explicit-package-bases


.PHONY: all run clean debug