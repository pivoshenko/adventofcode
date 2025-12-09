# Day 8: Playground (#1).
# https://adventofcode.com/2025/day/8

filepath = "../data/inputs/year_2025/day_08.txt"

content =
  filepath
  |> File.read!()
  |> String.split("\n", trim: true)

junction_boxes =
  Enum.map(content, fn line ->
    [x, y, z] = String.split(line, ",")
    {String.to_integer(x), String.to_integer(y), String.to_integer(z)}
  end)

boxes_map =
  junction_boxes
  |> Enum.with_index()
  |> Map.new(fn {box, index} -> {index, box} end)

box_count = length(junction_boxes)

distance_squared = fn {x1, y1, z1}, {x2, y2, z2} ->
  dx = x2 - x1
  dy = y2 - y1
  dz = z2 - z1
  dx * dx + dy * dy + dz * dz
end

pairs =
  for i <- 0..(box_count - 2),
      j <- (i + 1)..(box_count - 1) do
    point_a = Map.get(boxes_map, i)
    point_b = Map.get(boxes_map, j)
    dist = distance_squared.(point_a, point_b)
    {dist, point_a, point_b}
  end

sorted_pairs = Enum.sort_by(pairs, fn {dist, _point_a, _point_b} -> dist end)

connections = Enum.take(sorted_pairs, 1000)

defmodule CircuitTrackerP1 do
  def find(parent, point) do
    parent_point = Map.get(parent, point, point)

    if parent_point == point do
      {point, parent}
    else
      {root, updated_parent} = find(parent, parent_point)
      # Path compression
      {root, Map.put(updated_parent, point, root)}
    end
  end

  def union(parent, rank, point_a, point_b) do
    {root_a, parent} = find(parent, point_a)
    {root_b, parent} = find(parent, point_b)

    if root_a == root_b do
      # Already in same circuit
      {parent, rank}
    else
      rank_a = Map.get(rank, root_a, 0)
      rank_b = Map.get(rank, root_b, 0)

      cond do
        rank_a < rank_b ->
          {Map.put(parent, root_a, root_b), rank}

        rank_a > rank_b ->
          {Map.put(parent, root_b, root_a), rank}

        true ->
          {Map.put(parent, root_b, root_a), Map.put(rank, root_a, rank_a + 1)}
      end
    end
  end
end

initial_parent = Map.new(junction_boxes, fn point -> {point, point} end)
initial_rank = %{}

{final_parent, _final_rank} =
  Enum.reduce(connections, {initial_parent, initial_rank}, fn {_dist, point_a, point_b},
                                                              {parent, rank} ->
    CircuitTrackerP1.union(parent, rank, point_a, point_b)
  end)

circuit_sizes =
  junction_boxes
  |> Enum.map(fn point ->
    {root, _parent} = CircuitTrackerP1.find(final_parent, point)
    root
  end)
  |> Enum.frequencies()
  |> Map.values()


top_3_sizes =
  circuit_sizes
  |> Enum.sort(:desc)
  |> Enum.take(3)

answer = Enum.reduce(top_3_sizes, 1, fn size, acc -> size * acc end)

IO.inspect(answer)
