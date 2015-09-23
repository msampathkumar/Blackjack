from random import random, shuffle
from pprint import pprint
from util import get_my_cards_scores, blackjack_player, print_game_players

cards_scores = get_my_cards_scores()
get_card_values = lambda x : cards_scores[x]
count = len

def game(players=2):
    players = [ blackjack_player(i) for i in range(int(players + 1 )) ]
    # setting dealer
    players[-1].is_dealer = True
    if count(players) < 2 :
        return 'No game : No players'
    #
    all_cards = cards_scores.keys()
    shuffle(all_cards)
    cards_count = 2 # first turn
    while all_cards:
        active_players = [ _ for _ in players if not _.is_frozen ]
        # dealer buster
        if [ _ for _ in active_players if _.is_dealer and _.is_busted ]:
            return 'Game stopped: our dealer busted', print_game_players(players)
        # no players
        if len(active_players) == 0:
            return 'Game stopped: no active players', print_game_players(players)
        # no cards
        if ( count( active_players ) * cards_count ) > count(all_cards) :
            return 'Game stopped: cards are over  ', print_game_players(players)
        # cards distribution
        for _ in active_players:
            card = all_cards.pop()
            _.add_card(card)
            if cards_count == 2:
                cards_count = 1
                card = all_cards.pop()
                _.add_card(card)
        # is_winner
        tmp = [ _ for _ in players if _.is_winner ]
        if tmp:
            return 'Game stopped: We have a winner', tmp, print_game_players(players)



def main():
    print ('='*65)
    print ('Black Jack Game')
    print ('='*65)
    while True:
        players = input('Enter no. players(enter 0 to exit) : ')
        if players == 0: break
        game(players)
    print ('='*65)
    raw_input('Thank you for your time :)')


if '__name__' == '__main__':
    main()




