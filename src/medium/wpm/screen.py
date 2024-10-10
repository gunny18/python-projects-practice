from curses import wrapper
import curses
import time


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the speed typing test!")
    stdscr.addstr("\nPress any key to begin")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct = target[i]
        if char == correct:
            color = curses.color_pair(1)
        else:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)


def wpm_screen(stdscr):
    target = "This is a simple wpm test!"
    current_text = []
    stdscr.nodelay(True)

    start = time.time()
    while True:
        elapsed = max(time.time() - start, 1)
        wpm = round(len(current_text) / (elapsed / 60) / 5)
        stdscr.clear()
        display_text(stdscr, target, current_text, wpm)
        stdscr.refresh()

        if target == "".join(current_text):
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            stdscr.nodelay(False)
            break

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target):
            current_text.append(key)


def main(stdscr):
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


wrapper(main)
