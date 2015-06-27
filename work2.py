# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math

secret_number = 0
low = 0
high = 100
n = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    range100()
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number, low, high, n
    print 'set the range [0,100)\n'
    low = 0
    high = 100
    n = math.ceil(math.log(high - low + 1, 2))
    
    secret_number = random.randrange(low, high)
    
    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number, low, high, n
    print 'set the range [0,1000)\n'
    low = 0
    high = 1000
    n = math.ceil(math.log(high - low + 1, 2))
    
    secret_number = random.randrange(low, high)
    
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number, n
    print 'you try the number', n
    if n == 0:
        print 'You lost! correct is', secret_number
        print 'starts the new game.'
        new_game()     
    guess_number = int(guess)
    print "Guess was", guess_number
    if secret_number == guess_number:
        print "Correct"
        new_game()
    elif secret_number > guess_number:
        print "Higher"
    elif secret_number < guess_number:
        print "Lower"
    n = n - 1
    print '\n'
    
        
    
    
# create frame
frame = simplegui.create_frame("Guess the number",200,200)



# register event handlers for control elements and start frame
frame.add_button("Range: 0 - 100", range100,150)
frame.add_button("Range: 0 - 1000", range1000,150)
inp = frame.add_input('guess the number', input_guess, 50)
inp.set_text('')

frame.start()


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
