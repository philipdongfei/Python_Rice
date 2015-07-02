
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
# defining number to name
def number_to_name(Number):   
# convert name to number using if/elif/else(number):


    if Number == 0:
        Name = "ROCK"
    elif Number == 1:
        Name = "SPOCK"
    elif Number == 2:
        Name = "PAPER"
    elif Number == 3:
        Name = "LIZARD"
    elif Number == 4:
        Name = "SCISSORS" 
        # don't forget to return the result!
    return Name
#defining name to number    
def name_to_number(Name):
# convert number to a name using if/elif/else

    if Name == "ROCK":
        Number = 0
    elif Name == "SPOCK":
        Number = 1
    elif Name == "PAPER":
        Number = 2
    elif Name == "LIZARD":
        Number = 3
    elif Name == "SCISSORS":
        Number = 4
# don't forget to return the result!
    return Number

def rpsls(Name):
# delete the following pass statement and fill in your code below
# compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    player_number = name_to_number(Name)
    difference = (player_number-comp_number)
    difference_modular = (difference % 5)
# convert the player's choice to player_number using the function name_to_number()
    print "Player chooses", Name
    comp_name = number_to_name(comp_number)
    print "Computer chooses", comp_name
     # use if/elif/else to determine winner, print winner message

    if 1 <= difference_modular <= 2:
        print "Player wins!"
    elif 3 <= difference_modular:
        print "Computer wins!"
    elif difference_modular == 0:
        print "Player and computer tie!"
    print "\n"
    
# test your code
rpsls("ROCK")
rpsls("SPOCK")
rpsls("PAPER")
rpsls("LIZARD")
rpsls("SCISSORS")