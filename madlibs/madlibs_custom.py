'''
This program is an example solution of what your mad libs game could look like! The code is simple implementation of the game. Are there any ways you can improve it? :)
'''

# Colour class for fancy text
# Syntax: bc.BLUE or GREEN + STRING + bc.END
class bc:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'

def upload_story(copy, repeat):
  """
  Allows the user to upload a custom story

  Parameters:
  copy (list): Copy of previous story
  repeat (bool): True if user wants to repeat last story

  Returns:
  story (list): The story the user will play next
  """
  if repeat:
    return copy
  else:
    while True:
      story = input("Type/paste your story here (Don't press enter until you are finished): ")
      while True:
        # If they accidently pressed enter, they are allowed to input again
        confirm = input("Confirm input (y/n): ").lower()
        if confirm == 'y':
          # Split is a method that 'splits' a string into a list
          return story.split()
        elif confirm == 'n':
          print()
          break
        else:
          print("Invalid input, try again!")

def get_user_input(story_temp):
  """
  This function stores the final story by replacing legend words with user input
  
  Parameters:
  story (list): The list that will be looped through

  Returns:
  list: The final story with user input
  """
  story = story_temp[:]
  for i in range(len(story)):
    if "ADJ" in story[i]:
      story[i] = story[i].replace("ADJ", bc.BLUE + input("Enter an adjective: ") + bc.END)
    elif "NOUN" in story[i]:
      story[i] = story[i].replace("NOUN", bc.BLUE + input("Enter a noun: ") + bc.END)
    elif "VERBP" in story[i]:
      story[i] = story[i].replace("VERBP", bc.BLUE + input("Enter a verb (plural): ") + bc.END)
    elif "VERBS" in story[i]:
      story[i] = story[i].replace("VERBS", bc.BLUE + input("Enter a verb (singular): ") + bc.END)
    elif "VERBD" in story[i]:
      story[i] = story[i].replace("VERBD", bc.BLUE + input("Enter a verb (past tense): ") + bc.END)
    elif "ADVERB" in story[i]:
      story[i] = story[i].replace("ADVERB", bc.BLUE + input("Enter an adverb: ") + bc.END)
    elif "EMOJI" in story[i]:
      story[i] = story[i] = story[i].replace("EMOJI", input("Enter an emoji: "))
  return story

# Variables that control the game
keepPlaying = True
repeat = False

# Template story
story_temp = []

# Welcoming statements
# \n prints a newline
print("\nWelcome to PETCS Mad Libs!\n")
print('''Info --------------------->
Copy/paste a custom 1 paragraph story that follows the legend! 

Recommended story length is 100 - 500 words, but I won't stop you in testing the limits :) 

Legend for user input:
ADJ - Ask for an adjective
NOUN - Ask for a noun
VERBP - Ask for a plural verb
VERBS - Ask for a singular verb
VERBD - Ask for a past tense verb
ADVERB - Ask for a adverb
EMOJI - Ask for an emoji
* Legend is case sensitive!
''')

# Main game loop
while keepPlaying:
  # Prepares the story and gets user input
  story_temp = upload_story(story_temp, repeat)
  print()
  story = get_user_input(story_temp)
  
  # Prints the final story out
  print("\nHere is your Story!")
  # Alternative way of joining a list is using the .join method
  print(' '.join(story))
  print("\nTHE END\n")

  # Allows user to play again
  while True:
    playAgain = input("Play again? (y/n): ").lower()
    if playAgain == 'n':
      keepPlaying = False
      break
    elif playAgain == 'y':
      # Asks the user if they want to repeat last inputted story
      while True:
        repeatPrev = input("Repeat last entered story? (y/n): ").lower()
        if repeatPrev == 'y':
          repeat = True
          break
        elif repeatPrev == 'n':
          repeat = False
          break
        else:
          print("Invalid input, try again!")
      break
    else:
      print("Invalid input, try again!")

print("\nThanks for playing!")