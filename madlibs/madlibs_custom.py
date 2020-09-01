# Colour class for fancy text :)
# Syntax: bcolours.BLUE or GREEN + STRING + bcolours.END
class bcolours:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'

print("\nWelcome to PETCS Mad Libs!")
print(''' Info ---------------------
Copy/paste a custom story that follows the legend!
If you want to input a .txt file, make sure the .txt file is in the same directory (folder) as the python script!  

Legend for user input:
ADJ - Ask for an adjective
NOUN - Ask for a noun
NAME - Input a name for a character
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

def upload_story():
  while True:
    story = ""
    choice = input("\nUpload .txt file or manually (txt/man): ").lower()
    if repeat:
      return copy[:]
    else:
      # This code assumes you put in the right .txt name.
      # However, if you put the wrong name, it will throw
      # an error. How can you work around that? 
      # Hint: Try Except
      if choice == "txt":
        # Although we didn't teach open(), it is a built-in function for opening files :)
        open_story = open(input("Enter file name: "), "r")
        story = open_story.read()
        break
      elif choice == "man":
        story = input("Type your story here: ")
        break
      else:
        print("Invalid choice, try again!")
  # Split is a method that 'splits' a string into a list
  # By default, it seperates by whitespace characters
  return story.split()

def repeat_story():
  while True:
      repeatPrev = input("Repeat last entered story? (y/n): ").lower()
      if repeatPrev == 'y':
        return True
      elif repeatPrev == 'n':
        return False

# This function stores user input
def get_user_input(story):
  # Checks if a part of the story needs input
  for i in range(len(story)):
    if story[i] == "ADJ":
      story[i] = bcolours.BLUE + input("Enter an adjective: ") + bcolours.END
    elif story[i] == "NAME":
      story[i] = story[i] = bcolours.GREEN + input("Enter a name: ") +  bcolours.END
    elif story[i] == "NOUN":
      story[i] = bcolours.BLUE + input("Enter a noun: ") + bcolours.END
    elif story[i] == "VERBP":
      story[i] = bcolours.BLUE + input("Enter a verb (plural): ") + bcolours.END
    elif story[i] == "VERBS":
      story[i] = bcolours.BLUE + input("Enter a verb (singular): ") + bcolours.END
    elif story[i] == "VERBD":
      story[i] = bcolours.BLUE + input("Enter a verb (past tense): ") + bcolours.END
    elif story[i] == "ADVERB":
      story[i] = bcolours.BLUE + input("Enter an adverb: ") + bcolours.END
  return story

# This function outputs the user's story
def output_user_story(story):
  # \n outputs a newline
  print("\nHere is your Story!")
  # Alternative way of joining a list is using the .join
  # method, where in this case, a space between the 
  # quotes represents joining each word by a whitespace
  print(' '.join(story))
  print("\n\nTHE END\n")

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