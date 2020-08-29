# Colour class for fancy text :)
# Syntax: bcolours.OKBLUE or OKGREEN + STRING + bcolours.ENDC
class bcolours:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

print("\nWelcome to PETCS Mad Libs!")

keepPlaying = True

# Template story
story_temp = ["One ", "ADJ", " Wednesday afternoon, ", "NAME", " decides to attend an exciting PETCS meeting! ", "NAME", " happily walks into the ", "ADJ", " classroom choosing to ", "VERB", " by their favourite computer. The execs warmly greet all attending members and announce the lesson they are teaching: ", "LESSON", "! Everyone is puzzled, but agree to ", "VERB", " to the lesson. Halfway through the lesson, the principal ", "VERB", " into the room. He shouts at everyone to leave the premises, as there is a ", "ADJ", "NOUN1", " happening at the school soon ", "NAME", " being the smart student they are, chooses to ", "VERB", " out of the ", "NOUN2", " to escape the potential harm. With the PETCS meeting coming to an abrupt end, ", "NAME", " decides to go home and", "ADVERB", " work on their ", "ADJ", " homework."]
copy = story_temp[:]

# This function stores user input
def get_user_input(story, name):
  # Checks if a part of the story needs input
  for i in range(len(story)):
    if story[i] == "ADJ":
      story[i] = bcolours.OKBLUE + input("Enter an adjective: ") + bcolours.ENDC
    elif story[i] == "NAME":
      story[i] = name
    elif story[i] == "VERB":
      story[i] = bcolours.OKBLUE + input("Enter a verb (plural): ") + bcolours.ENDC
    elif story[i] == "LESSON":
      story[i] = bcolours.OKBLUE + input("What did you wish school taught you?: ") + bcolours.ENDC
    elif story[i] == "NOUN1":
      story[i] = bcolours.OKBLUE + input("What event would a school host?: ") + bcolours.ENDC
    elif story[i] == "NOUN2":
      story[i] = bcolours.OKBLUE + input("Enter your favourite location of your school: ") + bcolours.ENDC
    elif story[i] == "ADVERB":
      story[i] = bcolours.OKBLUE + input("Enter an adverb: ") + bcolours.ENDC
  return story

# This function outputs the user's story
def output_user_story(story):
  # \n outputs a newline
  print("\nHere is your Story!")
  for part in story:
    # end="" prevents a newline
    print(part, end="")
  print("\n\nTHE END\n")

# Allows user to play again
while keepPlaying == True:
  name = bcolours.OKGREEN + input("\nPlease name your character: ") + bcolours.ENDC
  print()
  story = get_user_input(story_temp, name)
  output_user_story(story)
  # Resets the template story
  story_temp = copy[:]
  while True:
    quitGame = input("Play again? (y/n): ")
    if quitGame == 'n':
      keepPlaying = False
      break
    elif quitGame == 'y':
      break
    else:
      print("Invalid input, try again!")

print("\nThanks for playing!")