from dataclasses import dataclass, field
from card import Card
from suit import Suit
from rank import Rank

@dataclass
class Deck:
    """Class representing a deck of cards"""
    cards: list[Card] = field(default_factory=list)

    def fill_deck_with_all_cards(self) -> None:
        """Fill the deck with all 52 cards."""
        self.cards.clear()
        for suit in Suit:
            for rank in Rank:
                card = Card(suit=suit, rank=rank)
                self.cards.append(card)