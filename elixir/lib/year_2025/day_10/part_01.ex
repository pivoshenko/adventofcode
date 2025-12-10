# Day 10: Factory (#1).
# https://adventofcode.com/2025/day/10

filepath = "../data/inputs/year_2025/day_10.txt"

parse_line = fn line ->
  [target_str | rest] = String.split(line, "] ")

  target =
    target_str
    |> String.trim_leading("[")
    |> String.graphemes()
    |> Enum.map(&(&1 == "#"))

  buttons_str = Enum.join(rest, "] ")

  buttons =
    Regex.scan(~r/\(([0-9,]+)\)/, buttons_str)
    |> Enum.map(fn [_, indices] ->
      indices
      |> String.split(",")
      |> Enum.map(&String.to_integer/1)
    end)

  {target, buttons}
end

find_pivot = fn matrix, start_row, col ->
  Enum.find_index(Enum.drop(matrix, start_row), fn row ->
    Enum.at(row, col) == 1
  end)
  |> case do
    nil -> nil
    idx -> start_row + idx
  end
end

swap_rows = fn matrix, i, j ->
  row_i = Enum.at(matrix, i)
  row_j = Enum.at(matrix, j)

  matrix
  |> List.replace_at(i, row_j)
  |> List.replace_at(j, row_i)
end

xor_rows = fn row1, row2 ->
  Enum.zip(row1, row2)
  |> Enum.map(fn {a, b} -> Bitwise.bxor(a, b) end)
end

back_substitute = fn matrix, num_vars ->
  inconsistent? =
    Enum.any?(matrix, fn row ->
      Enum.take(row, num_vars) |> Enum.all?(&(&1 == 0)) and
        Enum.at(row, num_vars) == 1
    end)

  if inconsistent? do
    :no_solution
  else
    solution =
      for i <- 0..(num_vars - 1) do
        row = Enum.at(matrix, i)

        if row && Enum.at(row, i) == 1 do
          Enum.at(row, num_vars)
        else
          0
        end
      end

    {:ok, solution}
  end
end

gauss_eliminate = fn matrix, num_vars ->
  num_rows = length(matrix)

  {reduced, _} =
    Enum.reduce(0..(num_vars - 1), {matrix, 0}, fn col, {mat, row} ->
      if row >= num_rows do
        {mat, row}
      else
        case find_pivot.(mat, row, col) do
          nil ->
            {mat, row}

          pivot_row ->
            mat = swap_rows.(mat, row, pivot_row)

            mat =
              for i <- 0..(num_rows - 1), i != row do
                if Enum.at(Enum.at(mat, i), col) == 1 do
                  xor_rows.(Enum.at(mat, i), Enum.at(mat, row))
                else
                  Enum.at(mat, i)
                end
              end
              |> List.insert_at(row, Enum.at(mat, row))
              |> Enum.take(num_rows)

            {mat, row + 1}
        end
      end
    end)

  back_substitute.(reduced, num_vars)
end

solve_machine = fn {target, buttons} ->
  num_lights = length(target)
  num_buttons = length(buttons)

  matrix =
    for i <- 0..(num_lights - 1) do
      row =
        for j <- 0..(num_buttons - 1) do
          button = Enum.at(buttons, j)
          if i in button, do: 1, else: 0
        end

      target_val = if Enum.at(target, i), do: 1, else: 0
      row ++ [target_val]
    end

  case gauss_eliminate.(matrix, num_buttons) do
    {:ok, solution} -> Enum.sum(solution)
    :no_solution -> :infinity
  end
end

answer =
  filepath
  |> File.read!()
  |> String.trim()
  |> String.split("\n")
  |> Enum.map(parse_line)
  |> Enum.map(solve_machine)
  |> Enum.sum()

IO.inspect(answer)
