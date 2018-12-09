from Deck import Deck
from Hand import Hand
from Chips import Chips


playing = True
deck = None
player_hand = None
dealer_hand = None


def take_bet(chips):
    while True:
        try:
            chips.bet = int (input("Please enter your bet: "))
        except ValueError:
            print("Value Error, input must by integer!")
        else:
            if chips.total <= chips.bet:
                print("You don't have enough chips credits!")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        move = input("Please choose next move: 'h' for hit or 's' for stand: ")
        if move.lower() == 'h':
            hit(deck, hand)

        elif move.lower() == 's':
            print("Dealer is playing.")
            playing = False
            continue
        else:
            print("Incorrect input!")
            continue
        break


def show_some(player, dealer):
    print("Dealer's hand: \n")
    print('<back of a first card> ', dealer.cards[1])
    print("Player's hand: \n")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print("Dealer's hand: \n")
    for card in dealer.cards:
        print(card)
    print("\nDealer's hand value: ", dealer.value)
    print("Player's hand: \n")
    for card in player.cards:
        print(card)
    print("\nPlayer's hand value: ", player.value)


def player_busts(chips):
    print("Player busts! \n")
    chips.lose_bet()


def player_wins(chips):
    print("Player wins! \n")
    chips.win_bet()


def dealer_busts(chips):
    print("Dealer busts! \n")
    chips.lose_bet()


def dealer_wins(chips):
    print("Dealer wins!\n")
    chips.win_bet()


def push():
    print("Tie game. Push.\n")


def create_and_shuffle_deck():
    global deck
    deck = Deck()
    deck.shuffle_deck()


def create_player_hand():
    global player_hand
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())


def create_dealer_hand():
    global dealer_hand
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())


def play_game():
    global playing, player_hand, dealer_hand, deck
    while True:
        print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11.')

        create_and_shuffle_deck()
        create_player_hand()
        create_dealer_hand()

        player_chips = Chips()
        take_bet(player_chips)
        show_some(player_hand, dealer_hand)

        while playing:

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player_hand)
            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_busts(player_chips)
                break

        # If Player hasn't busted, play Dealer's hand
        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            # Test different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_chips)

            else:
                push()

            # Inform Player of their chips total
            print("\nPlayer's winnings stand at total of ", player_chips.total)

        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break

        break


if __name__ == '__main__':
     play_game()




































