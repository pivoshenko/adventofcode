# Day 9: Movie Theater (#1).
# https://adventofcode.com/2025/day/9

filepath = "../data/inputs/year_2025/day_09.txt"

content =
  filepath
  |> File.read!()
  |> String.split("\n", trim: true)

red_tiles =
  Enum.map(content, fn line ->
    [x, y] = String.split(line, ",")
    {String.to_integer(x), String.to_integer(y)}
  end)

area_between = fn {x1, y1}, {x2, y2} ->
  width = abs(x1 - x2) + 1
  height = abs(y1 - y2) + 1
  width * height
end

answer =
  Enum.with_index(red_tiles)
  |> Enum.reduce(0, fn {point_a, index_a}, running_max ->
    remaining_tiles = Enum.drop(red_tiles, index_a + 1)

    remaining_tiles
    |> Enum.reduce(running_max, fn point_b, current_max ->
      area = area_between.(point_a, point_b)
      if area > current_max, do: area, else: current_max
    end)
  end)

IO.inspect(answer)
