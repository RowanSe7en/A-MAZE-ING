PYTHON = python3
MAIN = a_maze_ing.py
CONFIG = config.txt
VENV_NAME := $(shell python3 -c "import os,sys; print(os.path.basename(sys.prefix))")

all: run

run:
	$(PYTHON) $(MAIN) $(CONFIG)

install:
	pip install dist/mazegen-1.0.0-py3-none-any.whl

debug:
	$(PYTHON) -m pdb $(MAIN) $(CONFIG)

clean:
	rm -rf __pycache__
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -f  output_maze.txt
	rm -rf parsing/__pycache__
	rm -rf mazegen/__pycache__
	rm -rf algorithm/__pycache__

lint:
	python3 -m flake8 . --exclude=$(VENV_NAME)
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs --explicit-package-bases

lint-strict:
	python3 -m flake8 . --exclude=$(VENV_NAME)
	mypy . --strict --explicit-package-bases


.PHONY: all run clean debug lint lint-strict