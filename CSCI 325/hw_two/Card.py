class Card:
        """
        A class that defines a playing card in a standard 52 card deck

        Methods
        ============
        __str__(self) -> str
            return a printable string representation of a cards
        get_value(self) -> str
            returns the value of a particular card
        to_string(self) -> str
            returns a string format of the card

        """
        def __init__(self, value:str):
            """
            Constructor for Card class
            Attributes
            ===========
            value : str

            Paramaters
            ============
            value : str
            """
            # self.suit = suit
            self.value = value

        def __str__(self):
            """ Displays cards contents as a String

                EX: Card("hearts", "2") --> "This Card is the 2 of hearts"
            """
            return f"{self.value}"

        def to_string(self) -> str:
            """ Method ot convert value of CARD into string """
            return str(self.value)

        # def get_suit(self) -> str:
        #     """ Instance method that returns the SUIT of an instance of a card"""
        #
        #     return self.suit

        def get_value(self) -> str:
            """ Instance method that returns the VALUE of a card"""
            return self.value


# hand = Card("5")
# print(isinstance(hand, Card))
# print(hand.get_value())
