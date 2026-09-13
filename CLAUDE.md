# CLAUDE.md

## Overview

Personal [Advent of Code](https://adventofcode.com) solutions. Two independent stacks live side by side, one per puzzle year: `python/` managed by `uv`, `elixir/` managed by `mix`. No shared library, no framework, no cross-stack code. Each puzzle part is a standalone file that reads an input file and prints one answer. The only thing both stacks share is `data/`.

`just` is the task runner - `just --list` and `CONTRIBUTING.md` carry the full recipe table. `AGENTS.md` is a symlink to this file.

## Read This First

- **real inputs cannot be fetched.** `data/inputs/` is gitignored, AoC serves inputs only behind a session cookie, and there is no download recipe here. Ask for the file, or work from `data/examples/`. Never commit an input
- **`just test-ex` runs every Elixir solution.** There is no `test/` directory, but `mix test` compiles `lib/**/*.ex` first, and those files are top-level scripts, so compiling them *executes* them. Without `data/inputs/` the compile aborts with `** (File.Error) could not read file "../data/inputs/year_2025/day_01.txt"` before any test collection. With the inputs present it runs every solved part, then reports `There are no tests to run`
- **therefore `just check` cannot pass on a checkout without inputs** - it is `lint` then `test`, and `test` reaches `test-ex`. `just lint` and `just test-py` are the parts that run anywhere
- **Elixir solutions must be run from inside `elixir/`** - the input path is hardcoded relative to that directory

## Running Things

```bash
uv run --project python python/src/year_2024/day_01/part_01.py -f data/inputs/year_2024/day_01.txt  # one Python solution, from the repository root
uv run --project python pytest python/src/year_2024/day_07/part_02.py                               # one Python test
cd elixir && elixir lib/year_2025/day_01/part_01.ex                                                 # one Elixir solution
```

`just benchmark-ex-solution YEAR DAY PART` takes zero-padded arguments, e.g. `2025 01 02`.

## Layout

```
data/examples/year_<YYYY>/day_<DD>.txt   committed puzzle examples
data/inputs/year_<YYYY>/day_<DD>.txt     real puzzle inputs, gitignored
python/src/year_2024/day_<DD>/part_<PP>.py
elixir/lib/year_2025/day_<DD>/part_<PP>.ex
```

Day and part numbers are always zero-padded to two digits. A day directory holding only a `.todo` file is unsolved; a day with `part_01` and no `part_02` means part two is unsolved.

## Solution Shape

### Python

Every `part_<PP>.py` has the same four sections, in order:

1. a module docstring naming and linking the puzzle, e.g. `"""Day 7: Bridge Repair (#2).` followed by `https://adventofcode.com/2024/day/7`
2. `run(input_data: str) -> int` taking the whole file contents as one string and returning the answer, plus any helpers it needs
3. `test_run(examples_dir: pathlib.Path) -> None` asserting `run` over `data/examples/` returns the expected answer
4. an `if __name__ == "__main__":` block with an `argparse` parser taking a required `-f/--filepath`, which reads that file and prints `run`'s result

Tests are colocated with the solutions rather than in a `tests/` tree: `python_files` in `python/pyproject.toml` is set so pytest collects the solution files themselves. The `examples_dir` fixture comes from `python/src/year_2024/conftest.py` - **a new year needs its own `conftest.py`**.

### Elixir

Each `part_<PP>.ex` is top-level script code rather than a module wrapper - `elixir <file>` evaluates it directly. Some parts also define a helper module alongside that script code. The shape is:

1. two leading comments naming and linking the puzzle
2. `filepath = "../data/inputs/year_2025/day_<DD>.txt"` - relative to `elixir/`, which is why the run must happen from there
3. a pipeline from `File.read!` through parsing to the answer
4. `IO.inspect(answer)`

Elixir solutions read the real input only. They have no example-based test path, unlike the Python ones.

## When A Solution Lands

Two files outside the solution need updating:

- `README.md` - the benchmark row for that day/part, and the star badge for the year. Numbers come from `just benchmark-ex-*` (3 warm-ups, file I/O and parsing included, real input not the example)
- `justfile` - `benchmark-ex-year` is a hardcoded list of `benchmark-ex-solution` calls, one per solved part, so a new part is not benchmarked until a line is added

There are no GitHub Actions workflows; `just check` locally is the whole CI story. Commits and branches follow `CONTRIBUTING.md`.
