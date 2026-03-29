format-py:
  find python/src -type f -name '*.py' | xargs uv run --project python pyupgrade --py313-plus
  uv run --project python ruff format python

lint-py:
  uv run --project python ty check python
  uv run --project python ruff check python
  uv run --project python cz check --rev-range .

test-py:
  uv run --project python pytest python

format-ex:
  cd elixir && mix format

test-ex:
  cd elixir && mix test

run-ex YEAR DAY PART:
  hyperfine --warmup 3 "cd elixir && elixir lib/year_{{ YEAR }}/day_{{ DAY }}/part_{{ PART }}.ex"

bench-ex YEAR:
  just run-ex {{ YEAR }} 01 01
  just run-ex {{ YEAR }} 01 02
  just run-ex {{ YEAR }} 02 01
  just run-ex {{ YEAR }} 02 02
  just run-ex {{ YEAR }} 03 01
  just run-ex {{ YEAR }} 03 02
  just run-ex {{ YEAR }} 04 01
  just run-ex {{ YEAR }} 04 02
  just run-ex {{ YEAR }} 05 01
  just run-ex {{ YEAR }} 06 01
  just run-ex {{ YEAR }} 07 01
  just run-ex {{ YEAR }} 08 01
  just run-ex {{ YEAR }} 08 02
  just run-ex {{ YEAR }} 09 01
  just run-ex {{ YEAR }} 10 01
  just run-ex {{ YEAR }} 11 01
  just run-ex {{ YEAR }} 12 01
