import random
# Spades
spades = ['As', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks']

# Hearts
hearts = ['Ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh']

# Diamonds
diamonds = ['Ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd']

# Clubs
clubs = ['Ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc']

# Combine all lists into a single full deck
full_deck = spades + hearts + diamonds + clubs

def round(deck):
    tem_deck = deck
    player1 = []
    player2 = []
    player3 = []
    player4 = []
    player5 = []
    comm_cards = []
    for i in [player1, player2, player3, player4, player5]:
        for j in range(2):
            random_index = random.randrange(len(tem_deck))
            card = tem_deck[random_index]
            i.append(card)
    for i in range(5):
        random_index = random.randrange(len(tem_deck))
        card = tem_deck[random_index]
        comm_cards.append(card)
    

    players = {
        'Player 1': player1, 
        'Player 2': player2,
        'Player 3': player3,
        'Player 4': player4,
        'Player 5': player5
                }
    return comm_cards, players



# Display the results
if __name__ == "__main__":
    cards = round(full_deck)
    print(cards[0])
    print(cards[1])
