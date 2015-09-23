'''
utils package for black-jack game
---------------------------------

'''
from pprint import pprint

def get_my_cards_scores():
    suits = list('CSHD')
    cards = list('AKQJ') + range(2, 11)
    cards_scores = dict()
    for x in suits:
        for y in cards:
            if y == 'A':
                cards_scores[ str(x) + str(y)] = [ 1, 11 ]
            elif y in list('KQJ'):
                cards_scores[ str(x) + str(y)] = [ 10 ]
            else:
                cards_scores[ str(x) + str(y)] = [ int(y) ]
    return cards_scores

class blackjack_player():
    def __init__(self, id=1):
        self.name = str(id)
        self.cards = [ ]
        self.scores = [0]
        #
        self.is_dealer = False 
        #
        self.is_frozen = False 
        self.is_busted = False
        self.is_winner = False

    def add_card(self, card):
        self.cards.append(card)
        self.__update_scores__(card)
        self.__game_checkers__()
        
    def __repr__(self):
        show  = 'ID : %s; cards : %s; scores : %s' % ( self.name, str(self.cards), str(self.scores) )
        return show
    
    def __update_scores__(self, card):
        card_values = get_card_values(card)
        self.scores = set([ x + y for x in list(self.scores) for y in card_values ])
        
    def __game_checkers__(self):
        for _ in self.scores:
            if _ >= 17:
                self.is_frozen = True 
            if _ > 21:
                self.is_busted = True
            if _ == 21:
                self.is_winner = True

def print_game_players(players):
    players.sort( key = lambda _ : max(_.scores), reverse=True)
    frozen = []
    busted = []
    winners = []
    for _ in players:
        if _.is_winner:
            winners.append(_)
        elif _.is_busted:
            busted.append(_)
        elif _.is_frozen:
            frozen.append(_)
    others = [ _ for _ in players if _ not in set( winners + frozen + busted ) ]
    if [ _ for _ in players if _.is_dealer and _.is_busted ]:
        # no change for busted
        # all players become busted
        winners = winners + frozen
        frozen = []
    print ('='*25 )
    if winners:
        print ('winners')
        pprint(winners)
    if busted:
        print ('busted')
        pprint(busted)
    if frozen:
        print ('frozen')
        pprint(frozen)
    if others:
        print ('others')
        pprint(others)

def print_player(player):
    print 'is_winner :', player.is_winner
    print 'is_frozen :', player.is_frozen
    print 'is_busted :', player.is_busted
    print 'is_dealer :', player.is_dealer
    print (player)
    print '-' * 75

cards_n_scores = get_my_cards_scores()

get_card_values = lambda x : cards_n_scores[x]

# -------------------------------------------

def cards_players(cards=['C5'], reply=False):
    p = blackjack_player(id=1)
    for _ in cards : p.add_card( _ )
    if reply:
        return p
    else:
        print_player(p)

def testing01():
    cards_players([]) # initilisation
    cards_players(['C2']) # testing add_card - function
    cards_players(['C2', 'S3']) # testing if scores are updating fine 
    cards_players(['C2', 'S3', 'H4', 'D7']) # 17 limiting factors
    cards_players(['C2', 'S3', 'H4', 'D8']) # 17 limiting factors
    cards_players(['C2', 'S3', 'H4', 'D9']) # 17 limiting factors
    cards_players(['C2', 'S6', 'H4', 'D9']) # 17 limiting factors
    cards_players(['CA', 'S7', 'H7', 'D7']) # 17 limiting factors
    cards_players(['C2', 'S6', 'H7', 'D9']) # 17 limiting factors
    cards_players(['CA']) # testing A's multitple scores
    cards_players(['CA', 'S3']) # testing A's multiple score addition

def testing02():
    p = cards_players([], True ) # initilisation
    assert max( p.scores ) == 0
    p.add_card('C5')
    assert max( p.scores ) == 5
    p.add_card('DA')
    assert max( p.scores ) == 16 and p.is_frozen == False
    p.add_card('SK')
    assert max( p.scores ) == 26


test = False
if test:
    testing01()
    
    testing02()



