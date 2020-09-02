'''
This program is an example solution of what your mad libs game could look like! The code is simple implementation of the game. Are there any ways you can improve it? :)
'''

# Colour class for fancy text
# Syntax: bcolours.BLUE or GREEN + STRING + bcolours.END
class bcolours:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'

print("\nWelcome to PETCS Mad Libs!\n")
print('''Info --------------------->
Copy/paste a custom 1 paragraph story that follows the legend!
If you want to input a .txt file, make sure the .txt file is in the same directory (folder) as the python script!

Recommended story length is 100 - 500 words, but I won't stop you in testing the limits :) 

Legend for user input:
ADJ - Ask for an adjective
NOUN - Ask for a noun
VERBP - Ask for a plural verb
VERBS - Ask for a singular verb
VERBD - Ask for a past tense verb
ADVERB - Ask for a adverb
* Legend is case sensitive!
''')
  
keepPlaying = True
repeat = False

# Template story
story_temp = []
copy = []

# Allows the user to upload a custom story
def upload_story():
  if repeat:
    return copy[:]
  else:
    story = ""
    while True:
      choice = input("Upload .txt file or manually (txt/man): ").lower()
      # This code assumes you put in the right .txt name.
      # However, if you put the wrong name, it will throw an error. How can you work around that? 
      # Hint: Try Except
      if choice == "txt":
        # Although we didn't teach open(), it is a built-in function for opening files
        open_story = open(input("Enter file name: "), "r")
        story = open_story.read()
        break
      elif choice == "man":
        story = input("Type/paste your story here: ")
        break
      else:
        print("Invalid choice, try again!")
  # Split is a method that 'splits' a string into a list
  # By default, it seperates by whitespace characters
  return story.split()

# Asks the user if they want to repeat the last story inputted
def repeat_story():
  while True:
      repeatPrev = input("Repeat last entered story? (y/n): ").lower()
      if repeatPrev == 'y':
        return True
      elif repeatPrev == 'n':
        return False

# Sometimes an input prompt will be muddled with punctuation, so we should remove it!
def remove_punct(word):
  # You could also use string module for a more comprehensive list of punctuation
  punct = {".", ",", "?", "/", "!"}
  for ch in word:
    if ch in punct:
      word = word.replace(ch, "")
      return [word, ch]
  return [word, ""]

# This function stores user input
def get_user_input(story):
  # Checks if a part of the story needs input
  for i in range(len(story)):
    word = remove_punct(story[i]);
    if word[0] == "ADJ":
      story[i] = bcolours.BLUE + input("Enter an adjective: ") + bcolours.END + word[1]
    elif word[0] == "NOUN":
      story[i] = bcolours.BLUE + input("Enter a noun: ") + bcolours.END + word[1]
    elif word[0] == "VERBP":
      story[i] = bcolours.BLUE + input("Enter a verb (plural): ") + bcolours.END + word[1]
    elif word[0] == "VERBS":
      story[i] = bcolours.BLUE + input("Enter a verb (singular): ") + bcolours.END + word[1]
    elif word[0] == "VERBD":
      story[i] = bcolours.BLUE + input("Enter a verb (past tense): ") + bcolours.END + word[1]
    elif story[i] == "ADVERB":
      story[i] = bcolours.BLUE + input("Enter an adverb: ") + bcolours.END + word[1]
  return story

# This function outputs the user's story
def output_user_story(story):
  # \n outputs a newline
  print("\nHere is your Story!")
  # Alternative way of joining a list is using the .join method
  print(' '.join(story))
  print("\nTHE END\n")

# Main game loop
while keepPlaying == True:
  story_temp = upload_story()
  copy = story_temp[:]
  print()
  story = get_user_input(story_temp)
  output_user_story(story)
  # Allows user to play again
  while True:
    playAgain = input("Play again? (y/n): ").lower()
    if playAgain == 'n':
      keepPlaying = False
      break
    elif playAgain == 'y':
      repeat = repeat_story()
      break
    else:
      print("Invalid input, try again!")

print("\nThanks for playing!")