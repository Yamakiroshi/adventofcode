def prepare_inputs() -> list:
    inputs = []
    with open('./input.txt','r') as input_file:
        for line in input_file:
            inputs.append(line)

    return inputs

def part_one_function(input:list) -> int:
    depth = 0
    horizontal = 0

    for instruction in input:
        action_value = instruction.split(' ')
        action = action_value[0]
        value = int(action_value[1])
        if action == "forward":
            horizontal += value
        elif action == "down":
            depth += value
        else:
            depth -= value

    return ((depth * horizontal), depth, horizontal)

def part_two_function(input:list) -> int:
    depth = 0
    horizontal = 0
    aim = 0 
    for instruction in input:
        action_value = instruction.split(' ')
        action = action_value[0]
        value = int(action_value[1])
        if action == "forward":
            horizontal += value
            depth += (value * aim)
        elif action == "down":
            aim += value
        else:
            aim -= value

    return ((depth * horizontal), depth, horizontal, aim)


if __name__ == "__main__":
    demo_input = ["forward 5" , "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    input = prepare_inputs()
    part_one_demo_solution = part_one_function(demo_input)
    print(part_one_demo_solution)
    part_one_solution = part_one_function(input)
    print(part_one_solution)
    part_two_demo_solution = part_two_function(demo_input)
    print(part_two_demo_solution)
    part_two_solution = part_two_function(input)
    print(part_two_solution)