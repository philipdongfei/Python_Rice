# Mini-project #6 - Blackjack
#http://www.codeskulptor.org/#user40_mZaUAmboAK_3.py
import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
message = ""
score = 0
Dealer_Pos = (40, 260)
Player_Pos = (40, 426)

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}



# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        # if pos[0] == Dealer_Pos[0] and pos[1] == Dealer_Pos[1]:
            # if in_play:
                # canvas.draw_image(card_back, [CARD_BACK_SIZE[0] + CARD_BACK_CENTER[0], CARD_BACK_CENTER[1]], CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
            # else:
                # canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        # else:    
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.card_list = []	# create Hand object

    def __str__(self):
        # return a string representation of a hand
        strCards = ''
        for card in self.card_list:
            strCards += str(card)
            strCards += ' '
        return strCards

    def add_card(self, card):
        self.card_list.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0	# compute the value of the hand, see Blackjack video
        is_Ace = False
        for card in self.card_list:
            value += VALUES[card.get_rank()]
            if card.get_rank() is 'A':
                is_Ace = True
        if is_Ace:
            if value + 10 <= 21:
                value += 10
        return value
                
    def draw(self, canvas, pos):
        card_pos = [0, 0]
        for idx in range(len(self.card_list)):	# draw a hand on the canvas, use the draw method for cards
            card_pos[0] = pos[0] + idx * CARD_SIZE[0]
            card_pos[1] = pos[1]
            self.card_list[idx].draw(canvas, card_pos)
            idx = idx + 1
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.card_list = []	# create a Deck object
        for suit in SUITS:
            for rank in RANKS:
                c = Card(suit, rank)
                self.card_list.append(c)
        
                
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.card_list)    # use random.shuffle()

    def deal_card(self):
        card = self.card_list.pop(len(self.card_list) - 1)	# deal a card object from the deck
        return card
    
    def __str__(self):
        # return a string representing the deck
        strCards = ""
        for card in self.card_list:
            strCards += str(card)
            strCards += ' '
        return strCards
            

# define desk, player, dealer
deck = Deck()
player = Hand()
dealer = Hand()

#define event handlers for buttons
def deal():
    global outcome, in_play, score, player, dealer, deck, message
    
    # your code goes here
    outcome = ""
    message = ""
    if in_play:
        outcome = "You lost this round"
        score = score - 1 
    deck = Deck()
    player = Hand()
    dealer = Hand()
    deck.shuffle()
    for i in range(4):
        card = deck.deal_card()
        if i % 2 != 0:
            player.add_card(card)
        else:
            dealer.add_card(card)
    message = 'Hit or stand?'
    print outcome
    
    in_play = True

def hit():
    # replace with your code below
    global outcome, in_play, score, deck, player, dealer, message
    # if the hand is in play, hit the player
    
    if player.get_value() <= 21:
        c = deck.deal_card()
        player.add_card(c)
        print 'player: ', str(player), player.get_value()
    # if busted, assign a message to outcome, update in_play and score
    if player.get_value() > 21:
        outcome = 'You have busted'
        message = 'New deal?'
        in_play = False
        print outcome
        score -= 1
    else:
        message = 'Hit or stand?'
#        outcome = 'player: '
#        outcome += str(player) 
#        print outcome
        
       
def stand():
    # replace with your code below
    global outcome, in_play, player, dealer, deck, score, message
    message = "New deal?"
    if player.get_value() > 21:
        outcome = 'You have busted'
        in_play = False
        
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    else:
        while dealer.get_value() < 17:
            c = deck.deal_card()
            dealer.add_card(c)       
        print 'dealer: ', str(dealer)
    # assign a message to outcome, update in_play and score
        if dealer.get_value() > 21:
            outcome = 'Dealer have busted'
            score += 1
        elif player.get_value() <= dealer.get_value():
            outcome = 'You lost!'
            score -= 1
        else:
            outcome = 'You win!'
            score += 1
        in_play = False
        print outcome
        

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global player, dealer, outcome, message
#    card = Card("S", "A")
#    card.draw(canvas, [300, 300])
    
    dealer.draw(canvas, Dealer_Pos)
    player.draw(canvas, Player_Pos)
    canvas.draw_text(message,[Player_Pos[0] + 200, Player_Pos[1] - 24], 24, "Black")
    canvas.draw_text("Blackjack", [100, 100], 36, "Blue")
    canvas.draw_text("score:" + str(score), [350, 100], 24, "Black")
    canvas.draw_text("Dealer", [Dealer_Pos[0], Dealer_Pos[1] - 24], 24, "Black")
    canvas.draw_text(outcome, [Dealer_Pos[0] + 200, Dealer_Pos[1] - 24], 24, "Black")
    canvas.draw_text("Player", [Player_Pos[0], Player_Pos[1] - 24], 24, "Black")
    if in_play:
        canvas.draw_image(card_back, [CARD_BACK_SIZE[0] + CARD_BACK_CENTER[0], CARD_BACK_CENTER[1]], CARD_BACK_SIZE, [Dealer_Pos[0] + CARD_BACK_CENTER[0], Dealer_Pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

    
    



# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric