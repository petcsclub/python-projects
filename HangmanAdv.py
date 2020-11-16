#Hangman - Advanced - Ethan Kang

"""
CHECKLIST:
1. The user can make the same mistake *no longer
2. The user can enter more than one letter (always punished) *no longer
3. The answer is limited to one word (due to spaces) *no longer
4. Case sensitivity *no longer exists
5. Answer is the same every time *no longer
"""

"""setting up"""
import random #answer selects from a list of words instead of just one for variability (5)
wordList = ["I Love Aardvarks", "I Hate Aardvarks", "Aardvarks Are OK"]
answer = wordList[random.randint(0,len(wordList)-1)]
numMistakes = 0
manList = [" \n o","\n/", "|","\\","\n /","\\"]

ansList = [] 
for i in range(len(answer)): 
    ansList.append(answer[i].lower()) #the answer, along with all instances where the user's guess is checked or added to a list is forced to be lower case to bypass case sensitivity (4)
mistakes = [] 
guessedAns = [] 
for i in range(len(answer)): #Allows for spaces in the answer (3)
    guessedAns.append("_")
    if (ansList[i] == " "):
        guessedAns[i] = " "


"""gameplay"""
playAgain = True
while (playAgain):
    while (guessedAns != ansList and numMistakes < 7):
        correctGuess = False 
        print (guessedAns) 
        for i in range(numMistakes):
            print(manList[i], end = "")
        print ("\nmistakes: " + str(mistakes))
        guess = input("guess a letter: ") 

        if (len(guess) > 1): #Checks that the guess is only 1 letter and not repeated, correctGuess' use is to re-loop the code (1, 2)
            print("Please only guess 1 letter!")
            correctGuess = True
        if (guess.lower() in mistakes or guess.lower() in guessedAns):
            print("You already guessed that!")
            correctGuess = True
            
        for i in range(len(answer)): 
            if (guess.lower() == ansList[i]): 
                guessedAns[i] = guess.lower()
                correctGuess = True
        if (not correctGuess): 
            numMistakes+=1
            mistakes.append(guess.lower())
        print()
    if (numMistakes == 7): 
        print ("Better luck next time, you lose!")
    else:
        print ("Great job, you win!")
    retry = input("Would you like to play again? (y/n - any other answer will be interpeted as yes")
    if (retry.lower() == "n"):
        print("Goodbye!")
        playAgain = False
   
