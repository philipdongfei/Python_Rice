# implementation of card game - Memory
#http://www.codeskulptor.org/#user40_Z0J2SMUvGh_1.py
import simplegui
import random

number_list = []
exposed  = []
pairs = []
each_x = 800 / 16
Turns = 0
Turn_idx1 = -1
Turn_idx2 = -1

# helper function to initialize globals
def new_game():
    global state, Turns, pairs
	pairs = []
    state = 0
    Turns = 0
    label.set_text('Turns='+str(Turns))
    Turn_idx1 = -1
    Turn_idx2 = -1
    for i in range(16):
        if len(number_list) == 16:
            number_list[i] = i % 8
        else:
            number_list.append(i % 8)
        if len(exposed) == 16:
            exposed[i] = False
        else:
            exposed.append(False)
    random.shuffle(number_list)


     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global each_x, exposed, state, Turns, Turn_idx1, Turn_idx2,pairs
    if pos[1] > 0 and pos[1] < 100:
        idx = pos[0] // each_x
        if exposed[idx] == False:            
            if state == 0:#0->1
                state = 1
                Turn_idx1 = idx
            elif state == 1:#1->2
                state = 2
                Turn_idx2 = idx
                Turns = Turns + 1
                label.set_text('Turns='+str(Turns))
                if Turn_idx1 >= 0 and Turn_idx2 >= 0:
                    if number_list[Turn_idx1] == number_list[Turn_idx2]:
                        pairs.append(Turn_idx1)
                        pairs.append(Turn_idx2)
            else:#2->1
                state = 1
                Turn_idx1 = idx
                for idx1 in range(len(exposed)):
                    if exposed[idx1] == True:
                        if idx1 not in pairs:
                            exposed[idx1] = False
            exposed[idx] = True
           
   
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global number_list, exposed, each_x
    each_y = 100 / 3 * 2    
    for idx in range(len(number_list)):
         canvas.draw_line((idx * each_x + each_x / 2, 0), (idx * each_x + each_x / 2, 100), 800 / 16, 'Green')
		#use a fun of 
		#canvas.draw_polyline ([(idx*CARD_WIDTH, 0),
                                  # ((idx+1)*CARD_WIDTH, 0),
                                  # ((idx+1)*CARD_WIDTH, DECK_HEIGHT),
                                  # (idx*CARD_WIDTH, DECK_HEIGHT)],
                                  # 1, "Red", "Green")
        canvas.draw_line(((idx + 1) * each_x, 0), ((idx + 1) * each_x, 100), 2, 'Black')
        if exposed[idx]:
            canvas.draw_text(str(number_list[idx]),((idx + 1) * each_x - each_x / 3 * 2, each_y), 36, 'White')
        


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)

frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric