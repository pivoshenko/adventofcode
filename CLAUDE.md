# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Advent of Code solutions, one language per year: **Python for 2024** (`python/src/year_2024/`), **Elixir for 2025** (`elixir/lib/year_2025/`). The two stacks share only the `data/` directory and the root `justfile`. `just` is the entry point for every task; recipes are suffixed `-py` / `-ex`, and the unsuffixed recipes (`install`, `format`, `test`, `audit`, `check`) fan out to both stacks (`lint` and `update` are Python-only).

## Commands

Run from the repository root.

```sh
just                          # list all recipes
just install                  # uv sync --all-groups --all-extras (python) + mix deps.get (elixir)
just check                    # lint + test + audit, both stacks
just format                   # pyupgrade --py313-plus + ruff format (python), mix format (elixir)
just lint                     # ruff check (ty check is commented out in lint-py)
just test                     # pytest (python) + mix test (elixir)
just update                   # uv lock --upgrade + uvx uv-upsync (python only)
```

### Python

```sh
# all tests
uv run --project python pytest python

# one day/part (tests live inside the solution file)
uv run --project python pytest python/src/year_2024/day_01/part_01.py

# run a solution against any input file
uv run --project python python/src/year_2024/day_01/part_01.py -f data/examples/year_2024/day_01.txt
```

### Elixir

```sh
# run a solution (cwd MUST be elixir/ - input paths are relative to it)
cd elixir && elixir lib/year_2025/day_01/part_01.ex

# benchmark via hyperfine (3 warm-ups); args are YEAR DAY PART, zero-padded
just run-ex 2025 01 01
just run-bench-ex 2025            # hardcoded list of solved day/part pairs - extend it when adding days
```

There is no CI; `just check` is the only gate.

## Layout

```
data/examples/year_YYYY/day_DD.txt     committed puzzle examples
data/inputs/year_YYYY/day_DD.txt       real puzzle inputs - gitignored, NOT present in a fresh clone
python/src/year_YYYY/day_DD/part_0N.py
python/src/year_YYYY/conftest.py       per-year `examples_dir` fixture
elixir/lib/year_YYYY/day_DD/part_0N.ex
```

Year, day, and part names are always zero-padded (`day_01`, `part_01`).

## Python Conventions

Every `part_0N.py` has the same shape - copy an existing day rather than inventing structure:

1. Module docstring: `"""Day N: Title (#P).` + blank line + the `https://adventofcode.com/YYYY/day/N` URL
2. `from __future__ import annotations` - enforced by `ruff.lint.isort.required-imports`
3. `def run(input_data: str) -> int` taking the whole input file contents as a string
4. `def test_run(examples_dir: pathlib.Path) -> None` asserting `run` on the example file against a hardcoded `expected_answer`
5. `if __name__ == "__main__":` block with an argparse `-f/--filepath` that reads the file and prints `run`'s answer

Testing specifics:

- No `tests/` directory. `pytest.python_files` is overridden to `["main.py", "part_01.py", "part_02.py"]` in `python/pyproject.toml`, so pytest collects the solution files directly
- `examples_dir` comes from `python/src/year_2024/conftest.py`, which walks four parents up to the repo root and returns `data/examples/year_2024`. A new Python year needs its own `conftest.py` in that year's directory

Ruff runs with `select = ["ALL"]`, `fix = true`, `unsafe-fixes = true`, `line-length = 100`, target py313 (`requires-python = ">=3.13"`), isort `force-single-line` + `length-sort-straight` (one import per line, sorted short-to-long).

## Elixir Conventions

Elixir solutions are **plain scripts, not modules** - no `defmodule`, top-level pipelines ending in `IO.inspect(answer)`. `mix.exs` exists only so `mix format` / `mix hex.audit` have a project; there are no deps and no `test/` directory, so `just test-ex` collects nothing.

Each file opens with two `#` comments (`# Day N: Title (#P)` and the puzzle URL) and hardcodes its input path:

```elixir
filepath = "../data/inputs/year_2025/day_01.txt"
```

That path is relative to `elixir/`, so a solution only runs from that cwd and only when the gitignored real input exists. Elixir solutions have no example-based tests.

## README

`README.md` carries per-year benchmark tables (hyperfine, 3 warm-ups, real puzzle input, file I/O and parsing included) linking each day's directory, plus per-year star-count badges. Adding or re-benchmarking a day means updating the matching table row and badge.

## Commits

Angular conventional commits with a stack scope: `feat(python):`, `docs(elixir):`, `chore(justfile):`, `chore(deps):`, plus unscoped `docs:` / `chore:` / `build:` for root-level changes. PRs follow `.github/PULL_REQUEST_TEMPLATE.md`.
