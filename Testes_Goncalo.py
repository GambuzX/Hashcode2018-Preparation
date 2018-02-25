# Why are we opening the file twice?
input_file = open("example.in")  # open file
first_line = input_file.readline()  # read the first line
magic_numbers = first_line.split(" ")  # separate the numbers by whitespaces
input_file.close()  # close file

input_file = open("example.in").read()

pizza = [x for x in input_file if x.isalpha()]


def clean_char(list):  # cleans something
    i = 1
    tamanho = len(list) - 1
    ultimo = list[tamanho]
    numero = ultimo[0]

    while i < tamanho:
        if ultimo[i] == '\n':
            list.pop()
            list.append(numero)
            break
        numero = numero+ultimo[i]
        i += 1

    return list


def count_mushrooms(array):  # counts the total number of mushrooms
    counter = 0

    for x in array:
        if x == "M":
            counter += 1
    return counter


def count_tomatoes(array):  # counts the total number of tomatoes
    counter = 0

    for x in array:
        if x == "T":
            counter += 1

    return counter


# Important variables
mushroom_count = count_mushrooms(pizza)
tomato_count = count_tomatoes(pizza)
magic_numbers = clean_char(magic_numbers)


n_rows = int(magic_numbers[0])
n_columns = int(magic_numbers[1])
minimum_ingredients = int(magic_numbers[2])
maximum_cells = int(magic_numbers[3])


# Creates a list of n sub-lists where n = n_rows, with each sub-list containing a single row of pizza
def make_matrix(lista, n_colunas):
    contador = 0
    matriz = []
    linha = []

    for i in lista:
        if contador == n_colunas:
            matriz.append(linha)
            contador = 1
            linha = [i]

        else:
            linha.append(i)
            contador += 1

    matriz.append(linha)
    return matriz


pizza_matrix = make_matrix(pizza, n_columns)


# Attempting to decide how cuts should be made based on the ingredients
def lines_to_ignore(matrix):
    lines = []

    def check_line(matrix, line):
        ignore_line = True

        for i in range(n_columns - 1):
            if matrix[line][i] != matrix[line][0]:
                ignore_line = False

        return ignore_line

    for i in range(n_rows):
        if check_line(pizza_matrix, i):
            lines.append(i)

    return lines


lines_to_ignore = lines_to_ignore(pizza_matrix)


def cut_direction():
    if len(lines_to_ignore) > (n_rows / 2):
        return True
    else:
        return False

if cut_direction():
    cut_vertically()
else:
    cut_horizontally()

# Debug zone
print(pizza_matrix, pizza_matrix[0][0], sep="\n")
print(lines_to_ignore)