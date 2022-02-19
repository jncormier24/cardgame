import random
import card

class Deck:
    
    def __init__(self):
        self.all_cards = []
        
        for suit in card.Card.suits:
            for rank in card.Card.ranks:
                self.all_cards.append(card.Card(suit, rank))
        
    def draw_card(self):
        return self.all_cards.pop()
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def __len__(self):
        return len(self.all_cards)
    
