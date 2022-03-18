x = 0
y = 0
houses = [[]]

print(houses)

def santa_move(direction:str):
    global x
    global y
    if direction == "<":
        x -= 1
    if direction == ">":
        x += 1
    if direction == "^":
        y += 1
    if direction == "v":
        y -= 1

input = "^v^v^v^v^v"

for character in input:
    santa_move(character)
    print(x,y)