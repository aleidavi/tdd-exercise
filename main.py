VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    total_score = 0
    
    for card in hand:
        
        if card in VALID_CARDS:
            if card.isinstance(card, int):
                total_score += VALID_CARDS[card]
            
            elif card in VALID_CARDS[9:-1]:
                total_score += 10
            
            elif card == VALID_CARDS[-1]:

                