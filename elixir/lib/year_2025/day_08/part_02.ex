# Day 8: Playground (#2).
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

defmodule CircuitTrackerP2 do
  def find(parent, point) do
    parent_point = Map.get(parent, point, point)

    if parent_point == point do
      {point, parent}
    else
      {root, updated_parent} = find(parent, parent_point)
      {root, Map.put(updated_parent, point, root)}
    end
  end

  def union(parent, rank, point_a, point_b) do
    {root_a, parent} = find(parent, point_a)
    {root_b, parent} = find(parent, point_b)

    if root_a == root_b do
      # Already in same circuit - no merge happened
      {:same_circuit, parent, rank}
    else
      rank_a = Map.get(rank, root_a, 0)
      rank_b = Map.get(rank, root_b, 0)

      {new_parent, new_rank} =
        cond do
          rank_a < rank_b ->
            {Map.put(parent, root_a, root_b), rank}

          rank_a > rank_b ->
            {Map.put(parent, root_b, root_a), rank}

          true ->
            {Map.put(parent, root_b, root_a), Map.put(rank, root_a, rank_a + 1)}
        end

      {:merged, new_parent, new_rank}
    end
  end

  def find_last_connection(pairs, parent, rank, circuit_count) do
    if circuit_count == 1 do
      nil
    else
      [{_dist, point_a, point_b} | remaining_pairs] = pairs

      case union(parent, rank, point_a, point_b) do
        {:same_circuit, updated_parent, updated_rank} ->
          find_last_connection(remaining_pairs, updated_parent, updated_rank, circuit_count)

        {:merged, updated_parent, updated_rank} ->
          new_circuit_count = circuit_count - 1

          if new_circuit_count == 1 do
            {point_a, point_b}
          else
            find_last_connection(remaining_pairs, updated_parent, updated_rank, new_circuit_count)
          end
      end
    end
  end
end

initial_parent = Map.new(junction_boxes, fn point -> {point, point} end)
initial_rank = %{}
initial_circuit_count = box_count

{last_point_a, last_point_b} =
  CircuitTrackerP2.find_last_connection(
    sorted_pairs,
    initial_parent,
    initial_rank,
    initial_circuit_count
  )

{x_a, _y_a, _z_a} = last_point_a
{x_b, _y_b, _z_b} = last_point_b

answer = x_a * x_b

IO.inspect(answer)
