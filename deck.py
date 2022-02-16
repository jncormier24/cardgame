class Deck():
    
    def __init__(self, cards):
        self.cards = cards
        
    def drawCard(self):
        topcard = self.cards.pop()
        return topcard

    def __len__(self):
        return len(self.cards)