# Day 11: Reactor (#1).
# https://adventofcode.com/2025/day/11

filepath = "../data/inputs/year_2025/day_11.txt"

content =
  filepath
  |> File.read!()
  |> String.split("\n", trim: true)

graph =
  Enum.reduce(content, %{}, fn line, acc ->
    [device, outputs] = String.split(line, ": ", parts: 2)
    output_list = String.split(outputs, " ", trim: true)
    Map.put(acc, device, output_list)
  end)

find_all_paths = fn graph, start, target ->
  find_paths = fn find_paths, current, visited ->
    cond do
      current == target ->
        1

      true ->
        visited = MapSet.put(visited, current)
        neighbors = Map.get(graph, current, [])

        neighbors
        |> Enum.reject(&MapSet.member?(visited, &1))
        |> Enum.map(&find_paths.(find_paths, &1, visited))
        |> Enum.sum()
    end
  end

  find_paths.(find_paths, start, MapSet.new())
end

answer = find_all_paths.(graph, "you", "out")

IO.inspect(answer)
