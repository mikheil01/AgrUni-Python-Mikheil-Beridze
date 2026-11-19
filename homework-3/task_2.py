import random

suits = ["clubs (♣)", "diamonds (♦)", "hearts (♥)", "spades (♠)"]
ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
card = random.choice(deck)

print(card)
