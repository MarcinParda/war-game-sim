from dataclasses import dataclass, field
from card import Card
from suit import Suit
from rank import Rank


@dataclass
class Deck:
    """Class representing a deck of cards"""
    cards: list[Card] = field(default_factory=list)

    def show_deck(self) -> None:
        """Display the cards in the deck."""
        for card in self.cards:
            card_str = f"{card.rank.name} of {card.suit.name}"
            print(card_str)

    def clear_deck(self) -> None:
        """Clear the deck of cards."""
        self.cards.clear()

    def append_card(self, card: Card) -> None:
        """Append a card to the deck."""
        self.cards.append(card)

    def extend_deck(self, deck: 'Deck') -> None:
        """Append another deck to this deck."""
        self.cards.extend(deck.cards)

    def is_empty(self) -> bool:
        """Check if the deck is empty."""
        return len(self.cards) == 0

    def has_duplicates(self) -> bool:
        """Check if the deck has duplicate cards."""
        seen = set()
        for card in self.cards:
            card_str = f"{card.rank.name} of {card.suit.name}"
            if card_str in seen:
                return True
            seen.add(card_str)
        return False

    def fill_deck_with_all_cards(self) -> None:
        """Fill the deck with all 52 cards."""
        self.cards.clear()
        for suit in Suit:
            for rank in Rank:
                card = Card(suit=suit, rank=rank)
                self.append_card(card)

    def shuffle(self) -> None:
        """Shuffle the deck of cards."""
        import random
        random.shuffle(self.cards)

    def split_deck(self, num_players: int) -> list['Deck']:
        """Split the deck into a specified number of players."""
        decks: list[Deck] = [Deck() for _ in range(num_players)]
        for i, card in enumerate(self.cards):
            decks[i % num_players].cards.append(card)
        return decks
