# template for "Stopwatch: The Game"

# define global variables
import simplegui
times = 0
x = 0
y = 0
interval = 100
switch = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = 0
    seconds = 0
    tenthseconds = 0
    total = t
    if t > 0:
        totalseconds = int(total // 10)
        minutes = totalseconds // 60
        seconds = totalseconds - minutes * 60
        tenthseconds = total - totalseconds * 10
    return minutes, seconds, tenthseconds
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global switch
    switch = True

def Stop():
    global switch, x, y,times
    switch = False
    y = y + 1
    m, s, ts = format(times)
    if s % 5 == 0 and ts == 0:
        x = x + 1 	
    

def Reset():
    global switch, x, y,times
    switch = False
    times = 0
    x = 0
    y = 0
    

# define event handler for timer with 0.1 sec interval
def create_timer():
    global switch, times
    if switch:
        times = times + 1
    m, s, ts = format(times)
    if m >= 10:
        Reset()

# define draw handler
def draw(canvas):
    global times, success, tried
    m, s, ts = format(times)
    message = "%d:%02d.%d" % (m, s, ts)
    canvas.draw_text(message, (80, 110), 50, "White")
    grade = "%d/%d" % (x, y)
    canvas.draw_text(grade, (220, 25), 30, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)

# register event handlers
frame.add_button("Start", Start,150)
frame.add_button("Stop", Stop, 150)
frame.add_button("Reset", Reset, 150)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, create_timer)

# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric
