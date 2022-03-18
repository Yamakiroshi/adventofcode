
def prepare_inputs() -> list:
    inputs = []
    with open('./input.txt','r') as input_file:
        for line in input_file:
            inputs.append(line)

    inputs = [int(i) for i in inputs]

    #print(len(inputs))
    #print(inputs)
    return inputs

def part_one_solution(inputs:list) -> int:
    increasing_measurements = 0 
    previous_line = 0 
    for line in inputs:
        # Check if previous_line is zero, this means it's the start. 
        if previous_line == 0:
            previous_line = line
            continue

        if line > previous_line:
            increasing_measurements += 1
        
        previous_line = line

            #Else we ignore it
    print(increasing_measurements)
    return increasing_measurements


def part_two_solution(inputs:list) -> int:
    previous_set = []
    increasing_set = 0
    print("Looking for part two solution now")
    a = 0
    b = 3
    print(inputs[a:b])

    

    while b <= len(inputs):
        if not previous_set:
            previous_set = inputs[a:b]
            print(f"{chr(ord('A') + a)}  set {previous_set}")
        else:
            
            current_set = inputs[a:b]
            print(f"{chr(ord('A') + a)}  set {current_set}")
            previous_sum = sum(previous_set)
            current_sum = sum(current_set)
            if current_sum > previous_sum:
                increasing_set += 1
            previous_set = current_set
        
        a += 1
        b += 1
    print(increasing_set)



if __name__ == "__main__":
    demo_inputs = [199,200,208,210,200,207,240,269,260,263]
    inputs = prepare_inputs()
    answer_one = part_one_solution(inputs)
    answer_two = part_two_solution(inputs)