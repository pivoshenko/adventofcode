# Day 1: Secret Entrance (#2).
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

step = fn
  "R" -> 1
  "L" -> -1
end

{_dial_position, answer} =
  Enum.reduce(Enum.zip(directions, rotations), {50, 0}, fn {direction, rotation},
                                                           {dial_position, count} ->
    {dial_position, count} =
      Enum.reduce(1..rotation, {dial_position, count}, fn _, {position, count} ->
        position = Integer.mod(position + step.(direction), 100)
        count = if position == 0, do: count + 1, else: count
        {position, count}
      end)

    {dial_position, count}
  end)

IO.inspect(answer)
