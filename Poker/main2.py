import itertools
from collections import Counter
from main import round, full_deck


# Map ranks to numerical values for easy comparison
RANKS = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

def evaluate_five_card_hand(cards):
    """
    Evaluates a single 5-card hand and returns a tuple used for ranking:
    (Hand_Rank_Index, Tie_Breaker_Values)
    """
    ranks = sorted([RANKS[c[0]] for c in cards], reverse=True)
    suits = [c[1] for c in cards]

    is_flush = len(set(suits)) == 1
    is_straight = False
    straight_high = 0

    # Check for straight
    unique_ranks = sorted(list(set(ranks)))
    if len(unique_ranks) == 5 and unique_ranks[-1] - unique_ranks[0] == 4:
        is_straight = True
        straight_high = unique_ranks[-1]
    elif set(ranks) == {14, 5, 4, 3, 2}: # Ace-low straight
        is_straight = True
        straight_high = 5

    rank_counts = Counter(ranks)
    counts = sorted(rank_counts.values(), reverse=True)

    # Hand Ranking Logic
    if is_straight and is_flush:
        return (8, straight_high) # Straight Flush
    elif counts == [4, 1]:
        return (7, [r for r, count in rank_counts.items() if count == 4][0],
                [r for r, count in rank_counts.items() if count == 1][0]) # Four of a Kind
    elif counts == [3, 2]:
        return (6, [r for r, count in rank_counts.items() if count == 3][0],
                [r for r, count in rank_counts.items() if count == 2][0]) # Full House
    elif is_flush:
        return (5, ranks) # Flush
    elif is_straight:
        return (4, straight_high) # Straight
    elif counts == [3, 1, 1]:
        return (3, [r for r, count in rank_counts.items() if count == 3][0],
                sorted([r for r, count in rank_counts.items() if count == 1], reverse=True)) # Three of a Kind
    elif counts == [2, 2, 1]:
        pairs = sorted([r for r, count in rank_counts.items() if count == 2], reverse=True)
        kicker = [r for r, count in rank_counts.items() if count == 1][0]
        return (2, pairs, kicker) # Two Pair
    elif counts == [2, 1, 1, 1]:
        pair = [r for r, count in rank_counts.items() if count == 2][0]
        kickers = sorted([r for r, count in rank_counts.items() if count == 1], reverse=True)
        return (1, pair, kickers) # One Pair
    else:
        return (0, ranks) # High Card

def get_hand_name(score, cards):
    """
    Returns the string name of the poker hand.
    """
    rank_idx = score[0]
    
    if rank_idx == 8:
        if score[1] == 14: # Straight high is 14 (Ace high)
            ranks = sorted([RANKS[c[0]] for c in cards])
            if ranks == [10, 11, 12, 13, 14]:
                return "Royal Flush"
        return "Straight Flush"
    elif rank_idx == 7:
        return "Four of a Kind"
    elif rank_idx == 6:
        return "Full House"
    elif rank_idx == 5:
        return "Flush"
    elif rank_idx == 4:
        return "Straight"
    elif rank_idx == 3:
        return "Three of a Kind"
    elif rank_idx == 2:
        return "Two Pair"
    elif rank_idx == 1:
        return "One Pair"
    else:
        return "High Card"

def find_best_hands(community_cards, players_hands):
    """
    Finds the best 5-card combination out of 7 for each player, evaluates 
    the hand name, and generates reasoning.
    """
    results = {}
    
    for player, hole_cards in players_hands.items():
        all_cards = community_cards + hole_cards
        best_hand = None
        best_score = (-1,)

        # Texas Hold'em allows using any 5 cards from the 7 available
        for comb in itertools.combinations(all_cards, 5):
            score = evaluate_five_card_hand(comb)
            if score > best_score:
                best_score = score
                best_hand = comb
                
        # Determine the name of the hand
        hand_name = get_hand_name(best_score, best_hand)
        
        # Build reasoning based on which cards came from hole vs community
        hole_used = [c for c in best_hand if c in hole_cards]
        comm_used = [c for c in best_hand if c in community_cards]
        
        reasoning = f"Uses {len(hole_used)} hole card(s) {hole_used} and {len(comm_used)} community card(s) {comm_used}."

        results[player] = {
            'best_hand': list(best_hand),
            'score': best_score,
            'raw_hole': hole_cards,
            'hand_name': hand_name,
            'reasoning': reasoning
        }
        
    # Sort the players from best to worst hand
    sorted_players = sorted(results.items(), key=lambda x: x[1]['score'], reverse=True)
    return sorted_players

# --- Example Game Scenario ---

cards = round(full_deck)
community_cards = cards[0]
players = cards[1]
# Run the evaluation
game_results = find_best_hands(community_cards, players)

print("--- Game Results (Ranked from Best to Worst) ---\n")
for rank, (player, data) in enumerate(game_results, 1):
    print(f"#{rank} {player}:")
    print(f"  Hole Cards   : {data['raw_hole']}")
    print(f"  Hand Name    : {data['hand_name']}")
    print(f"  Best Hand    : {data['best_hand']}")
    print(f"  Reasoning    : {data['reasoning']}")
    print("-" * 75)

