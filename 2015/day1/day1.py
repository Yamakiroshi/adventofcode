first_found = False
floor = 0
with open("./input.txt", 'r') as demo_input:
    for line in demo_input:
        print(len(line))
        for index, character in enumerate(line):
            if character == "(":
                floor += 1
            elif character == ")":
                floor -= 1

            if floor == -1 and first_found == False:
                print(f"first time to reach the basement == {index}")
                first_found = True

print(floor)