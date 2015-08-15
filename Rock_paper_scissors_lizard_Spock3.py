import random


def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return -1


def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'invalid number'

def rpsls(player_choice):
    print('\n')
    print('Player chooses', player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
#   print('player_number=',player_number,'comp_number=',comp_number)
    print('Computer chooses', comp_choice)
    Sub = player_number - comp_number
    Mod1 = Sub % -5
    Mod2 = Sub % 5
#   print("Mod2(%5)",Mod2,"Mod1(%-5)",Mod1)
    if Sub == 0:
        print('Player and computer tie!')
    elif (Sub == 1) or  (Sub == 2):
        print('Player wins!')
    elif (Sub == -1) or  (Sub == -2):
        print('Computer wins!')
    elif (Mod2 == 1) or (Mod2 == 2):
        print('Player wins!')
    elif (Mod1 == -1) or  (Mod1 == -2):
        print('Computer wins!')
    else:
        print('Invalid Result')
    
        
#player_choice = input("Please enter the choice:")
#rpsls(player_choice)

    
    
    