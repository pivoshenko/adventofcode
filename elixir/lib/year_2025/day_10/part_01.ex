# Day 10: Light Machine (#1).
# https://adventofcode.com/2025/day/10

filepath = "../data/inputs/year_2025/day_10.txt"

content =
  filepath
  |> File.read!()
  |> String.split("\n", trim: true)

parse_line = fn line ->
  [lights_part | rest] = String.split(line, "] ")

  lights =
    lights_part
    |> String.trim_leading("[")
    |> String.graphemes()
    |> Enum.map(&if &1 == "#", do: 1, else: 0)

  buttons_str = Enum.join(rest, "] ") |> String.split(" {") |> hd()

  buttons =
    Regex.scan(~r/\(([0-9,]+)\)/, buttons_str)
    |> Enum.map(fn [_, nums] ->
      nums |> String.split(",") |> Enum.map(&String.to_integer/1)
    end)

  {lights, buttons}
end

find_pivot = fn matrix, start_row, col ->
  matrix
  |> Enum.drop(start_row)
  |> Enum.find_index(fn row -> Enum.at(row, col) == 1 end)
  |> case do
    nil -> nil
    idx -> start_row + idx
  end
end

swap_rows = fn matrix, i, j ->
  if i == j do
    matrix
  else
    row_i = Enum.at(matrix, i)
    row_j = Enum.at(matrix, j)

    matrix
    |> List.replace_at(i, row_j)
    |> List.replace_at(j, row_i)
  end
end

xor_rows = fn row1, row2 ->
  Enum.zip(row1, row2)
  |> Enum.map(fn {a, b} -> rem(a + b, 2) end)
end

eliminate_column = fn matrix, pivot_row, col ->
  pivot = Enum.at(matrix, pivot_row)

  matrix
  |> Enum.with_index()
  |> Enum.map(fn {row, idx} ->
    if idx != pivot_row and Enum.at(row, col) == 1 do
      xor_rows.(row, pivot)
    else
      row
    end
  end)
end

find_all_solutions = fn matrix, num_vars ->
  pivot_vars =
    matrix
    |> Enum.with_index()
    |> Enum.reduce([], fn {row, _idx}, acc ->
      case Enum.find_index(Enum.take(row, num_vars), &(&1 == 1)) do
        nil -> acc
        col -> [col | acc]
      end
    end)
    |> Enum.reverse()
    |> Enum.uniq()

  free_vars = Enum.to_list(0..(num_vars - 1)) -- pivot_vars

  consistent? =
    Enum.all?(matrix, fn row ->
      leading = Enum.find_index(Enum.take(row, num_vars), &(&1 == 1))
      rhs = Enum.at(row, num_vars)
      leading != nil or rhs == 0
    end)

  if not consistent? do
    :no_solution
  else
    num_free = length(free_vars)

    all_solutions =
      if num_free == 0 do
        # No free variables, compute single solution
        solution = List.duplicate(0, num_vars)

        result =
          Enum.reduce(Enum.reverse(matrix), {:ok, solution}, fn row, acc ->
            case acc do
              :no_solution ->
                :no_solution

              {:ok, sol} ->
                leading = Enum.find_index(Enum.take(row, num_vars), &(&1 == 1))
                rhs = Enum.at(row, num_vars)

                case leading do
                  nil ->
                    {:ok, sol}

                  idx ->
                    val =
                      rem(
                        rhs +
                          Enum.sum(
                            Enum.drop(row, idx + 1)
                            |> Enum.take(num_vars - idx - 1)
                            |> Enum.zip(Enum.drop(sol, idx + 1))
                            |> Enum.map(fn {a, b} -> a * b end)
                          ),
                        2
                      )

                    {:ok, List.replace_at(sol, idx, val)}
                end
            end
          end)

        case result do
          {:ok, sol} -> [sol]
          :no_solution -> []
        end
      else
        for combo <- 0..(Integer.pow(2, num_free) - 1) do
          # Set free variables according to combo
          free_vals =
            for i <- 0..(num_free - 1) do
              if rem(div(combo, Integer.pow(2, i)), 2) == 1, do: 1, else: 0
            end

          initial_solution =
            Enum.reduce(Enum.zip(free_vars, free_vals), List.duplicate(0, num_vars), fn {var, val},
                                                                                        sol ->
              List.replace_at(sol, var, val)
            end)

          Enum.reduce(Enum.reverse(matrix), initial_solution, fn row, sol ->
            leading = Enum.find_index(Enum.take(row, num_vars), &(&1 == 1))

            case leading do
              nil ->
                sol

              idx ->
                rhs = Enum.at(row, num_vars)

                val =
                  rem(
                    rhs +
                      Enum.sum(
                        Enum.drop(row, idx + 1)
                        |> Enum.take(num_vars - idx - 1)
                        |> Enum.zip(Enum.drop(sol, idx + 1))
                        |> Enum.map(fn {a, b} -> a * b end)
                      ),
                    2
                  )

                List.replace_at(sol, idx, val)
            end
          end)
        end
      end

    if all_solutions == [] do
      :no_solution
    else
      {:ok, Enum.min_by(all_solutions, &Enum.sum/1)}
    end
  end
end

gaussian_elimination_gf2 = fn matrix ->
  rows = length(matrix)
  cols = if rows > 0, do: length(hd(matrix)), else: 0
  vars = cols - 1

  {reduced, _} =
    Enum.reduce(0..(min(rows, vars) - 1), {matrix, 0}, fn col, {mat, pivot_row} ->
      case find_pivot.(mat, pivot_row, col) do
        nil ->
          {mat, pivot_row}

        pivot_idx ->
          mat = swap_rows.(mat, pivot_row, pivot_idx)
          mat = eliminate_column.(mat, pivot_row, col)
          {mat, pivot_row + 1}
      end
    end)

  find_all_solutions.(reduced, vars)
end

solve_machine = fn {target, buttons} ->
  n = length(target)
  m = length(buttons)

  matrix =
    for i <- 0..(n - 1) do
      row =
        for j <- 0..(m - 1) do
          if i in Enum.at(buttons, j), do: 1, else: 0
        end

      row ++ [Enum.at(target, i)]
    end

  case gaussian_elimination_gf2.(matrix) do
    {:ok, solution} -> Enum.sum(solution)
    :no_solution -> 0
  end
end

answer =
  content
  |> Enum.map(parse_line)
  |> Enum.map(solve_machine)
  |> Enum.sum()

IO.inspect(answer)
