import os
import time

from Tesst import play
from Aarav import reactor_puzzle
from Ayana import maze_game
from Suhani import escape_room


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_storyline():
    storyline = (
        "John is stranded on a spaceship. If he does not get out soon the "
        "spaceship may face engine failure. However, he needs to go through "
        "a sequence of games to reach the door of the control room. Can he "
        "escape? Play to find out!!!"
    )
    clear_screen()
    print("=" * 40)
    print("      THE PUZZLE ADVENTURE")
    print("=" * 40)
    print()
    for character in storyline:
        print(character, end="", flush=True)
        time.sleep(0.1)
    print("\n")
    input("Press Enter to help John escape...")


def main():
    show_storyline()
    clear_screen()
    wordle_win = play()

    clear_screen()
    reactor_win = reactor_puzzle(wordle_win)

    clear_screen()
    maze_win = maze_game(reactor_win)

    clear_screen()
    return escape_room(
        wordle_win,
        reactor_win,
        maze_win
    )


if __name__ == "__main__":
    main()
