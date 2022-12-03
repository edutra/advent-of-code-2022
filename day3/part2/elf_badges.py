path = '..\input'

pontuation = 0

group = []

with open(path, 'r') as file:
    for line in file:
        line = line.strip()
        group.append(line)
        if len(group) == 3:
            for x in group[0]:
                if x in group[1] and x in group[2]:
                    if "a" <= x <= "z":
                        pontuation += ord(x) - ord("a") + 1
                    else:
                        pontuation += ord(x) - ord("A") + 27
                    break
            group = []
            
    print(pontuation)























    #     if len(group) < 3:
    #         for x in group[0]:
    #             if x in group[1] and x in group[2]:
    #                 # print(x, group[0], group[1], group[2])
    #                 if "a" <= x <= "z":
    #                     # print(ord(x) - ord("a") + 1)
    #                     pontuation += ord(x) - ord("a") + 1
                        
    #                 else:
    #                     # print(ord(x) - ord("A") + 27)
    #                     pontuation += ord(x) - ord("A") + 27
    #                 group = []
    #                 # break
    #     else:
    #         group.append(line)

    # print(pontuation)