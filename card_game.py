import random

# Define ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Create deck
deck = [rank + " of " + suit for rank in ranks for suit in suits]

# Shuffle deck
random.shuffle(deck)

# Draw a card for player 1 and 2
p1 = deck.pop()
p2 = deck.pop()

print(f"Player 1 drew: {p1}")
print(f"Player 2 drew: {p2}")

# Function to determine value of card
def card_value(card):
    rank = card.split(' ')[0]
    if rank == 'J':
        return 11
    elif rank == 'Q':
        return 12
    elif rank == 'K':
        return 13
    elif rank == 'A':
        return 14
    else:
        return int(rank)

# Compare values
if card_value(p1) > card_value(p2):
    print("🏆 Player 1 wins!")
elif card_value(p1) < card_value(p2):
    print("🏆 Player 2 wins!")
else:
    print("🤝 It's a tie!")
