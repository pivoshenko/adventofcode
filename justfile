default:
    @just --list

install: install-ex install-py

install-ex:
    cd elixir && mix deps.get

install-py:
    cd python && uv sync --all-groups --all-extras

format: format-ex format-py

format-ex:
    cd elixir && mix format

format-py:
    cd python && uv run ruff check --fix .
    cd python && uv run ruff format .

lint: lint-py

lint-py:
    cd python && uv run ruff check .
    cd python && uv run ty check .

test: test-ex test-py

test-ex:
    @cd elixir && ([ -f .no-tests ] && echo "skipping (.no-tests sentinel)" || mix test)

test-py:
    @cd python && ([ -f .no-tests ] && echo "skipping (.no-tests sentinel)" || uv run pytest .)

check: lint test

update: update-py

update-py:
    cd python && uv lock --upgrade
    cd python && uvx uv-upsync

benchmark-ex-solution YEAR DAY PART:
    hyperfine --warmup 3 "cd elixir && elixir lib/year_{{ YEAR }}/day_{{ DAY }}/part_{{ PART }}.ex"

benchmark-ex-year YEAR:
    just benchmark-ex-solution {{ YEAR }} 01 01
    just benchmark-ex-solution {{ YEAR }} 01 02
    just benchmark-ex-solution {{ YEAR }} 02 01
    just benchmark-ex-solution {{ YEAR }} 02 02
    just benchmark-ex-solution {{ YEAR }} 03 01
    just benchmark-ex-solution {{ YEAR }} 03 02
    just benchmark-ex-solution {{ YEAR }} 04 01
    just benchmark-ex-solution {{ YEAR }} 04 02
    just benchmark-ex-solution {{ YEAR }} 05 01
    just benchmark-ex-solution {{ YEAR }} 06 01
    just benchmark-ex-solution {{ YEAR }} 07 01
    just benchmark-ex-solution {{ YEAR }} 08 01
    just benchmark-ex-solution {{ YEAR }} 08 02
    just benchmark-ex-solution {{ YEAR }} 09 01
    just benchmark-ex-solution {{ YEAR }} 10 01
    just benchmark-ex-solution {{ YEAR }} 11 01
    just benchmark-ex-solution {{ YEAR }} 12 01
