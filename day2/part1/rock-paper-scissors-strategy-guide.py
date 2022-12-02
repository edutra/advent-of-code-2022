'''
A X -> Rock = 1 point
B Y -> Paper = 2 points
C Z -> Scissors = 3 points

lost = 0 points
draw = 3 points
win = 6 points

round pontuation = shape selected score + outcome of the round score

e.g.
A Y = win + paper = 8 points
B X = lost + rock = 1 point
C Z = draw + scissors = 6 points
'''

path = '../input'

pontuation = 0
enemy_choice = ""
selected_choice = ""

def resolve_round(enemy_choice, player_choice, pontuation):
    if enemy_choice == "A":
        if player_choice == "X":
            return 4
        elif player_choice == "Y":
            return 8
        elif player_choice == "Z":
            return 3
    elif enemy_choice == "B":
        if player_choice == "X":
            return 1
        elif player_choice == "Y":
            return 5
        elif player_choice == "Z":
            return 9
    elif enemy_choice == "C":
        if player_choice == "X":
            return 7
        elif player_choice == "Y":
            return 2
        elif player_choice == "Z":
            return 6

with open(path, 'r') as file:
    for line in file:
        enemy_choice, selected_choice = line.split(" ")
        selected_choice = selected_choice.split("\n")[0]
        pontuation += resolve_round(enemy_choice, selected_choice, pontuation)
        
    print(pontuation)
        
        

