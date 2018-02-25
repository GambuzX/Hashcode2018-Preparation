input_file = open("example.in").read()

magic_numbers = [int(x) for x in input_file if x.isdigit()]

n_rows = magic_numbers[0]
n_columns = magic_numbers[1]
minimum_ingredients = magic_numbers[2]
maximum_cells = magic_numbers[3]

pizza = [x for x in input_file if x.isalpha()]

slices = []

# Attempting slicing of pizza
# The following loop returns a list of lists, each containing the ingredients in each column.
# It works by slicing the pizza vertically, but doesn't take into account the height of the pizza.
i = 0

while i < len(pizza) - 10:
    slices.append(pizza[i::4 + 1])
    i = i + 1

# Debug area, remove on release
print(input_file, slices, sep="\n")
