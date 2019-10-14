#!/usr/bin/python3

import curses

user_name = "user"
available_commands = {
    "help": "Display generic help message. Use help [command] to display help text for that command.",
    "hello": "Echo the current user's name.",
    "changemyname": "Use changemyname [string] to change the current user's name.",
    "ls": "List files in the directory.",
    "read": "Use read [file] to display a file.",
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

def read_command(user_input_string):
    global user_name
    out_str = ""
    user_input_list = user_input_string.split()
    if user_input_list[0] == "help":
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
    elif user_input_list[0] == "hello":
        out_str += "Hello "
        out_str += user_name
        out_str += "\n"
    elif user_input_list[0] == "changemyname":
        if len(user_input_list) == 1:
            out_str += "Error: missing argument\n"
        else:
            user_name = user_input_list[1]
            out_str += "Name changed to "
            out_str += user_name
            out_str += "\n"
    elif user_input_list[0] == "ls":
        for i in files:
            out_str += i
            out_str += " "
        out_str += "\n"
    elif user_input_list[0] == "read":
        if len(user_input_list) == 1:
            out_str += "Error: missing argument\n"
        elif user_input_list[1] not in files:
            out_str += "Error: no file named "
            out_str += user_input_list[1]
            out_str += "\n"
        else:
            out_str += files[user_input_list[1]]
            out_str += "\n"
    else:
        out_str += "Error: did not recognise command "
        out_str += user_input_list[0]
        out_str += "\nTry typing help\n"
    return out_str

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
        stdscr.addstr( read_command(user_input) )

curses.wrapper(main)
