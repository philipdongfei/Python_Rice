# Cipher

import simplegui
import random

#CIPHER = {'a': 'x', 'b': 'c', 'c': 'r', 'd': 'm', 'e': 'l'}
CIPHER = {}
LETTERS = "abcdefghijklmnopqrstuvwxyz"

message = ""


def init():
   
    list_letters = list(LETTERS)
    random.shuffle(list_letters)
    for ch in LETTERS:
        CIPHER[ch] = list_letters.pop()

# Encode button
def encode():
    global message
    emsg = ""
    for ch in message:
        emsg += CIPHER[ch]
    print message, "encodes to", emsg
    message = emsg

# Decode button
def decode():
    global message
    dmsg = ""
    for ch in message:
        for key, value in CIPHER.items():
            if ch == value:
                dmsg += key
    print message, "decodes to", dmsg

# Update message input
def newmsg(msg):
    global message
    message = msg
    label.set_text(msg)
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Cipher", 2, 200, 200)
frame.add_input("Message:", newmsg, 200)
label = frame.add_label("", 200)
frame.add_button("Encode", encode)
frame.add_button("Decode", decode)
init()

# Start the frame animation
frame.start()
