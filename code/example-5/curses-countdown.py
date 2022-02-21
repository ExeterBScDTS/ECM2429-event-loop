"""
    See https://theailearner.com/2019/03/10/snake-game-using-python-curses/
"""
import curses
from datetime import timedelta, datetime

def show_count(win, deadline: datetime):
    remaining = deadline - datetime.now()
    if remaining < timedelta(0):
        remaining = "     Launch     "
        deadline = None
    win.addstr(9, 7, f"{remaining}")
    return deadline


def start_countdown(seconds):
    return datetime.now() + timedelta(seconds=seconds)


def setup(stdsrc):
    stdsrc.clear()
    sc = curses.initscr()
    h, w = sc.getmaxyx()
    win = curses.newwin(h, w, 0, 0)
    curses.curs_set(0)
    win.border(0)

    win.addstr(3, 5, "s - start countdown")
    win.addstr(5, 5, "r - reset")
    win.addstr(7, 5, "c - cancel")
    win.addstr(7, 25, "x - exit")
    return win


def mainloop(stdscr):
    win = setup(stdscr)

    countdown_seconds = 10
    deadline = None
    
    while True:

        win.timeout(10)
        key = win.getch()
 
        if deadline:
            deadline = show_count(win, deadline)

        if key == -1:
            continue

        if key == ord('s'):
            # Start the countdown if it isn't already running
            if not deadline:
                deadline = start_countdown(countdown_seconds)
            else:
                curses.beep()
        elif key == ord('r'):
            # Restart the countdown if it is already running
            if deadline:
                deadline = start_countdown(countdown_seconds)
            else:
                curses.beep()
        elif key == ord('c'):
            # Cancel the countdown
            if deadline:
                deadline = None
            else:
                curses.beep()
        elif key == ord('x'):
            # Exit.  Only available if the countdown has completed.
            if not deadline:
                break
            curses.beep()
        else:
            curses.beep()


curses.wrapper(mainloop)
print("Goodbye")
