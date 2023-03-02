from Card import Card
from random import randint
class Deck:
    """
        A class that defines a deck of playing cards that can be added to and have cards removed from.

        Methods
        ===========
        __str__(self) -> str
            returns a string representation of DECK
        construct_deck(self) -> None
            constructs a standard 52 playing card Deck
        get_deck_length(self) -> int
            returns the length of a Deck
        add_card(self, new_card:Card)
            adds a Card to a Deck
        draw_card(self) -> Card
            removes card from deck and returns the removed cards


    """

    def __init__(self):
        """Constructs a DECK with construct_deck() method
           Attributes
           ===========
           cards_in_deck : list
        """
        self.cards_in_deck = []
        self.construct_deck()

    def __str__(self) -> str:
        """ Method to return an string representation of deck that can be printed"""
        return_string = ""
        for card in self.cards_in_deck:
            return_string += card.__str__() + ", "
        return return_string

    def construct_deck(self):
        """ Method to construct standard 52 card deck"""
        for suit in range(4):
            for value in range(2,15):#############
                    self.cards_in_deck.append(Card(value))

    def get_deck_length(self) -> int:
        """ Method return the length of the deck """
        return len(self.cards_in_deck)

    def add_card(self, new_card:Card):
        """ Method to add a card to a deck manually
                not used in gofish but good function to have
        """
        if not isinstance(new_card, Card):
            raise TypeError("This method only accepts type \'Card\' for function parameter")
        self.cards_in_deck.append(new_card)

    def draw_card(self) -> Card:
        """ Method to take a card from the deck and return the CARD removed """
        if len(self.cards_in_deck) > 0:
            drawn_card = self.cards_in_deck[randint(0, len(self.cards_in_deck)-1)]
            self.cards_in_deck.remove(drawn_card)
            return drawn_card
        else:
            print("Deck is out of cards")
            return None



# deck_52 = Deck()
# print(deck_52)
# print(deck_52.get_deck_length())
# for num in range(53):
#     deck_52.draw_card()
# print(deck_52.draw_card())
# print(deck_52.get_deck_length())
# deck_52.add_card(Card("7"))
# print(deck_52.get_deck_length())
