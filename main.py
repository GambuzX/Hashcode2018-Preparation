input_file = open("example.in")  # open file
first_line = input_file.readline() # read the first line
magic_numbers = first_line.split(" ") # separate the numbers by whitespaces
input_file.close() # close file

input_file = open("example.in").read()

pizza = [x for x in input_file if x.isalpha()]
print (pizza)

def limpar_caracter(lista):
    i=1
    tamanho=lista.length-1
    ultimo=lista[tamanho]
    numero=ultimo[0]
    while True:
        if ultimo[i] == '\n':
            lista.pop()
            lista.append(ultimo[i])
            break
        numero=numero+ultimo[i]
        i+=1
    return numero

def countMushrooms(array): #counts the total number of mushrooms
    counter = 0
    for x in array:
        if x == "M":
            counter += 1
    return counter

def countTomatoes(array): #counts the total number of tomatoes
    counter = 0
    for x in array:
        if x == "T":
            counter += 1
    return counter

mushroomCount = countMushrooms(pizza)
tomatoCount = countTomatoes(pizza)
magic_numbers = limpar_caracter(magic_numbers)


n_rows = magic_numbers[0]
n_columns = magic_numbers[1]
minimum_ingredients = magic_numbers[2]
maximum_cells = magic_numbers[3]
