from dataclasses import dataclass, field
from deck import Deck
from card import Card


class Game:
    def __init__(self) -> None:
        """Initialize the game with a 2 shuffled decks for each player."""

        self.round = 0
        self.war_count = 0
        self.game_over = False

        whole_deck = Deck()
        whole_deck.fill_deck_with_all_cards()
        print(f"Main deck filled with {len(whole_deck.cards)} cards.")

        whole_deck.shuffle()
        print("Deck shuffled.")

        self.bet = Deck()
        self.player1_deck = Deck()
        self.player2_deck = Deck()

        decks = whole_deck.split_deck(num_players=2)
        self.player1_deck, self.player2_deck = decks
        print("Decks split between players.")

    def show_decks(self) -> None:
        """Display the decks of both players."""
        print("Player 1's deck:")
        self.player1_deck.show_deck()
        print("\nPlayer 2's deck:")
        self.player2_deck.show_deck()

    def show_round(self) -> None:
        """Display the current round number."""
        print(f"Current round: {self.round}")

    def check_game_winner(self) -> str | None:
        """Check if there is a winner and who it is."""
        if self.player1_deck.is_empty():
            return "Player 2"
        elif self.player2_deck.is_empty():
            return "Player 1"
        else:
            return None

    def fight(self, player1_card: Card, player2_card: Card) -> None:
        """Determine the winner of a round."""
        self.bet.append_card(player1_card)
        self.bet.append_card(player2_card)

        print(
            f"Player 1 plays {player1_card.rank.name} of {player1_card.suit.name}.")
        print(
            f"Player 2 plays {player2_card.rank.name} of {player1_card.suit.name}.")
        if player1_card.rank.value > player2_card.rank.value:
            print("Player 1 wins this round.")
            self.player1_deck.extend_deck(self.bet)
            self.bet.cards.clear()
        elif player1_card.rank.value < player2_card.rank.value:
            print("Player 2 wins this round.")
            self.player2_deck.extend_deck(self.bet)
            self.bet.cards.clear()
        else:
            print("It's a WAR! Adding 2 cards from each deck to the bet.")
            self.war_count += 1
            if len(self.player1_deck.cards) < 3 and len(self.player2_deck.cards) < 3:
                print("Not enough cards for war from both sides. Game over.")
                self.game_over = True
                return
            elif len(self.player1_deck.cards) < 3:
                print("Not enough cards for war from Player 1. Player 2 wins the game.")
                self.player1_deck.append_card(player1_card)
                self.player2_deck.append_card(player2_card)
                self.game_over = True
                return
            elif len(self.player2_deck.cards) < 3:
                print("Not enough cards for war from Player 2. Player 1 wins the game.")
                self.player1_deck.append_card(player1_card)
                self.player2_deck.append_card(player2_card)
                self.game_over = True
                return
            self.bet.append_card(self.player1_deck.cards.pop(0))
            self.bet.append_card(self.player1_deck.cards.pop(0))
            self.bet.append_card(self.player2_deck.cards.pop(0))
            self.bet.append_card(self.player2_deck.cards.pop(0))

            player1_card = self.player1_deck.cards.pop(0)
            player2_card = self.player2_deck.cards.pop(0)

            self.fight(player1_card, player2_card)

    def play_round(self) -> None:
        """Play a round of the game."""
        self.round += 1
        print("-" * 20)
        print(f"Round {self.round} starts!")

        player1_card = self.player1_deck.cards.pop(0)
        player2_card = self.player2_deck.cards.pop(0)
        self.fight(player1_card, player2_card)

    def start(self) -> None:
        """Start the game simulation."""
        print("Game started!")
        while self.game_over is False:
            winner = self.check_game_winner()
            if winner:
                print(f"{winner} wins the game!")
                self.game_over = True
            else:
                self.play_round()
        print("-" * 20)
        print("Game over!")
        print(f"Total rounds played: {self.round}")
        print(f"Total wars: {self.war_count}")
        # print(f"Player 1's remaining cards: {len(self.player1_deck.cards)}")
        # print(f"Player 2's remaining cards: {len(self.player2_deck.cards)}")
        # self.player1_deck.show_deck()
        # self.player2_deck.show_deck()
        # print(f"Deck 1 has duplicates: {self.player1_deck.has_duplicates()}")
        # print(f"Deck 2 has duplicates: {self.player2_deck.has_duplicates()}")
