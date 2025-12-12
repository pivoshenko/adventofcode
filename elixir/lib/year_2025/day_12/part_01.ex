# Day 12: Christmas Tree Farm (#1).
# https://adventofcode.com/2025/day/12

filepath = "../data/inputs/year_2025/day_12.txt"

content =
  filepath
  |> File.read!()

[_, _, _, _, _, _, regions] = String.split(content, "\n\n")

parsed_regions =
  regions
  |> String.split("\n", trim: true)
  |> Enum.map(fn str ->
    str
    |> String.split(~r/x|: | /)
    |> Enum.reject(&(&1 == ""))
    |> Enum.map(&String.to_integer/1)
  end)

answer =
  parsed_regions
  |> Enum.count(fn region ->
    [w, h | presents] = region
    w * h >= Enum.sum(presents) * 9
  end)

IO.inspect(answer)
