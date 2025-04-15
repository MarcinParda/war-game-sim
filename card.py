from dataclasses import dataclass, field
from suit import Suit
from rank import Rank

@dataclass
class Card:
    """Class representing a playing card."""
    suit: Suit
    rank: Rank
