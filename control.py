import entity, time

dealer = entity.Dealer()
player = entity.Player()

# This sets up inventories
cards = [] # This is all of the cards
dealerinventory = [] # This is for the dealer
playerinventory = [] # This is for the player

# First Step is for the dealer to generate the cards, shuffle, and then deal the cards
# Second Step is the repeated process of the player seeing the cards and the total, and the choice of hit or stand,
#
# if "hit" is chosen, the dealer will give the player one additional card and checks the player's total 
# (If the total is greater than 21, the player gets busted, otherwise it repeats back to the chocies).
#
# if "stand" is chosen, the dealer shows its cards and compares the player's total and its total (whoever has the higher count wins)
# NOTE: if the player gets 21 in the first round, the player gets a blackjack.
#
# When the game is over with either a victory or a bust, then the game will ask the player if they want to play again, if they enter "yes",
# the game restarts, if the player chooses "no", then the game ends.

class UniversalControl():

    def __init__(self, dealertotalnumber, playertotalnumber, inBeginning):
        self.dealertotalnumber = dealertotalnumber
        self.playertotalnumber = playertotalnumber
        self.inBeginning = inBeginning

    # This starts the game
    def startGame(self):
        print("Welcome to BlackJack, a card game where you pick two cards from the dealer and combine the values to see if you or the dealer have the higher value")
        print()
        dealer.generateCards(cards)
        dealer.shuffleCards(cards)
        dealer.dealCards(cards, dealerinventory, playerinventory)
        self.dealertotalnumber = dealer.countCards(dealerinventory)
        time.sleep(2)
    
    # This runs the game
    def playGame(self):
        self.playertotalnumber = player.countCards(playerinventory)
        player.displayCards(playerinventory, self.playertotalnumber)
        finished = player.checkBust(self.playertotalnumber)
        if finished == False:
            repeat = True
            while repeat:
                print("Do you want to hit, or stand?")
                print('Enter "hit" if you want to hit')
                print('Enter "stand" if you want to stand')
                choice = input("ENTER HERE: ")
                if choice.lower() == "hit":
                    print()
                    player.hit(cards, playerinventory)
                    self.inBeginning = False
                    repeat = False
                    return True
                elif choice.lower() == "stand":
                    print()
                    player.compareCards(dealerinventory, playerinventory, self.dealertotalnumber, self.playertotalnumber)
                    time.sleep(1)
                    player.checkResult(self.dealertotalnumber, self.playertotalnumber, self.inBeginning)
                    repeat = False
                    return False
                else:
                    print()
                    print("Sorry, wrong input")
                    print()
    
    # This asks if you want to play again
    def willContinue(self):
        time.sleep(1)
        repeat = True
        while repeat:
            print("Do you want to play again?")
            print('Enter "yes" if you want to play again')
            print('Enter "no" if you want to stop')
            choice = input("ENTER HERE: ")
            if choice.lower() == "no":
                print()
                print("Thank you for playing!")
                repeat = False
                return False
            elif choice.lower() != "yes":
                print()
                print("Sorry, wrong input")
                print()
            else:
                print()
                print("Restarting...")
                print()
                dealer.clearCards(cards, dealerinventory, playerinventory)
                time.sleep(2)
                repeat = False
                return True