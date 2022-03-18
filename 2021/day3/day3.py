binary_inputs = []
number_of_digits = 12
with open('input.txt','r') as input:
    for line in input:
        binary_inputs.append( line.split())


current_digit = 0
gamma_rate = []
epsilon_rate = []
while current_digit < number_of_digits:
    current_row = 0
    ones = 0
    zeros = 0
    while current_row < len(binary_inputs):
        print(f"{current_digit} {current_row} - {binary_inputs[current_row][0][current_digit]}")
        if int(binary_inputs[current_row][0][current_digit]) == 0:
            print("Zero")
            zeros += 1
        else:
            print("One")
            ones += 1
        current_row += 1
    print((ones, zeros))
    if ones > zeros:
        gamma_rate.append(1)
    else:
        gamma_rate.append(0)
    current_digit += 1
gamma_dec = int(''.join(str(x) for x in gamma_rate),2)
print(f" Gamma Rate = {gamma_rate} in decimal is {int(''.join(str(x) for x in gamma_rate),2)}")

for i in gamma_rate:
    if i == 1:
        epsilon_rate.append(0)
    else:
        epsilon_rate.append(1)
eps_dec = int(''.join(str(x) for x in epsilon_rate),2)
print(f" epsilon  Rate = {epsilon_rate} in decimal is {int(''.join(str(x) for x in epsilon_rate),2)}")

pw_consuption = gamma_dec*eps_dec
print(pw_consuption)