input_file = open("big.in")

first_line = input_file.readline()

magic_numbers = first_line.split(" ")

i=1
ultimo=magic_numbers[3]
numero=ultimo[0]
def limpar_caracter(lista):
    i=1
    tamanho=lista.length
    ultimo=lista[tamanho]
    numero=ultimo[0]
    while True:
        if ultimo[i] == '\n':
            magic_numbers.pop()
            magic_numbers.append(ultimo[i])
            break
        numero=numero+ultimo[i]
        i+=1




