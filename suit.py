from enum import Enum

class Suit(Enum):
    """Enum representing card suits with their values."""
    HEARTS = ('Hearts', 4)
    DIAMONDS = ('Diamonds', 3)
    CLUBS = ('Clubs', 2)
    SPADES = ('Spades', 1)