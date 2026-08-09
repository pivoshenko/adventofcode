# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Advent of Code solutions, one language per year: **Python for 2024** (`python/`), **Elixir for 2025** (`elixir/`). The two stacks share nothing but the `data/` directory and the root `justfile`. `just` is the single entry point for every task; recipes are suffixed `-py` / `-ex` and the unsuffixed ones fan out to both.

## Commands

Run from the repository root.

```sh
just                          # list all recipes
just install                  # uv sync (python) + mix deps.get (elixir)
just check                    # lint + test + audit, both stacks
just format                   # pyupgrade --py313-plus + ruff format, mix format
just lint                     # ruff check (ty is commented out in lint-py)
just test                     # pytest + mix test
just update                   # uv lock --upgrade + uvx uv-upsync
```

### Python

```sh
# all tests
uv run --project python pytest python

# one day/part
uv run --project python pytest python/src/year_2024/day_01/part_01.py

# run a solution against any input file
uv run --project python python/src/year_2024/day_01/part_01.py -f data/examples/year_2024/day_01.txt
```

### Elixir

```sh
# run a solution (cwd MUST be elixir/ — input paths are relative to it)
cd elixir && elixir lib/year_2025/day_01/part_01.ex

# benchmark via hyperfine (3 warm-ups); args are YEAR DAY PART, zero-padded
just run-ex 2025 01 01
just bench-ex 2025            # hardcoded list of solved day/part pairs — extend when adding days
```

## Layout

```
data/examples/year_YYYY/day_DD.txt   committed puzzle examples
data/inputs/                         real puzzle inputs — gitignored, NOT present in a fresh clone
python/src/year_YYYY/day_DD/part_0N.py
python/src/year_YYYY/conftest.py     per-year `examples_dir` fixture
elixir/lib/year_YYYY/day_DD/part_0N.ex
```

Day and part directories/files are always zero-padded (`day_01`, `part_01`).

## Python conventions

Every `part_0N.py` follows the same four-block shape — copy an existing day rather than inventing structure:

1. Module docstring: `"""Day N: Title (#P).` + blank line + the `https://adventofcode.com/YYYY/day/N` URL.
2. `from __future__ import annotations` — enforced by `ruff.lint.isort.required-imports`.
3. `def run(input_data: str) -> int` taking the whole file contents as a string.
4. `def test_run(examples_dir: pathlib.Path) -> None` asserting against a hardcoded `expected_answer` from the example file, then an `if __name__ == "__main__":` block with an argparse `-f/--filepath`.

Testing specifics:

- There is no `tests/` directory. Tests live inside the solution files; `pytest.python_files` is overridden to `["main.py", "part_01.py", "part_02.py"]`, so pytest collects solutions directly.
- `examples_dir` comes from `python/src/year_2024/conftest.py`, which walks four parents up to the repo root. Adding a new Python year requires a new `conftest.py` in that year's directory.
- pytest rootdir is `python/` (config lives in `python/pyproject.toml`), but `run` invocations above are relative to the repo root.

Ruff runs with `select = ["ALL"]`, `fix = true`, `unsafe-fixes = true`, `line-length = 100`, isort `force-single-line` + `length-sort-straight` (imports are sorted short-to-long, one per line). Target is py313; `requires-python = ">=3.13"`.

## Elixir conventions

Elixir solutions are **plain scripts, not modules** — no `defmodule`, no `Mix` application code, top-level pipelines ending in `IO.inspect(answer)`. `mix.exs` exists only to give `mix format` / `mix hex.audit` a project; there are no deps and no `test/` directory, so `just test-ex` collects nothing.

Each file opens with two `#` comments (`# Day N: Title (#P)` and the puzzle URL) and hardcodes its input:

```elixir
filepath = "../data/inputs/year_2025/day_01.txt"
```

That path is relative to `elixir/`, so a solution only runs with that cwd and only when the gitignored real input exists. Elixir solutions have no example-based tests.

## README

`README.md` carries per-year benchmark tables (hyperfine, 3 warm-ups, real input, I/O and parsing included) linking each day's directory, plus star-count badges. Adding or benchmarking a day means updating the matching row and badge.

## Commits

Angular conventional commits with a stack scope: `feat(python):`, `docs(elixir):`, `chore(justfile):`, plus unscoped `docs:` / `chore:` for root-level changes.
