# Day 2: Gift Shop (#1).
# https://adventofcode.com/2025/day/2

filepath = "../data/examples/year_2025/day_02.txt"

content =
  filepath
  |> File.read!()
  |> String.replace("\n", "")
  |> String.split(",", trim: true)
  |> Enum.map(fn line ->
    String.split(line, "-") |> Enum.map(fn el -> String.to_integer(el) end)
  end)
  |> Enum.map(fn pair -> List.to_tuple(pair) end)

ids =
  content
  |> Enum.map(fn {start_id, end_id} ->
    Enum.to_list(start_id..end_id)
  end)

invalid_ids =
  ids
  |> Enum.map(fn id_range ->
    Enum.filter(id_range, fn id ->
      Regex.match?(~r/^(\d+)\1$/, Integer.to_string(id))
    end)
  end)

answer =
  invalid_ids
  |> List.flatten()
  |> Enum.reduce(0, fn id, sum -> sum + id end)

IO.inspect(answer)
