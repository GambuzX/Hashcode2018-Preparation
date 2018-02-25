input_file = open("example.in")  # open file
first_line = input_file.readline() # read the first line
magic_numbers = first_line.split(" ") # separate the numbers by whitespaces

n_rows = magic_numbers[0]
n_columns = magic_numbers[1]
minimum_ingredients = magic_numbers[2]
maximum_cells = magic_numbers[3]

input_file.close() # close file

input_file = open("example.in").read()

pizza = [x for x in input_file if x.isalpha()]
print (maximum_cells)

def countMushrooms(array):
    counter = 0
    for x in array:
        if x == "M":
            counter += 1
    return counter

def countTomatoes(array):
    counter = 0
    for x in array:
        if x == "T":
            counter += 1
    return counter

mushroomCount = countMushrooms(pizza)
tomatoCount = countTomatoes(pizza)

print (mushroomCount, tomatoCount)
