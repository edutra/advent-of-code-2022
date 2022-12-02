path = '../input'

elf_id = 1
soma = 0
max_soma = 0
max_elf_id = 1

with open(path, 'r') as file:
    for line in file:
        if line == '\n':
            if soma > max_soma:
                max_soma = soma
                max_elf_id = elf_id
            soma = 0
            elf_id += 1
                
        else:
            soma += int(line)
            
    print(max_soma)
