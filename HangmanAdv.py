#Hangman - Advanced - Ethan Kang

"""setting up"""
import random #answer selects from a list of words instead of just one for variability (5)
wordList = ["I Love Aardvarks", "I Hate Aardvarks", "Aardvarks Are OK"]
manList = [" \n o","\n/", "|","\\","\n/"," \\"]

"""gameplay"""
playAgain = True
while (playAgain):#Loop allows for replayability
    answer = random.choice(wordList)
    numMistakes = 0
    mistakes = [] 
    guessedAns = [] 
    for i in range(len(answer)): #Allows for spaces in the answer
        guessedAns.append("_")
        if (answer[i] == " "):
            guessedAns[i] = " "
    
    while ("".join(guessedAns) != answer and numMistakes < 7):
        correctGuess = False 
        print (" ".join(guessedAns)) 
        for i in range(numMistakes):
            print(manList[i], end = "")
        print ("\nmistakes: " + ", ".join(mistakes))
        guess = input("guess a letter: ").lower()

        if (len(guess) != 1): #Checks that the guess is only 1 letter and not repeated, correctGuess' use is to re-loop the code=
            print("Please only guess 1 letter!")
            continue
        if (guess in mistakes or guess in guessedAns):
            print("You already guessed that!")
            continue
            
        for i in range(len(answer)): 
            if (guess == answer[i].lower()): 
                guessedAns[i] = answer[i]
                correctGuess = True
        if (not correctGuess): 
            numMistakes+=1
            mistakes.append(guess)
        print()
    if (numMistakes == 7): 
        print ("Better luck next time, you lose!")
    else:
        print ("Great job, you win!")
    retry = input("Would you like to play again? (y/n) ").lower() #Allows for replayability using boolean retry
    while retry != "y":
        if (retry == "n"):
            print ("Goodbye!")
            playAgain = False
            break
        retry = input("Please input either y or n ").lower()
