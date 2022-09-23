from commands import commands_list
import mainStory

mainStory.prolog()  # Start the game with the prolog
mainStory.player_name_question()  # ask for the player's name
mainStory.start_main_storyline()  # print the start of the main storyline

while True:
    print("\n")
    command = input("Befehl: ").lower()  # in kleinbuchstaben umwandeln
    if command[0] in commands_list:
        commands_list[command[0]]()
    elif command[0] == "help" or "rest":
        pass
    else:
        print("Command not found")
