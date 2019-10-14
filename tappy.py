#!/bin/python3

import curses

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


def main(stdscr):
    #stdscr.addstr("gday" + str(curses.COLS) + "  " + str(curses.LINES) )
    #stdscr.getch() #wait

    #stdscr.move(5,0)
    #curses.echo()
    #user_input = stdscr.getstr()
    #curses.noecho()

    #stdscr.move(10,0)
    #stdscr.addstr(user_input)
    #stdscr.getch() #wait

    stdscr.scrollok(True)
    user_prompt = "> "

    #input loop
    user_input = ""
    while user_input != "exit":
        stdscr.addstr(user_prompt)
        user_input = get_string(stdscr)

        stdscr.addstr("I heard " + str(user_input) + "\n" )


curses.wrapper(main)
