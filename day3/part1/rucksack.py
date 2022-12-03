path = '..\input'

pontuation = 0

with open(path, 'r') as file:
    for line in file:
        line.strip()
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        for x in firstpart:
            if x in secondpart:
                if "a" <= x <= "z":
                    pontuation += ord(x) - ord("a") + 1
                else:
                    pontuation += ord(x) - ord("A") + 27
                break

    print(pontuation)