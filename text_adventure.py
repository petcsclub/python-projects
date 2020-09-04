from random import randint, choice
from time import sleep
from os import system
# from colorama import Fore, Back, Style

# You can change these constant lists depending on the story you create
yes_no = ["yes", "no"]
directions = ["left", "right"]
moves = ["fight", "run", "dodge", "inspect"]
classes = ["knight", "hunter"]

def make_decision(prompt, choices):
  """
  Returns any valid decision the user makes
  """
  while True:
    user_input = input(prompt).lower()
    if user_input in choices:
      return user_input
    else:
      print("Invalid choice, try again!")

def generate_player():
  """
  Returns randomly generated stats depending on the chosen class
  """
  player_class = make_decision("> Are you a knight or a hunter?: ", classes)
  sleep(1)
  if player_class == 'knight':
    print("> You are a knight! You are endowed with strength and courage, but you are extremely stubborn!")
    return {
      "hp": randint(100, 130),
      "atk": randint(5, 12),
      "spd": randint(10, 55)
    }
  else:
    print("> You are a Hunter! You are endowed with agility and stealth, but you lack vitality!")
    return {
      "hp": randint(70, 100),
      "atk": randint(7, 10),
      "spd": randint(35, 60)
    }
  
def generate_boss():
  """
  Returns a randomly generated boss with stats
  """
  boss_type = choice(["dragon", "orc"])
  if boss_type == "dragon":
    return {
      "type": "dragon",
      "hp": randint(100, 140),
      "atk": randint(5, 8),
      "spd": randint(50, 70)
    }
  else:
    return {
      "type": "orc",
      "hp": randint(90, 110),
      "atk": randint(7, 10),
      "spd": randint(20, 40)
    }
    return None

def print_stats(name):
  """
  Prints out the HP stat of the boss and player. Does not return anything.
  """
  print("\nHEALTH------------------------------")
  print(name.upper() + ":", player["hp"], "HP")
  print(boss["type"].upper() + ":", boss["hp"], "HP")
  print("------------------------------------\n")

def inspect(name):
  """
  Prints out the ATK and SPD stats of the boss and player. Does not return anything.
  """
  print("\nSTATS-------------------------------")
  print(name.upper()+":", player["atk"]+"ATK |", player["spd"]+"SPD")
  print(boss["type"].upper()+":", boss["atk"]+"ATK |", boss["spd"]+"SPD")
  print("------------------------------------\n")

def boss_fight(player, name, boss):
  """
  Executes the fight with the randomly generated boss. Returns True if the user beats the boss, False if they die, None if they run away.
  """
  while True:
    print_stats(name)
    move = make_decision("> Do you FIGHT, RUN, INSPECT or DODGE?: ", moves)
    if move == "fight":
      print("\n> You attack!")
      boss["hp"] -= randint(player["atk"]-4, player["atk"]+2)
    elif move == "dodge":
      sleep(1)
      if randint(0, player["spd"]) > randint(0, boss["spd"]):
        print("\n> You dodged! You regained health.")
        player["hp"] += randint(5, 10)
        continue
      else:
        print("\n> You failed to dodge!")
    elif move == "INSPECT":
      print("\n You inspected the", boss["type"] + "!")
      inspect(name)
    else:
      if player["spd"] > boss["spd"]:
        return None
      else:
        print("\n> You attempt to run, but you're too slow!")

    if boss["hp"] <= 0:
      return True
    
    sleep(1)
    print("\n>", boss["type"].upper(), "attacks!")
    sleep(1)
    if randint(0, 9) >= 1:
      player["hp"] -= randint(boss["atk"]-2, boss["atk"]+2)
    else:
      print("> But it misses!")

    if player["hp"] <= 0: 
      return False
  
# Main game loop
while True:
  name = input("\n> What is your name, adventurer?: ")
  player = generate_player()
  boss = generate_boss()

  while True:
    # Choice 1
    sleep(3)
    print("\n> You find yourself lost in a vast forest...")
    print("> Your head hurts...")
    print("> You look around to get a bearing of your surroundings. It seems you have 2 choices.")
    print("> Go LEFT past a nearby mysterious monument")
    print("> Go RIGHT past a little stream\n")
    
    sleep(1)
    # Tbh is kind of here for the aesthetic, cause ur choices don't matter haha
    decision = make_decision("> What do you choose, " + name + "?: ", directions)
    
    sleep(2)
    if randint(0, 1) == 1:
      print("\n> You choose to go", decision + ", but it seems you've gone even deeper into the forest.")
    else:
      print("\n> You choose to go", decision + ". As you make your way down the path, you are ambushed. You cannot make out who or what attacked you before everything goes black.")
      sleep(2)
      print("> You died!")
      break

    # Choice 2
    print("> You start to feel uneasy...")
    print("> Do you want to turn around?\n")
    
    sleep(1)
    decision = make_decision("> YES or NO, " + name +"?: ", yes_no)

    sleep(2)
    if decision == "no":
      print("\n> You choose to continue" + ", but you have gotten even more lost!")
    else:
      print("\n> You choose to go back" + ". While walking, you start to feel extremely nauseous...")
      print("> You fall over and pass out!")
      sleep(2)
      print("> You died!")
      break

    # Choice 3
    print("> Your heart starts pounding...")
    print("> You see a path that splits into two directions...\n")

    sleep(1)
    decision = make_decision("> LEFT or RIGHT, " + name +"?: ", directions)

    sleep(3)
    if randint(0, 1) == 1:
      print("\n> You choose to go", decision + "...")
    else:
      print("\n> You choose to go", decision + ". The forest become less dense as you walk down the path.")
      sleep(2)
      print("> After what seems like an hour, you finally make it out of the forest.")
      sleep(1)
      print("> You escaped unscathed!")
      break
    
    sleep(1)
    print("> All of a sudden, the ground shakes!")
    print("> A huge", boss["type"], "emerges from the trees!")

    win = boss_fight(player, name, boss)

    if win == None:
      print("\n> You cowardly run away from the", boss["type"] + "!")
      sleep(2)
      print("> After what seems like an hour of running, you finally make it out of the forest.")
      break
    elif win:
      print("\n> You defeated the", boss["type"] + "! You claim the loot of your fallen foe and make your way out of the forest!")
      break
    else:
      print("\n> The injuries you sustained from fighting make you collapse... You died!")
      break
  
  playAgain = make_decision("\nPlay again (YES/NO)?: ", yes_no)
  if playAgain == "no":
    break
  sleep(1)
  system('clear')


print("\nThanks for playing!")