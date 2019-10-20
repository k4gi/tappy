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
