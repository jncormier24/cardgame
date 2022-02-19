import card
import deck

class Player():
    """
    creates a plyer class
    """
    def __init__(self, name):
        """
        initialize the player class
        """
        self.name = name
        self.all_cards = []

    def remove_card(self):
        """
        play a card from the top of the deck
        """
        return self.all_cards.pop(0)

    def add_cards(self, cards):
        """
        add n number of cards to the bottom of the players hand
        """
        if type(cards) == type([]):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)

    def showcards(self):
        for acard in self.all_cards:
            print(acard)

    def __str__(self):
        """
        stringify the player data
        """
        return f'Player {self.name} has {len(self.all_cards)} cards'
    