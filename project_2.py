import random
randNumber=random.randint(1,100)
guessNumber=None
guesses=0
while(guessNumber!=randNumber):
    guessNumber=int(input("Enter the Number: "))
    if(guessNumber==randNumber):
        print("You guessed it right!")
    else:
        if(guessNumber>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a higher number")
    guesses=guesses+1
print(f"You guessed the number in {guesses} guesses")

with open("highscore2.txt","r") as f:
    highscore=int(f.read())

    if(guesses<highscore):
        print("You have just broken High Score!")
        with open("highscore2.txt","w") as f:
            f.write(str(guesses))

        
