#Hangman - Easy - Ethan Kang

"""
LIMITS:
1. The user can make the same mistake
2. The user can enter more than one letter (always punished)
3. The answer is limited to one word (due to spaces)
4. Case sensitivity
"""

"""setting up"""
answer = "aardvark" #answer
lives = 6 #lives

ansList = [] #converts the chosen answer to a list
for i in range(len(answer)): 
    ansList.append(answer[i])
mistakes = [] #list of mistakes
guessedAns = [] #visual display of the user's guesses
for i in range(len(answer)): #fills guessedAns with blanks the length of the answer
    guessedAns.append("_")


"""gameplay"""
while (guessedAns != ansList and lives > 0):
    correctGuess = False #checks whether the user made a correct guess (see Ln 26, 27)
    print (guessedAns) #visual display of user's guesses, remaining lives, and mistakes
    print ("lives: " + str(lives))
    print ("mistakes: " + str(mistakes))
    guess = input("guess a letter: ") #user inputs guess here
    
    for i in range(len(answer)): #checks to see if the guess is in the word
        if (guess == ansList[i]): #replaces correct guess in correct position
            guessedAns[i] = guess
            correctGuess = True
    if (not correctGuess): #the user's mistake loses them a life and gets added to the list of mistakes
        lives -= 1
        mistakes.append(guess)
    print() #space for clarity ingame

if (lives == 0): #win/lose messages
    print ("Better luck next time, you lose!")
else:
    print ("Great job, you win!")
    
    
