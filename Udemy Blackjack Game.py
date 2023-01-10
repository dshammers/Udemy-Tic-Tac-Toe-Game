#card class
#suit,rank,integer value
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10,'Ace':[11,1]}
class Card():
    def __init__(self,rank,suit):
        self.suit=suit.capitalize()
        self.rank=rank.capitalize()
        self.value=values[rank.capitalize()]
        
    def __str__(self):
        return self.rank+' of '+self.suit
    
class Deck():
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_card=Card(rank,suit)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop[0]

class Player():
    def __init__(self,name,bankroll):
        self.name=name
        self.bankroll=bankroll
        self.hand=[]
        
    def bet_in_play(self):
        self.bet_in_play=[0]
    
    def bet(self,bet):
        bankroll-=bet
        self.bet_in_play.append(bet)

    def winning(self,amount):
        self.winning=self.bankroll=bankroll+amount

    def hit(self,new_card):
        self.hand.append(new_card)

class Dealer():
    def __init__(self):
        self.dealers_hand=[]
        
    def hit(self,added_card):
        self.dealers_hand.append(added_card)

new_deck=Deck()
new_deck.shuffle()

dealer=Dealer()

#game logic
while True:
    player_name=input("What's your name?")
    player_bankroll=int(input("How much money do you have?"))
    player_1=Player(player_name,player_bankroll)

    play_game=True

    begin_game=input(f"Hi {player_name}, Would you like to play Blackack? y/n")
    if begin_game=='y':
        play_game=True
    if begin_game=='n':
        play_game=False
        break


    while play_game:
        if player_1.bankroll==0:
            print("You're out of money!")
            play_game=False
            break

        while player_1.bet_in_play==0:
            bet_amount=int(input("How much would you like to bet?"))
            if isinstance(bet_amount,int)==True and bet_amount <= player_1.bankroll:
                    player_1.bet(bet_amount)
                    break
            elif isinstance(bet_amount,int)==True and bet_amount > player_1.bankroll:
                    print("You don't have that much!")


        if len(dealer.dealers_hand)<2:
            player_1.hit(new_deck.deal_one)
            dealer.hit(new_deck.deal_one)

        print(f'{player_name} has {player_1.hand}')
        print(f'dealer is showing {dealer.dealers_hand[0]}')

        player_turn=True
        dealer_turn=False

        while player_turn:
                choice=input('Would you like to hit or stay?').lower()
                if choice=='hit':
                    player_1.hit(new_deck.deal_one())
                    if sum(player_1.hand.value)>21:
                        print(player_1.hand)
                        print('Player has busted! Dealer wins')
                        player_turn=False
                        play_game=False
                        break
                    print(player_1.hand)
                if choice=='stay':
                    print(player_1.hand)
                    player_turn=False
                    dealer_turn=True
                    break

        while dealer_turn:
            if sum(dealer.dealers_hand.value)<17:
                dealer.hit(new_deck.deal_one())
            if sum(dealer.dealers_hand.value)>21:
                 print(dealer.dealers_hand)
                 print('Dealer has busted! Player wins!')
                 dealer_turn=False
                 play_game=False
                 break
            else:
                if sum(player_1.hand.value) > sum(dealer.dealers_hand.value):
                    print ('Player 1 beat the dealer!')
                    player_1.winning(player_1.bet_in_play*2)
                    dealer_turn=False
                    break
                if sum(player_1.hand.value) < sum(dealer.dealers_hand.value):
                    print ('Player 1 loses!')
                    player_1.bet_in_play=0
                    dealer_turn=False
                    break
                if sum(player_1.hand.value)==sum(dealer.dealers_hand.value):
                    print ('Push!')
                    player_1.winning(player_1.bet_in_play)
                    dealer_turn=False
                    break