'''
This program is an example solution of what your mad libs game could look like! The code is simple implementation of the game. Are there any ways you can improve it? :)
'''

# Colour class for fancy text :)
# Syntax: bcolours.BLUE or GREEN + STRING + bcolours.END
class bcolours:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'

def runMadlibs():
  def get_user_input(story_temp, name):
    """
    This function stores the final story by replacing template with user input
    
    Parameters:
    story (list): The list that will be looped through
    name (str): The name of the character

    Returns:
    list: The final story with user input
    """
    story = story_temp[:]
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

  keepPlaying = True

  # Template story using a list
  story_temp = ["One ", "ADJ", " Wednesday afternoon, ", "NAME", " decides to attend an exciting PETCS meeting! ", "NAME", " happily walks into the ", "ADJ", " classroom choosing to ", "VERB", " by their favourite computer. The execs warmly greet all attending members and announce the lesson they are teaching: ", "LESSON", "! Everyone is puzzled, but they all agree to ", "VERB", " to the lesson. Halfway through the lesson, the principal runs", " into the room. He shouts at everyone to leave the premises, as there is a ", "ADJ", " ", "NOUN1", " happening at the school soon. ", "NAME", " being the smart student they are, chooses to ", "VERB", " out of the ", "NOUN2", " to escape a potential social situation. With the PETCS meeting coming to an abrupt end, ", "NAME", " decides to go home and ", "ADVERB", " work on their ", "ADJ", " homework."]

  # Welcome statement
  print("\nWelcome to PETCS Mad Libs!")

  # Main game loop
  while keepPlaying:
    # User can choose a name for the character
    name = bcolours.GREEN + input("\nPlease name your character: ") + bcolours.END
    print()
    story = get_user_input(story_temp, name)

    # \n outputs a newline
    print("\nHere is your Story!")

    # Prints the story
    for part in story:
      # end="" prevents a newline
      print(part, end="")
    print("\n\nTHE END\n")
    
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

if __name__ == "__main__":
  runMadlibs()