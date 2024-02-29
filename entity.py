import random, event

ev = event.Event()

# This module is basically where the actions, abilities, and events happen based on the dealer or the player

# This are the actions that both the dealer and the player can do
class Both():
    # This counts the cards
    def countCards(self, inv):
        total = 0
        for i in range(len(inv)):
            total += inv[i][1]
        return total
    
    # This checks the result and compares the totals if the player chooses to "stand"
    def checkResult(self, dealertotal, playertotal, beginbool):
        blackjack = False

        if beginbool == True:
            if playertotal == 21:
                blackjack = True
                print("you got a BLACKJACK!")
                print()
        
        if dealertotal > 21:
            if blackjack == False:
                print("dealer bust")
                print()
        else:
            if playertotal > dealertotal:
                if blackjack == False:
                    print("you win!")
                    print()
            elif playertotal == dealertotal:
                if blackjack == False:
                    print("tied")
                    print()
            else:
                if blackjack == False:
                    print("dealer wins! :(")
                    print()
    
    # This displays to the player the cards that you had and the cards that the dealer had, including the total numbers for both.
    def compareCards(self, dealerinv, playerinv, dealertotal, playertotal):
        card_info = ""
        for i in range(len(playerinv)):
            card_info = card_info + str(playerinv[i][0]) + " "
            if i == len(playerinv)-1:
                card_info = card_info + str(playerinv[i][1]) + "."
            elif i == len(playerinv)-2:
                card_info = card_info + str(playerinv[i][1]) + ", and "
            else:
                card_info = card_info + str(playerinv[i][1]) + ", "

        print(f"You have the cards: {card_info}")
        print()
        card_info = ""
        for i in range(len(dealerinv)):
            card_info = card_info + str(dealerinv[i][0]) + " "
            if i == len(dealerinv)-1:
                card_info = card_info + str(dealerinv[i][1]) + "."
            elif i == len(dealerinv)-2:
                card_info = card_info + str(dealerinv[i][1]) + ", and "
            else:
                card_info = card_info + str(dealerinv[i][1]) + ", "

        print(f"The dealer has the cards: {card_info}")
        print()
        print(f"Your total number is {playertotal}")
        print(f"Dealer's total number is {dealertotal}")
        print()

# This is the dealer exclusive actions
class Dealer(Both):

    # This generates the cards
    def generateCards(self, mycards):
        suit = " "
        for i in range(1, 5):
            if i == 1:
                suit = "club"
            elif i == 2:
                suit = "diamond"
            elif i == 3:
                suit = "heart"
            elif i == 4:
                suit = "spade"
            else:
                 suit = "invalid"
            for j in range(1, 14):
                mycards.append([suit, j])
    
    # This shuffles the cards
    def shuffleCards(self, mycards):
        random.shuffle(mycards)
    
    # This deals the cards to both the dealer and the player (They have inventories)
    def dealCards(self, mycards, dealerinv, playerinv):
        dealerinv.append(mycards.pop(0))
        dealerinv.append(mycards.pop(0))
        playerinv.append(mycards.pop(0))
        playerinv.append(mycards.pop(0))
        print("Both you and the dealer have been dealt with 2 cards")
        print()
    
    # This clears the inventory of the cards
    def clearCards(self, mycards, dealerinv, playerinv):
        dealerinv.clear()
        playerinv.clear()
        mycards.clear()

# This is you, the player
class Player(Both):
    # This displays the player's cards
    def displayCards(self, inv, total):
        card_info = ""
        for i in range(len(inv)):
            card_info = card_info + str(inv[i][0]) + " "
            if i == len(inv)-1:
                card_info = card_info + str(inv[i][1]) + "."
            elif i == len(inv)-2:
                card_info = card_info + str(inv[i][1]) + ", and "
            else:
                card_info = card_info + str(inv[i][1]) + ", "

        print(f"You have the cards: {card_info}")
        print(f"Your total number is {total}")
        print()
    
    # This is if the player chooses "hit"
    def hit(self, mycards, inv):
        inv.append(mycards.pop(0))

    # This automatically checks if the player's total is over 21, if it is, the player has bust
    def checkBust(self, playertotal):
        if playertotal > 21:
            print("You bust")
            print()
            return True
        else:
            return False
