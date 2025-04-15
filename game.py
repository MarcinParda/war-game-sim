from dataclasses import dataclass
from deck import Deck

@dataclass
class Game:
    round: int = 0
    main_deck: Deck = None

    def start(self) -> None:
        """Start the game."""
        self.main_deck = Deck()
        self.main_deck.fill_deck_with_all_cards()
        print(f"Main deck filled with {len(self.main_deck.cards)} cards.")
        # Print all cards in the deck
        for card in self.main_deck.cards:
            print(card)