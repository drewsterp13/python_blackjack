import control

cmd = control.UniversalControl(0, 0, True)

# USE THIS FILE TO RUN THE PROGRAM

# The class and method that runs the entire game
class Key():
    def main(self):
        repeatGame = True
        loopGame = True
        while repeatGame:
            cmd.startGame()
            while loopGame:
                loopGame = cmd.playGame()
                if loopGame == False:
                    break
            repeatGame = cmd.willContinue()
            if repeatGame == False:
                break
            else:
                loopGame = True

key = Key()

key.main()