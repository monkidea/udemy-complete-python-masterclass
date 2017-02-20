import random

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
# =================================================================================

def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tk.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    # for each suit, retrieve the image for the cards
    for suit in suits:
        for card in range(1, 11):
            name = 'cards_{0}/{1}_{2}.{0}'.format(extension, str(card), suit)
            image = tk.PhotoImage(file=name)
            card_images.append((card, image,))

        for card in face_cards:
            name = 'cards_{0}/{1}_{2}.{0}'.format(extension, str(card), suit)
            image = tk.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    # pop the next card off the top of the deck
    next_card = deck.pop(0)
    # add the image to a Label and display the label
    tk.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the card's face value
    return next_card


def score_hand(hand):
    # Calculate the total score of all cards in a list
    # Only one Ace can have the value 11, and this will be reduced to 1 if the hand would bust.
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust, check for ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return(score)


def deal_dealer():
    deal_card(dealer_card_frame)


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")

    # global player_score
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # # if we would bust, check if there is an ace and subtract
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer wins!")
    # print(locals())

# ===================================================================================
root = tk.Tk()
root.title("Black Jack")
root.geometry("640x480")
root.configure(background="green")

# Set up the screen and frames for the dealer and player
result_text = tk.StringVar()
results = tk.Label(root, textvariable=result_text)
results.grid(row=0, column=0, columnspan=3)

card_frame = tk.Frame(root, relief='sunken', borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tk.IntVar()
tk.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tk.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# Embedded frame to hold the card images
dealer_card_frame = tk.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tk.IntVar()
tk.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tk.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# Embedded frame to hold the card images
player_card_frame = tk.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tk.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tk.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

# Load cards
cards = []
load_images(cards)

# Create a new deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)

# Create the list to store dealer's and player's hands
dealer_hand = []
player_hand = []












root.mainloop()