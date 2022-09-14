from unicodedata import name
import characters
import locations
from commands import commands_list
import MainStory

game_name = "placeholder"  # Name of the game World !IMPORTANT placeholder

print(MainStory.prolog())  # print the prolog from MainStory.py
print(MainStory.player_name_question())  # print the player name question

print("\n" + "Na dann...", characters.MainCharacter.player_name(name),", Willkommen in", game_name)

while True:
    print("\n")
    command = input("Befehl: ").lower()  # in kleinbuchstaben umwandeln
    if command[0] in commands_list:
        commands_list[command[0]]()
    elif command[0] == "help" or "rest":
        pass
    else:
        print("Command not found")
