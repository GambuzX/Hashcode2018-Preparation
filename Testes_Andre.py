input_file = open("big.in")

first_line = input_file.readline()

magic_numbers = first_line.split(" ")

print(first_line)
print(thisline)

i=1
ultimo=magic_numbers[3]
numero=ultimo[0]
while True:
    if ultimo[i] == '\n':
        magic_numbers.pop()
        magic_numbers.append(ultimo[i])
        break
    numero=numero+ultimo[i]
    i+=1








lastnumber=thisline[3]
thisline.pop()
