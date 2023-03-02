#Author: Harris Tanweer
from Card import Card
from random import randint
from Deck import Deck
from Hand import Hand
from Computer import Computer
class GoFishGame:
     """ A class to define the game GoFish
        Methods
        =========
        play_again() -> bool
            asks user if they want to play again
        score()
            adds up the points in each hand
        go_fish -> Card
            draws a card from the deck
        ask_user()
            asks the user to pick a card from opponent
        ask_comp()
            asks computer to pick a card from user
        welcome_message()
            displays a message introducing the game
        is_game_over()
            checks if game is over

     """
     def __init__(self):
         """ Constructs a GAME object to be used to play go fish against a
         computer """

         #Welcome message at the beginning of a game
         self.welcome_message()
         #create game deck
         self.game_deck = Deck()

            # print(self.game_deck.get_deck_length())

            # print(self.game_deck)

         #deal cards to players hands
         self.player_hand = Hand(self.game_deck)
         self.comp = Computer(self.game_deck)
            #print(self.game_deck.get_deck_length())

         while(not self.is_game_over()):
             self.player_hand.display(self.comp.get_hand())
             self.ask_user()
             if self.is_game_over():
                 break
             input("Press enter to continue")
             self.comp.request_card(self.player_hand)
             input("Press enter to continue")
             self.player_hand.display(self.comp.get_hand())

         print("The game is over!")
         self.score()
         if self.play_again():
             newer_game = GoFishGame()



     def play_again(self) -> bool:
         """prompts user if they wish to play again"""

         while(True):
             resp = input("Would you like to play again? (Y/N): ")
             resp = resp.upper()

             if resp == "Y":
                 self.player_hand.clear_hand()
                 self.comp.get_hand().clear_hand()
                 self.game_deck = Deck()
                 return True
             if resp == "N":
                 return False
             print("Invalid input")


     def score(self):
         """Scores players once game is over"""

         computer_score = 0
         for card in self.comp.get_hand().hand_to_list_of_values():
             computer_score += card

         player_score = 0
         for card in self.player_hand.hand_to_list_of_values():
             player_score += card

         print("Your score is ", player_score)
         print("The computer's score is ", computer_score)

         if player_score > computer_score:
             print("You win! Well done!")
         elif player_score < computer_score:
             print("You lost. Better luck next time!")
         else:
             print("You tied! Good match!")


     def go_fish(self, hand) -> Card:
         """Prints go fish and draws a card"""

         print("Go Fish!")

         if(self.game_deck.get_deck_length() > 0):
             card = self.game_deck.draw_card()
             hand.add_card(card)
         else:
             return

         if hand is self.player_hand:
             print("Now adding " + card.to_string() + " to your hand.")
             # print(self.player_hand.display(self.computer_hand))
         else:
             print("The computer has drawn a card.")

         return card
     # def comp_go_fish(self, hand):
     #     """Prints go fish and draws a card"""
     #     print("Go Fish!")
     #     if(deck.get_deck_length() > 0):
     #         card = deck.draw_card()
     #         hand.add_card(card)
     #     else:
     #         return
     #         print("The computer has drawn a card.")
     #     return card


     def ask_user(self):
         """prompts user ito pick a card from computer and either adds to hand
         or draws from deck"""
         invalid = True

         while(invalid):

             print("What card would you like? ")
             resp = input("Enter one of your cards: " + str(set(self.player_hand.hand_to_list_of_values())) + ": ")

             try:
                 if int(resp) in self.player_hand.hand_to_list_of_values():
                     invalid = False
                 else:
                     print("Invalid response")
             except ValueError:
                 print("Please choose a valid card from your Hand \"", resp, "\" is not acceptable")

         self.comp.add_memo_moves(Card(int(resp)))
         if int(resp) in self.comp.get_hand().hand_to_list_of_values():
             print("Computer has card")
             self.comp.get_hand().give_card(self.player_hand, Card(int(resp)))
         else:
             print("Computer does not have card")
             self.go_fish(self.player_hand)


     def ask_comp(self):
         """Computer requests a card from the user and either adds to hand or
         draws from deck """

         potential_cards = []
         for card_value in set(self.comp.get_hand().hand_to_list_of_values()):
             count = self.comp.get_hand().hand_to_list_of_values().count(card_value)
             if count != 4:
                 potential_cards.append(Card(card_value))
         if (len(potential_cards) > 0):
             index = randint(0, len(potential_cards) - 1)
             resp = potential_cards[index]
         else:
             resp = self.comp.get_hand()[randint(0, len(self.comp.get_hand().get_cards_in_hand()) - 1)]


         print("The computer is requesting", resp)
         input("Press enter to continue.")

         if (int(resp.get_value()) in self.player_hand.hand_to_list_of_values()):
             print("You have this card")
             self.player_hand.give_card(self.comp.get_hand(), resp)
         else:
             print("You do not have card")
             self.go_fish(self.comp.get_hand())






     def welcome_message(self):
         """ defines a method that welcomes the user and explains rules"""

         print("Welcome to the game 'Go Fish'!")
         print("Your goal is to collect as many ")
         print("4-of-a-kind, or 'books', as you can.")
         print("Books are scored based on the card ")
         print("value with Aces being the highest and ")
         print("'2' being the lowest. Now let's play! Good luck!")
         input("Press enter to continue")

     def is_game_over(self) -> bool:
         """Determines if game is over"""
         if self.game_deck.get_deck_length() > 0:
             return False
         for card_value in set(self.player_hand.hand_to_list_of_values()):
             count = self.player_hand.hand_to_list_of_values().count(card_value)
             if count != 4:
                 return False
         for card_value in set(self.comp.get_hand().hand_to_list_of_values()):
             count = self.comp.get_hand().hand_to_list_of_values().count(card_value)
             if count != 4:
                 return False
         return True



#main method of the gofish game
if __name__ == "__main__":
    new_game = GoFishGame()
