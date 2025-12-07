# Day 6: Trash Compactor (#1).
# https://adventofcode.com/2025/day/6

filepath = "../data/inputs/year_2025/day_06.txt"

content =
  filepath
  |> File.read!()
  |> String.split("\n", trim: true)
  |> Enum.map(fn line -> String.split(line, ~r/\s+/, trim: true) end)

max_columns = Enum.max_by(content, fn line -> length(line) end) |> length()

padded_lines =
  Enum.map(content, fn line -> line ++ List.duplicate("", max_columns - length(line)) end)

columns = padded_lines |> Enum.zip() |> Enum.map(fn column -> Tuple.to_list(column) end)

answer =
  Enum.reduce(columns, 0, fn column, total ->
    case List.last(column) do
      "+" ->
        numbers =
          Enum.slice(column, 0, length(column) - 1)
          |> Enum.filter(fn el -> el != "" end)
          |> Enum.map(fn el -> String.to_integer(el) end)

        total + Enum.sum(numbers)

      "*" ->
        numbers =
          Enum.slice(column, 0, length(column) - 1)
          |> Enum.filter(fn el -> el != "" end)
          |> Enum.map(fn el -> String.to_integer(el) end)

        total + Enum.reduce(numbers, 1, fn number, acc -> number * acc end)

      _ ->
        total
    end
  end)

IO.inspect(answer)
