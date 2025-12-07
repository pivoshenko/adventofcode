# Day 5: Cafeteria (#1).
# https://adventofcode.com/2025/day/5

filepath = "../data/inputs/year_2025/day_05.txt"

[input_ranges, input_ids] =
  filepath
  |> File.read!()
  |> String.split("\n\n", trim: true)

range_lines =
  input_ranges
  |> String.split("\n", trim: true)

id_lines =
  input_ids
  |> String.split("\n", trim: true)

ranges =
  Enum.map(range_lines, fn line ->
    [from_str, to_str] = String.split(line, "-", parts: 2)
    {String.to_integer(from_str), String.to_integer(to_str)}
  end)

ids =
  Enum.map(id_lines, fn line ->
    String.to_integer(line)
  end)

is_fresh = fn id_value, ranges_list ->
  Enum.any?(ranges_list, fn {from_id, to_id} ->
    from_id <= id_value and id_value <= to_id
  end)
end

answer =
  Enum.reduce(ids, 0, fn id_value, acc_count ->
    if is_fresh.(id_value, ranges) do
      acc_count + 1
    else
      acc_count
    end
  end)

IO.inspect(answer)
