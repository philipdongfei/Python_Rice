# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [-40.0 / 60.0,  5.0 / 60.0]
paddle1_vel = [0,  0]
paddle2_vel = [0,  0]
score1 = 0
score2 = 0
paddle1_pos = [PAD_WIDTH, HEIGHT / 2]
paddle2_pos = [WIDTH - PAD_WIDTH, HEIGHT / 2] 


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[0] = random.randrange(120, 240) / 60.0
    ball_vel[1] = random.randrange(60, 180) / 60.0    
    if direction == LEFT:
        ball_vel[0] = - abs(ball_vel[0])
    elif direction == RIGHT:
        ball_vel[0] = abs(ball_vel[0])
    flag = random.randint(0, 1)
    
    if flag == 0:
        ball_vel[1] = abs(ball_vel[1])
    else:
        ball_vel[1] = - abs(ball_vel[1])
                          

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = [PAD_WIDTH, HEIGHT / 2]
    paddle2_pos = [WIDTH - PAD_WIDTH, HEIGHT / 2] 
    paddle1_vel = [0,  0]
    paddle2_vel = [0,  0]
    spawn_ball(random.randint(LEFT, RIGHT))
    
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
   
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    
    paddle1_pos[0] += paddle1_vel[0]
    if (paddle1_pos[1] + paddle1_vel[1]) > HALF_PAD_HEIGHT and (paddle1_pos[1] + paddle1_vel[1]) < (HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos[1] += paddle1_vel[1]
    
    paddle2_pos[0] += paddle2_vel[0]
    if (paddle2_pos[1] + paddle2_vel[1]) > HALF_PAD_HEIGHT and (paddle2_pos[1] + paddle2_vel[1]) < (HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos[1] += paddle2_vel[1]
    # draw paddles
    canvas.draw_line((paddle1_pos[0],paddle1_pos[1] - HALF_PAD_HEIGHT), (paddle1_pos[0] - PAD_WIDTH,paddle1_pos[1]- HALF_PAD_HEIGHT), 2, 'White')
    canvas.draw_line((paddle1_pos[0],paddle1_pos[1] + HALF_PAD_HEIGHT), (paddle1_pos[0] - PAD_WIDTH,paddle1_pos[1]+ HALF_PAD_HEIGHT), 2, 'White')
    canvas.draw_line((paddle2_pos[0],paddle2_pos[1] - HALF_PAD_HEIGHT), (paddle2_pos[0] + PAD_WIDTH,paddle2_pos[1]- HALF_PAD_HEIGHT), 2, 'White')
    canvas.draw_line((paddle2_pos[0],paddle2_pos[1] + HALF_PAD_HEIGHT), (paddle2_pos[0] + PAD_WIDTH,paddle2_pos[1]+ HALF_PAD_HEIGHT), 2, 'White')
 
    
    
    # determine whether paddle and ball collide
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
        if ball_pos[1] >= paddle1_pos[1] - HALF_PAD_HEIGHT and ball_pos[1] <= (paddle1_pos[1] + HALF_PAD_HEIGHT):
            ball_vel[0] = - (ball_vel[0] * 1.1)
            
        else:
            spawn_ball(RIGHT)
            score2 = score2 + 1
    elif ball_pos[0] >= (WIDTH - BALL_RADIUS - PAD_WIDTH):
        if ball_pos[1] >= paddle2_pos[1] - HALF_PAD_HEIGHT and ball_pos[1] <= (paddle2_pos[1] + HALF_PAD_HEIGHT):
            ball_vel[0] = - (ball_vel[0] * 1.1)
            
        else:
            spawn_ball(LEFT)
            score1 = score1 + 1
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]   
    
    # draw scores
    canvas.draw_text(str(score1) + 'vs' + str(score2), (WIDTH / 2 - 30, 30), 30, 'Red')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 5
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] += acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] -= acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game, 100)


# start frame
new_game()
frame.start()
