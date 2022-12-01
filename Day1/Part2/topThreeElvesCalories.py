path = '../input'

elf_arr = [0, 0, 0]
soma = 0

with open(path, 'r') as file:
    for line in file:
        if line == '\n':
            elf_arr.sort()
            if soma > elf_arr[0]:
                del elf_arr[0]
                elf_arr.append(soma)
            soma = 0
            
        else:
            soma += int(line)

    print(sum(elf_arr))

