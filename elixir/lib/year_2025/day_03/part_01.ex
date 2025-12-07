# Day 3: Lobby (#1).
# https://adventofcode.com/2025/day/3

filepath = "../data/inputs/year_2025/day_03.txt"

content =
  filepath
  |> File.read!()
  |> String.split("\n", trim: true)

pick_next_digit = fn digits, start, finish ->
  start..finish
  |> Enum.reduce({-1, -1}, fn i, {best_digit, best_idx} ->
    d = Enum.at(digits, i)
    if d > best_digit, do: {d, i}, else: {best_digit, best_idx}
  end)
end

answer =
  content
  |> Enum.map(fn line ->
    digits =
      line
      |> String.to_charlist()
      |> Enum.map(fn char -> char - ?0 end)

    {digit_1, idx_1} = pick_next_digit.(digits, 0, length(digits) - 2)
    {digit_2, _idx_2} = pick_next_digit.(digits, idx_1 + 1, length(digits) - 1)

    digit_1 * 10 + digit_2
  end)
  |> Enum.sum()

IO.inspect(answer)
