# Day 1: Secret Entrance (#1).
# https://adventofcode.com/2025/day/1

filepath = "../data/examples/year_2025/day_01.txt"

content =
  filepath
  |> File.read!()
  |> String.split("\n", trim: true)

{directions, rotations} =
  Enum.map(content, fn line ->
    {direction, rotation} = String.split_at(line, 1)
    {direction, String.to_integer(String.trim(rotation))}
  end)
  |> Enum.unzip()

answer =
  Enum.zip(directions, rotations)
  |> Enum.reduce({50, []}, fn {direction, rotation}, {dial_position, dial_positions} ->
    dial_position =
      case direction do
        "L" -> dial_position - rotation
        "R" -> dial_position + rotation
      end
      |> Integer.mod(100)

    {dial_position, [dial_position | dial_positions]}
  end)
  |> then(fn {_dial_position, dial_positions} -> dial_positions end)
  |> Enum.count(fn dial_position -> dial_position == 0 end)

IO.inspect(answer)
