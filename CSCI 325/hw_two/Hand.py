from Card import Card
from random import randint
from Deck import Deck

class Hand:
    """
        A class that defines a HAND in a game of go fish

        Methods
        ===========
        get_hand_length -> int
            returns length of hands
        get cards_in_hand -> list
            returns the cards in a hand
        hand_to_list_of_values -> list
            returns a list of the values in a hand
        add_card -> None
            adds card to a players hand
        clear_hand -> None
            empties a players hands
        give_card -> None
            removes card from one player and gives to another
        display -> str
            returns a string that shows the players hand and num of cards of opponent

    """
    def __init__(self, game_deck:Deck):
        """ Constructs a HAND object that represents the cards the player has
        Attributes
        ===========
        cards_in_hand : list
        Paramaters
        ==========
        game_deck:DECK
            deck used to create HANDS"""
        self.cards_in_hand = []
        self.game_deck = game_deck
        for num in range(7):
            card = self.game_deck.draw_card()
            self.cards_in_hand.append(card)

    def get_hand_length(self) -> int:
        """ Method to return the length of a players HAND"""
        return len(self.cards_in_hand)

    def get_cards_in_hand(self) -> list:
        """ Method to getr all cards in the hand"""
        return self.cards_in_hand

    def hand_to_list_of_values(self) -> list:
        """ Method to return a list of all the values of cards in hand"""
        value_list = []
        for card in self.cards_in_hand:
            value_list.append(card.get_value())
        return value_list

    # def get_hand_values(self):
    #     values = []
    #     for card in self.cards_in_hand:
    #         values.append(card.get_value())
    #         return values

    def add_card(self, desired_card:Card):
        """ Method to add card to a players HAND """
        self.cards_in_hand.append(desired_card)
    def clear_hand(self):
        """ Method to empty game HANDS to play again """
        self.cards_in_hand.clear()

    def give_card(self,receiver_hand, card:Card):
        """ Method that allows a player to give a card to another player """
        print("Giving all Cards: " + card.to_string())
        # 6,4,6,2,1,1,7
        index = 0
        for hand_card in self.cards_in_hand:
            if str(hand_card.get_value()) == str(card.get_value()):
                self.cards_in_hand.pop(index)
                receiver_hand.add_card(card)
            index += 1


    def display(self, comp_hand) -> str:
        """ Method Display the cards of a HAND and number of cards in opponents"""
        print("The opponent has", comp_hand.get_hand_length(), "cards")
        print("Your cards are: ")

        card_counts = {} # key:value of card value:num of value in hand
        player_cards = ""
        if(len(self.cards_in_hand) < 1):
            print("You have no cards")
        else:
            for card in self.cards_in_hand:
                player_cards += card.to_string() + ", "
        print(player_cards)

#
# deck_52 = Deck()
# print(deck_52.get_deck_length())
# print("---")
# my_hand = Hand(deck_52)
# comp_hand = Hand(deck_52)
# print(deck_52.get_deck_length())
# my_hand.display(comp_hand)
# comp_hand.display(my_hand)
