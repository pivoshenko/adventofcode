# Day 4: Printing Department (#1).
# https://adventofcode.com/2025/day/4

filepath = "../data/inputs/year_2025/day_04.txt"

content =
  filepath
  |> File.read!()
  |> String.split("\n", trim: true)

grid =
  Enum.reduce(Enum.with_index(content), %{}, fn {line, y}, grid_acc ->
    chars = String.graphemes(line)

    Enum.reduce(Enum.with_index(chars), grid_acc, fn {cell, x}, grid_acc_2 ->
      Map.put(grid_acc_2, {x, y}, cell)
    end)
  end)

answer =
  Enum.reduce(grid, 0, fn {{x, y}, cell}, acc ->
    if cell == "@" do
      neighbor_count =
        Enum.reduce(-1..1, 0, fn dy, cnt_1 ->
          Enum.reduce(-1..1, cnt_1, fn dx, cnt_2 ->
            if dx == 0 and dy == 0 do
              cnt_2
            else
              neighbor_pos = {x + dx, y + dy}

              if Map.get(grid, neighbor_pos) == "@" do
                cnt_2 + 1
              else
                cnt_2
              end
            end
          end)
        end)

      if neighbor_count < 4 do
        acc + 1
      else
        acc
      end
    else
      acc
    end
  end)

IO.inspect(answer)
