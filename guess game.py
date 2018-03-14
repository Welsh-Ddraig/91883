from random import randint

def main():
    print ("Welcome to Guess game")
    print ("Pick your difficulty level. Easy (10) Medium (20) or Hard (50) or EXTREME (100)")
    print("Each difficulty has more numbers but you get 2 more gueses per level with 3 your start point.")
    difficultSetting = input("So enter E for Easy, M for Medium, H for Hard or X for eXtreme.").lower()
    
    if difficultSetting == "e":
        game_mode(10, 3)
    elif difficultSetting == "m":
        game_mode(20, 5)
    elif difficultSetting =="h":
        game_mode(50, 7)
    elif difficultSetting == "x":
        game_mode(100, 9)
    else:
        print("FAILED to select correct difficulty Goodbye!")

def game_mode(maxnumber, maxlives):
    guessNum = randint(1,maxnumber)
    
    userGuess = int(input("What is your guess??? "))
    while maxlives != 0:
        if userGuess == guessNum:
            print("Correct Guess well done.")
            end_game(maxlives)
        elif userGuess < guessNum:
            print("To Low try again. ")
            maxlives = maxlives - 1
        elif userGuess > guessNum:
            print("To high try again. ")
            maxlives = maxlives - 1
        else:
            print("No Guess.")
        userGuess = int(input("What is your guess??? "))
    end_game(maxlives)
    
def end_game(livesLeft):
    print ("Well done you won with", livesLeft,"Lives left.")
    playAgain = input("Would you like ot play again? Y/N ").lower()
    
    if playAgain == "y":
        main()
    else:
        print("Goodbye.")
    
main() #comment 
