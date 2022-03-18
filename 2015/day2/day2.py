
def calculate_present_size(length:int, width:int, height:int)-> int:
    #print(length, width, height)
    side_one = length*width
    side_two = width*height
    side_three = height*length
    smallest_side = min([side_one, side_two, side_three])
    total_size = (side_one * 2 ) + (side_two * 2) + (side_three * 2)+smallest_side
    return total_size

def calculate_ribbon_size(length:int, width:int, height:int) -> int:
    bow_length = length * width * height
    side_one = (width * 2) + (length * 2) 
    side_two = (width * 2) + (height * 2)
    side_three = (length * 2) + (height * 2) 
    smallest_side = min([side_one, side_two, side_three])
    return bow_length + smallest_side

if __name__ == "__main__":
    total_paper = 0
    total_ribbon = 0
    with open("./input.txt", 'r') as input_data:
        for line in input_data:
            present_dims = line.split('x')
            total_paper += calculate_present_size(int(present_dims[0]), int(present_dims[1]), int(present_dims[2]))
            total_ribbon += calculate_ribbon_size(int(present_dims[0]), int(present_dims[1]), int(present_dims[2]))
    print(total_paper)
    print(total_ribbon)
    print(calculate_ribbon_size(2,3,4))
    
