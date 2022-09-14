def game_help():
    print("verfügbare Befehle: ")
    for help_commands in commands_list.keys():
        print(help_commands)

def game_quit():
    print("Auf Wiedersehen")
    quit()

def yes():
    print("yes")

def no():
    print("no")

commands_list = {
    'help': game_help,
    'quit': game_quit
}
