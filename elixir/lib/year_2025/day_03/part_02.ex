filepath = "../data/examples/year_2025/day_03.txt"

# Function to find max k-digit number from a digit list
pick_k_digits = fn digits, k ->
  # Recursive helper to build the result
  pick_helper = fn pick_helper, remaining_digits, _start_idx, digits_needed, acc ->
    if digits_needed == 0 do
      acc
    else
      # We can search up to position where we still have enough digits left
      search_end = length(remaining_digits) - digits_needed

      # Find the maximum digit in valid range
      {max_digit, max_pos} =
        0..search_end
        |> Enum.reduce({-1, -1}, fn i, {best_digit, best_pos} ->
          d = Enum.at(remaining_digits, i)
          if d > best_digit, do: {d, i}, else: {best_digit, best_pos}
        end)

      # Take digits after the selected position and continue
      new_remaining = Enum.drop(remaining_digits, max_pos + 1)
      pick_helper.(pick_helper, new_remaining, 0, digits_needed - 1, acc * 10 + max_digit)
    end
  end

  pick_helper.(pick_helper, digits, 0, k, 0)
end

content =
  filepath
  |> File.read!()
  |> String.split("\n", trim: true)

answer =
  content
  |> Enum.map(fn line ->
    digits =
      line
      |> String.to_charlist()
      |> Enum.map(fn char -> char - ?0 end)

    pick_k_digits.(digits, 12)
  end)
  |> Enum.sum()

IO.inspect(answer)
