#Author: Harris Tanweer
from Card import Card
from random import randint
from Deck import Deck
from Hand import Hand

class Computer:
     """ A class to define the game GoFish
        Methods
        =========
        request_card() -> none
            requests a card from the user using 4 different methods
        add_memo_moves() -> none
            adds user past moves to computers "memory"
        get_hand -> none
            returns the computers hand to be used in GoFishGame.py
        comp_go_fish() -> none
            draws a card for the computer and says go fish


     """

    def __init__(self, deck):
        """ contructs a computer object"""
        self.game_deck = deck
        self.computer_hand = Hand(deck)
        self.memorized_moves = []

    def request_card(self, player_hand):
        """ Method that requests a card from the user"""
        #pick highest - 0
        #pick closest to book - 1
        #pick users - 2
        #random - 4

        #pick highest - 0
        random = randint(0,4)
        if(random == 0):
            print("highest")
            potential_cards = []
            #doesn't ask for books
            for card_value in set(self.computer_hand.hand_to_list_of_values()):
                count = self.computer_hand.hand_to_list_of_values().count(card_value)
                if count != 4:
                    potential_cards.append(Card(card_value))
            values = self.computer_hand.hand_to_list_of_values()
            high = 0
            #knows win criteria aka highest points win
            if (len(potential_cards) != 0):
                for card in potential_cards:
                    if int(card.get_value()) > high:
                        high = int(card.get_value())
                        high_card = card
                resp = high_card
            else:
                resp = self.computer_hand.get_cards_in_hand()[randint(0,len(self.computer_hand.get_cards_in_hand())-1)]

    #pick closest to book - 1
        elif(random == 1):
            print("closest to book")
            potential_cards = []
            for card_value in set(self.computer_hand.hand_to_list_of_values()):
                count = self.computer_hand.hand_to_list_of_values().count(card_value)
                if count != 4:
                    potential_cards.append(Card(card_value))
            dict = {}
            if  len(potential_cards) != 0:
                for card in potential_cards:
                    dict[card.get_value()] = dict.get(card.get_value(),0) + 1
                    freq_card = max(dict, key=dict.get)
                resp = Card(freq_card)
            else:
                resp = self.computer_hand.get_cards_in_hand()[randint(0,len(self.computer_hand.get_cards_in_hand())-1)]

    #pick memorized users moves- 2
        elif(random == 2):
            print("users")
            potential_cards = []
            for card_value in set(self.computer_hand.hand_to_list_of_values()):
                count = self.computer_hand.hand_to_list_of_values().count(card_value)
                if count != 4:
                    potential_cards.append(Card(card_value))

                past_cards = []
                for card in self.memorized_moves:
                    if card in potential_cards:
                        past_cards.append(card)
                if len(past_cards) != 0:
                    resp = past_cards[randint(0,len(past_cards)-1)]
                elif len(potential_cards) == 0:
                    resp = self.computer_hand.get_cards_in_hand()[randint(0,len(self.computer_hand.get_cards_in_hand())-1)]
                else:
                    resp = potential_cards[randint(0,len(potential_cards)-1)]
    #pick a random move - 4
        else:
            print("random")
            potential_cards = []
            for card_value in set(self.computer_hand.hand_to_list_of_values()):
                count = self.computer_hand.hand_to_list_of_values().count(card_value)
                if count != 4:
                    potential_cards.append(Card(card_value))
                if len(potential_cards) != 0:
                    resp = potential_cards[randint(0,len(potential_cards)-1)]
                else:
                    resp = self.computer_hand.get_cards_in_hand()[randint(0,len(self.computer_hand.get_cards_in_hand())-1)]

        print("The computer is requesting", resp)
        input("Press enter to continue.")

        if (int(resp.get_value()) in player_hand.hand_to_list_of_values()):
            print("You have this card")
            player_hand.give_card(self.computer_hand, resp)
        else:
            print("You do not have card")
            self.comp_go_fish(self.computer_hand)

    def add_memo_moves(self, card):
        """" Method that records users previous moves"""
        self.memorized_moves.append(card.get_value())

    def get_hand(self):
        """returns hand of computer"""
        return self.computer_hand

    def comp_go_fish(self, hand):
        """Prints go fish and draws a card"""
        print("Go Fish!")

        if(self.game_deck.get_deck_length() > 0):
            card = self.game_deck.draw_card()
            hand.add_card(card)
        else:
            return
        print("The computer has drawn a card.")
        return card


    # def pick_highest(self):
    #     potential_cards = []
    #     for card_value in set(self.computer_hand.hand_to_list_of_values()):
    #         count = self.computer_hand.hand_to_list_of_values().count(card_value)
    #         if count != 4:
    #             potential_cards.append(Card(card_value))
    #     values = self.computer_hand.hand_to_list_of_values()
    #     high = 0
    #     for card in potential_cards:
    #         if int(card.get_value()) > high:
    #             high = int(card.get_value())
    #             high_card = card
    #     return high_card
