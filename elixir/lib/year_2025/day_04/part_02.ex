# Day 4: Printing Department (#2).
# https://adventofcode.com/2025/day/4

filepath = "../data/examples/year_2025/day_04.txt"

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

count_neighbors = fn grid_state, x, y ->
  Enum.reduce(-1..1, 0, fn dy, cnt_1 ->
    Enum.reduce(-1..1, cnt_1, fn dx, cnt_2 ->
      if dx == 0 and dy == 0 do
        cnt_2
      else
        neighbor_pos = {x + dx, y + dy}

        if Map.get(grid_state, neighbor_pos) == "@" do
          cnt_2 + 1
        else
          cnt_2
        end
      end
    end)
  end)
end

find_accessible = fn grid_state ->
  Enum.reduce(grid_state, [], fn {{x, y}, cell}, acc_positions ->
    if cell == "@" do
      neighbor_count = count_neighbors.(grid_state, x, y)

      if neighbor_count < 4 do
        [{x, y} | acc_positions]
      else
        acc_positions
      end
    else
      acc_positions
    end
  end)
end

remove_many = fn grid_state, positions ->
  Enum.reduce(positions, grid_state, fn {x, y}, g ->
    Map.put(g, {x, y}, ".")
  end)
end

{_f_grid, answer} =
  Stream.iterate({grid, 0}, fn {current_grid, removed_so_far} ->
    accessible_positions = find_accessible.(current_grid)

    case accessible_positions do
      [] ->
        {current_grid, removed_so_far}

      _ ->
        new_grid = remove_many.(current_grid, accessible_positions)
        {new_grid, removed_so_far + length(accessible_positions)}
    end
  end)
  |> Enum.reduce_while(nil, fn {current_grid, removed_so_far}, _acc ->
    accessible_positions = find_accessible.(current_grid)

    if accessible_positions == [] do
      {:halt, {current_grid, removed_so_far}}
    else
      {:cont, {current_grid, removed_so_far}}
    end
  end)

IO.inspect(answer)
