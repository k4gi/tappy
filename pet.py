#!/usr/bin/python3

import curses
import random

user_name = "user"
available_commands = {
    "help": "Display generic help message. Use help [command] to display help text for that command.",
    "hello": "Echo the current user's name.",
    "changemyname": "Use changemyname [string] to change the current user's name.",
    "ls": "List files in the directory.",
    "read": "Use read [file] to display a file.",
    "random": "Guess a number game. Type 'exit' to stop playing.",
    "exit": "Turn off the computer."
}
files = {
    "readme.txt": "hey comrade is your computer working ok? shoot me an email when you read this, i like to know when my builds are a success -fade",
    "dontreadme.txt": "i told u dog"
}


def get_string(window):
    out_str = ""
    curses.nocbreak()
    curses.echo()
    curses.curs_set(1)
    user_input = ""
    while user_input != "\n":
        out_str += user_input
        user_input = window.getkey()
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    return out_str

def p_help(window, user_input_list):
    out_str = ""
    if len(user_input_list) == 1:
        out_str += "Listing available commands:\n"
        for i in available_commands:
            out_str += i
            out_str += " "
        out_str += "\nUse help [command] to display help text for that command.\n"
    elif user_input_list[1] not in available_commands:
        out_str += "Error: no command named "
        out_str += user_input_list[1]
        out_str += "\n"
    else:
        out_str += available_commands[user_input_list[1]]
        out_str += "\n"
    window.addstr(out_str)

def p_hello(window, user_input_list):
    out_str = ""
    out_str += "Hello "
    out_str += user_name
    out_str += "\n"
    window.addstr(out_str)

def p_changemyname(window, user_input_list):
    global user_name
    out_str = ""
    if len(user_input_list) == 1:
        out_str += "Error: missing argument\n"
    else:
        user_name = user_input_list[1]
        out_str += "Name changed to "
        out_str += user_name
        out_str += "\n"
    window.addstr(out_str)

def p_ls(window, user_input_list):
    out_str = ""
    for i in files:
        out_str += i
        out_str += " "
    out_str += "\n"
    window.addstr(out_str)

def p_read(window, user_input_list):
    out_str = ""
    if len(user_input_list) == 1:
        out_str += "Error: missing argument\n"
    elif user_input_list[1] not in files:
        out_str += "Error: no file named "
        out_str += user_input_list[1]
        out_str += "\n"
    else:
        out_str += files[user_input_list[1]]
        out_str += "\n"
    window.addstr(out_str)

def p_random(window, user_input_list):
    window.addstr("Guess a random number from 0 to 99!\n")
    user_prompt = "?> "
    hidden_number = random.randint(0, 99)
    tries = 0
    #input loop
    user_input = ""
    while user_input != "exit":
        window.addstr(user_prompt)
        user_input = get_string(window)

        user_input_list2 = user_input.split()
        if user_input_list2:
            try:
                user_guess = int( user_input_list2[0] )
            except:
                window.addstr("Error: " + user_input_list2[0] + " not a number\n")
            else:
                tries += 1
                if user_guess > hidden_number:
                    window.addstr("Go lower!\n")
                elif user_guess < hidden_number:
                    window.addstr("Go higher!\n")
                else:
                    window.addstr("Correct! You got it in " + str(tries) + " tries!\n")
                    user_input = "exit"

def p_explore(window, user_input_list):
    window.addstr("You're lost on an island. Can you find your way back home?\n-----\n")
    window.addstr("You wake up. You try to breathe, and damp sand gets sucked into your nostrils. When you're done sputtering, you notice the gentle, rhythmic sound of waves and the sunlight warm on your skin. Gradually, you stand up. You're on a long, white beach. Behind you the ocean water stretches to the horizon. Before you lies a wild jungle. Welcome to The Island.\n")
    user_prompt = ">> "
    #input loop
    user_input = ""
    while user_input != "exit":
        window.addstr(user_prompt)
        user_input = get_string(window)
        user_input_list2 = user_input.split()
        if user_input_list2:
            window.addstr(user_input_list2[0] + "\n")

def p_town(window, user_invoke_list):
    window.addstr("It's town management time, binch.\n")
    user_prompt = ">> "

    #declare town stats
    town_day = 1
    town_pop = 5
    town_pop_starving = 0
    town_pop_dead = 0
    town_graveyard = 0
    town_food = 20
    town_wood = 20
    town_houses = 1
    town_house_progess = 0
    town_art = 0
    town_art_progress = 0
    #jobs
    job_forager = 0
    job_cutter = 0
    job_builder = 0
    job_artisan = 0

    #game loop
    user_input = ""
    while user_input != "exit":
        #status update
        window.addstr("The sun rises on day " + town_day + " of The Town.\n")
        while town_food < town_pop: #feed the well fed
            town_pop -= 1
            town_pop_starving += 1
        town_food -= town_pop
        while town_food < town_pop_starving: #feed the starving
            town_pop_starving -= 1
            town_pop_dead += 1
        town_food -= town_pop_starving
        while town_food > 0 && town_pop_starving > 0: # satiate the starving
            town_food -= 1
            town_pop_starving -= 1
            town_pop += 1
        if town_houses > (town_pop + town_pop_starving)/5: #check for sprout
            if random.randint(0,4) == 0:
                town_pop += 1
                window.addstr("A new townsperson has sprouted!\n")
        window.addstr(town_pop + " people are well fed.\n" + town_pop_starving + " people are starving.\n" + town_pop_dead + " people have died.\n")
        if town_house_progress > 0: #check for building progress
            if town_house_progress > job_builder:
                town_house_progress -= job_builder
            else:
                town_house_progress = 0
                town_houses += 1
                window.addstr("A new house has finished construction!\n")
        # general status update
        window.addstr("The Town has " town_houses + " houses.\n")
        window.addstr("The stockpiles hold " + town_food + " food,\n")
        window.addstr("                and " + town_wood + " wood.\n")
        window.addstr("What will the next day bring?\n\n")

        while user_input != "exit" && user_input != "continue":
            window.addstr("Listing options . . .\n1: idk\n")
            window.addstr(user_prompt)
            user_input = get_string(window)
            user_input_list = user_input.split()
            if user_input_list[0] == 1:
                # some code here i guess
            elif user_input_list[0] == "exit":
                user_input = "exit"
            else:
                user_input = "continue"

def read_command(window, user_input_string):
    user_input_list = user_input_string.split()
    if user_input_list:
        if user_input_list[0] == "help":
            p_help(window, user_input_list)
        elif user_input_list[0] == "hello":
            p_hello(window, user_input_list)
        elif user_input_list[0] == "changemyname":
            p_changemyname(window, user_input_list)
        elif user_input_list[0] == "ls":
            p_ls(window, user_input_list)
        elif user_input_list[0] == "read":
            p_read(window, user_input_list)
        elif user_input_list[0] == "random":
            p_random(window, user_input_list)
        elif user_input_list[0] == "explore":
            p_explore(window, user_input_list)
        elif user_input_list[0] == "town":
            p_town(window, user_input_list)
        else:
            out_str = ""
            out_str += "Error: did not recognise command "
            out_str += user_input_list[0]
            out_str += "\nTry typing help\n"
            window.addstr(out_str)

def main(stdscr):
    curses.curs_set(0)
    stdscr.scrollok(True)
    user_prompt = "> "
    #input loop
    user_input = ""
    while user_input != "exit":
        stdscr.addstr(user_prompt)
        user_input = get_string(stdscr)

        #stdscr.addstr("I heard " + str(user_input) + "\n" )
        read_command(stdscr, user_input)

curses.wrapper(main)
