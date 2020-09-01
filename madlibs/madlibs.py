# Colour class for fancy text :)
# Syntax: bcolours.BLUE or GREEN + STRING + bcolours.END
class bcolours:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'

print("\nWelcome to PETCS Mad Libs!")

keepPlaying = True

# This function stores user input
def get_user_input(story, name):
  # Checks if a part of the story needs input
  # Not pretty, but simple to understand with if loops
  for i in range(len(story)):
    if story[i] == "ADJ":
      story[i] = bcolours.BLUE + input("Enter an adjective: ") + bcolours.END
    elif story[i] == "NAME":
      story[i] = name
    elif story[i] == "VERB":
      story[i] = bcolours.BLUE + input("Enter a verb (plural): ") + bcolours.END
    elif story[i] == "LESSON":
      story[i] = bcolours.BLUE + input("What did you wish school taught you?: ") + bcolours.END
    elif story[i] == "NOUN1":
      story[i] = bcolours.BLUE + input("What event would a school host?: ") + bcolours.END
    elif story[i] == "NOUN2":
      story[i] = bcolours.BLUE + input("Enter your favourite location of your school: ") + bcolours.END
    elif story[i] == "ADVERB":
      story[i] = bcolours.BLUE + input("Enter an adverb: ") + bcolours.END
  return story

# This function outputs the user's story
def output_user_story(story):
  # \n outputs a newline
  print("\nHere is your Story!")
  for part in story:
    # end="" prevents a newline
    print(part, end="")
  print("\n\nTHE END\n")

# Template story -> ngl easiest way to implement madlibs
story_temp = ["One ", "ADJ", " Wednesday afternoon, ", "NAME", " decides to attend an exciting PETCS meeting! ", "NAME", " happily walks into the ", "ADJ", " classroom choosing to ", "VERB", " by their favourite computer. The execs warmly greet all attending members and announce the lesson they are teaching: ", "LESSON", "! Everyone is puzzled, but agree to ", "VERB", " to the lesson. Halfway through the lesson, the principal ", "VERB", " into the room. He shouts at everyone to leave the premises, as there is a ", "ADJ", "NOUN1", " happening at the school soon ", "NAME", " being the smart student they are, chooses to ", "VERB", " out of the ", "NOUN2", " to escape the potential harm. With the PETCS meeting coming to an abrupt end, ", "NAME", " decides to go home and ", "ADVERB", " work on their ", "ADJ", " homework."]
copy = story_temp[:]

# Main game loop
while keepPlaying == True:
  name = bcolours.GREEN + input("\nPlease name your character: ") + bcolours.END
  print()
  story = get_user_input(story_temp, name)
  output_user_story(story)
  # Resets the template story
  story_temp = copy[:]
  # Allows user to play again
  while True:
    playAgain = input("Play again? (y/n): ").lower()
    if playAgain == 'n':
      keepPlaying = False
      break
    elif playAgain == 'y':
      break
    else:
      print("Invalid input, try again!")

print("\nThanks for playing!")