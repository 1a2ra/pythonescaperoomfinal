import random
import os

GREEN = "\033[92m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
RESET = "\033[0m"

WORDS = [
    "python", "rocket", "planet", "garden", "bridge", "castle",
    "forest", "island", "jungle", "magnet", "pencil", "silver",
    "window", "dragon", "monkey", "orange", "purple", "yellow",
    "coffee", "doctor", "flower", "guitar", "hammer", "winter"
]

WORD_LENGTH = 6
MAX_ATTEMPTS = 6


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def check_guess(secret, guess):
    result = ["gray"] * WORD_LENGTH
    remaining = list(secret)

    for i in range(WORD_LENGTH):
        if guess[i] == secret[i]:
            result[i] = "green"
            remaining[i] = None

    for i in range(WORD_LENGTH):
        if result[i] == "green":
            continue

        if guess[i] in remaining:
            result[i] = "yellow"
            remaining[remaining.index(guess[i])] = None

    return result


def color_letter(letter, status):
    colors = {
        "green": GREEN,
        "yellow": YELLOW,
        "gray": GRAY
    }

    return f"{colors[status]}[{letter.upper()}]{RESET}"


def draw_board(history):
    print()
    print("╔════════════════════════════╗")
    print("║          WORDLE            ║")
    print("╚════════════════════════════╝")
    print()

    for guess, result in history:
        row = ""

        for ch, status in zip(guess, result):
            row += color_letter(ch, status) + " "

        print(row)

    for _ in range(MAX_ATTEMPTS - len(history)):
        print("[ ] [ ] [ ] [ ] [ ] [ ]")

    print()


def play():

        secret = random.choice(WORDS)
        history = []

        clear()
        print("=" * 32)
        print("WORDLE: ENGINE ACCESS CODE")
        print("=" * 32)
        print("Guess the hidden 6-letter word in 6 attempts.")
        print("After each guess, letters show how close you are:")
        print("[GREEN] correct letter and position")
        print("[YELLOW] correct letter, wrong position")
        print("[GRAY] letter is not in the word")
        print("A successful solve earns the code and a bonus hint.")
        print("If you run out of guesses, the code is revealed.")
        input("\nPress Enter to start Wordle...")

        while len(history) < MAX_ATTEMPTS:

                clear()
                draw_board(history)

                guess = input(
                    f"Guess #{len(history) + 1}/{MAX_ATTEMPTS}: "
                ).lower().strip()

                if len(guess) != WORD_LENGTH or not guess.isalpha():
                    print("\nWord must contain exactly 6 letters.")
                    input("Press Enter...")
                    continue

                result = check_guess(secret, guess)
                history.append((guess, result))

                if guess == secret:
                    clear()
                    draw_board(history)

                    print(f"{GREEN}")
                    print("🎉 YOU WIN!")
                    print(f"SECRET WORD: {secret.upper()}")
                    print()
                    print(f"{RESET}")
                    print("Code Chest 1:B@D!")

                    print (
                        "Bonus Hint: Number is not always number")


                    return True

        clear()
        draw_board(history)

        print(f"{GRAY}")
        print("💀 GAME OVER")
        print(f"The word was: {secret.upper()}")
        print(f"{RESET}")
        print("You failed the challenge.")
        print("Emergency Recovery Protocol.")
        print("CHEST CODE 1: B@D!")
        print("Penalty: No bonus hint for you!")
        return False






if __name__ == "__main__":
    play()
