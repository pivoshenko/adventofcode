# Day 7: Laboratories (#1).
# https://adventofcode.com/2025/day/7

filepath = "../data/inputs/year_2025/day_07.txt"

content =
  filepath
  |> File.read!()
  |> String.split("\n", trim: true)

grid =
  content
  |> Enum.with_index()
  |> Enum.flat_map(fn {line, row} ->
    line
    |> String.graphemes()
    |> Enum.with_index()
    |> Enum.map(fn {char, column} -> {{row, column}, char} end)
  end)
  |> Map.new()

{start_row, start_column} =
  grid
  |> Enum.find(fn {_pos, char} -> char == "S" end)
  |> elem(0)

max_row = length(content) - 1

defmodule Simulator do
  def simulate(beams, _grid, _max_row, splits) when beams == [] do
    splits
  end

  def simulate(beams, grid, max_row, splits) do
    # Move each beam down and check for splits
    {new_beams, new_splits} =
      beams
      |> Enum.reduce({[], splits}, fn {row, column}, {acc_beams, acc_splits} ->
        next_row = row + 1

        if next_row > max_row do
          {acc_beams, acc_splits}
        else
          case Map.get(grid, {next_row, column}) do
            "^" ->
              left_beam = {next_row, column - 1}
              right_beam = {next_row, column + 1}
              {[left_beam, right_beam | acc_beams], acc_splits + 1}

            _ ->
              {[{next_row, column} | acc_beams], acc_splits}
          end
        end
      end)

    unique_beams = Enum.uniq(new_beams)

    simulate(unique_beams, grid, max_row, new_splits)
  end
end

answer = Simulator.simulate([{start_row, start_column}], grid, max_row, 0)

IO.inspect(answer)
