'''
A -> Rock = 1 point
B -> Paper = 2 points
C -> Scissors = 3 points

X -> lost = 0 points
Y -> draw = 3 points
Z -> win = 6 points

round pontuation = shape selected score + outcome of the round score

e.g.
A Y = draw -> need to play rock -> 3 + 1
B X = lost -> need to play rock -> 0 + 1
C Z = win -> need to play rock -> 6 + 1
'''

path = '../input'

pontuation = 0


with open(path, 'r') as file:
    for line in file:
        plays = {("A", "X"): 3, ("B", "X"): 1, ("C", "X"): 2,
                 ("A", "Y"): 4, ("B", "Y"): 5, ("C", "Y"): 6,
                 ("A", "Z"): 8, ("B", "Z"): 9, ("C", "Z"): 7}
        enemy_choice, outcome = line.split()
        pontuation += plays[(enemy_choice, outcome)]
        
    print(pontuation)
        
        

