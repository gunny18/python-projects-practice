from curses import wrapper
import curses
import time


def start_screen(stdscr):
    # clears all text from screen
    stdscr.clear()

    # adds the text to screen at pos 0,0 by default
    stdscr.addstr("Welcome to the speed typing test!")
    stdscr.addstr("\nPress any key to begin")

    # refresh screen to apply the changes
    stdscr.refresh()

    # waiting for a key press event - blocking code!!
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)

    # first val is to move vertically, second horizontally on screen
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct = target[i]
        if char == correct:
            color = curses.color_pair(1)
        else:
            color = curses.color_pair(2)
        # can use the color pair numbers to apply a color combo/pair
        stdscr.addstr(0, i, char, color)


def wpm_screen(stdscr):
    target = "This is a simple wpm test!"
    current_text = []

    # to ensure, the key event is not blocking.
    # to make sure the wpm will decrease if we are not typing anything, instead of being static and waiting for a keypress
    stdscr.nodelay(True)

    start = time.time()
    while True:
        elapsed = max(time.time() - start, 1)
        wpm = round(len(current_text) / (elapsed / 60) / 5)
        stdscr.clear()
        display_text(stdscr, target, current_text, wpm)
        stdscr.refresh()

        # check to target and what we typed is matching, then exit
        if target == "".join(current_text):
            stdscr.nodelay(False)
            break

        # in the no delay mode of screen, waiting for keypress will give an error, hence needs to be wrapped in try except
        try:
            key = stdscr.getkey()
        except:
            continue

        # checks if the esc key is pressed. 27 is the ASCII code of esc key
        if ord(key) == 27:
            stdscr.nodelay(False)
            break

        # checking if backspace is pressed. We need to remove the char we typed if that happens, instead of default behavior of curses backspace event
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target):
            current_text.append(key)


# the wrapper passes a stdscr (screen) variable, which will be used to control the operations on the screen
def main(stdscr):

    # to customize the screen colors
    # 1st arg is a number to identify the color combo
    # second arg is the font color of text
    # third arg is for background color of text
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        wpm_screen(stdscr)
        stdscr.addstr(2, 0, "You completed the test!. Press any key to continue...")
        key = stdscr.getkey()

        if ord(key) == 27:
            break


# must be done to use curses lib
wrapper(main)
