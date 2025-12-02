{options, _, _} =
  OptionParser.parse(System.argv(),
    strict: [filepath: :string],
    aliases: [f: :filepath]
  )

content =
  case options[:filepath] do
    nil ->
      IO.puts("Error: --filepath is required")
      System.halt(1)

    filepath ->
      filepath
      |> File.read!()
      |> String.split("\n", trim: true)
  end

{directions, rotations} =
  Enum.map(content, fn line ->
    {direction, rotation} = String.split_at(line, 1)
    {direction, String.to_integer(String.trim(rotation))}
  end)
  |> Enum.unzip()

initial_dial_position = 50

answer =
  Enum.zip(directions, rotations)
  |> Enum.reduce({initial_dial_position, []}, fn {direction, rotation},
                                                 {dial_position, dial_positions} ->
    dial_position =
      case direction do
        "L" -> dial_position - rotation
        "R" -> dial_position + rotation
      end
      |> Integer.mod(100)

    {dial_position, [dial_position | dial_positions]}
  end)
  |> then(fn {_dial_position, dial_positions} -> dial_positions end)
  |> Enum.count(fn dial_position -> dial_position == 0 end)

IO.inspect(answer)
