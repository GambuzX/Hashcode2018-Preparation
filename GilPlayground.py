input_file = open("example.in")
first_line = input_file.readline()
magic_numbers = first_line.split(" ")

n_rows = magic_numbers[0]
n_columns = magic_numbers[1]
minimum_ingredients = magic_numbers[2]
maximum_cells = magic_numbers[3]

pizza = input_file.readlines()
print (pizza)