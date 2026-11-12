import os
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"
RESET = "\033[0m"
MAGENTA = "\033[95m"
GRAY = "\033[90m"
BOLD = "\033[1m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def banner(title, color=CYAN):
    print(f"{color}{BOLD}╔{'═' * 30}╗{RESET}")
    print(f"{color}{BOLD}║{title.center(30)}║{RESET}")
    print(f"{color}{BOLD}╚{'═' * 30}╝{RESET}")


notes = []


def show_notes():
    print(f"\n{MAGENTA}{BOLD}📓 CLUE NOTEBOOK{RESET}")
    if not notes:
        print(f"{GRAY}Nothing yet. Open a chest to find clues!{RESET}")
    for line in notes:
        print(f"{YELLOW}- {line}{RESET}")
    input(f"{CYAN}Press Enter to go back...{RESET}")


def ask(prompt=""):
    while True:
        answer = input(prompt)
        if answer.strip().lower() in ("n", "notes", "notebook"):
            show_notes()
            continue
        return answer


def win_screen(code, hint=None, extra=None):
    print(f"\n{GREEN}{BOLD}🎉 PUZZLE SOLVED!{RESET}")
    if extra:
        print(f"{CYAN}{extra}{RESET}")
    print(f"{YELLOW}{BOLD}🔑 Chest code: {code}{RESET}")
    if hint:
        print(f"{MAGENTA}💡 Hint: {hint}{RESET}")


def lose_screen(reason, code):
    print(f"\n{RED}{BOLD}💀 PUZZLE FAILED!{RESET}")
    print(f"{GRAY}{reason}{RESET}")
    print(f"{YELLOW}{BOLD}🔑 Chest code: {code}{RESET}")
    print(f"{GRAY}No bonus hint for you this time!{RESET}")

def wordle_game():
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
        banner("WORDLE", CYAN)
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

                        win_screen("B@D!", "Num is alpha, alpha is num", extra=f"The secret word was {secret.upper()}")

                        return True

            clear()
            draw_board(history)

            lose_screen(f"The word was {secret.upper()}.", "B@D!")
            return False






    return play()


def maze_game():
    import random
    import builtins
    _print = builtins.print
    pending = []
    capturing = [False]

    def print(*a, **k):
        if capturing[0]:
            pending.append((a, k))
        else:
            _print(*a, **k)

    def flush_pending():
        capturing[0] = False
        for a, k in pending:
            _print(*a, **k)
        pending.clear()

    mazes = [
        [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "P", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", "#", "#", ".", ".", "#", ".", "#", "#", ".", ".", "#"],
            ["#", ".", ".", ".", ".", "E", ".", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", ".", "#", "#", "#", "#", ".", "#", ".", ".", "#"],
            ["#", ".", ".", ".", "#", ".", ".", ".", ".", "#", ".", ".", "#"],
            ["#", ".", "#", ".", "#", ".", "#", "#", ".", "#", ".", ".", "#"],
            ["#", ".", "#", ".", ".", ".", ".", "#", ".", ".", ".", ".", "#"],
            ["#", ".", "#", "#", "#", "#", ".", "#", "#", "#", ".", ".", "#"],
            ["#", "K", ".", ".", ".", ".", ".", ".", "#", ".", ".", "X", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        ],
        [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "P", ".", ".", "#", ".", ".", ".", "#", ".", ".", ".", "#"],
            ["#", "#", ".", "#", ".", "#", ".", "#", ".", "#", ".", "#", "#"],
            ["#", ".", ".", ".", ".", ".", "E", ".", ".", ".", ".", ".", "#"],
            ["#", ".", "#", "#", "#", ".", "#", ".", "#", "#", "#", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", ".", "#", "#", "#", "#", ".", "#", "#", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", "#", "#", ".", "#", "#", ".", "#", "#", ".", ".", "#"],
            ["#", "K", ".", ".", ".", ".", ".", ".", ".", ".", ".", "X", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        ],
        [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "P", ".", "#", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
            ["#", ".", ".", "#", ".", "#", "#", "#", ".", "#", ".", ".", "#"],
            ["#", "#", ".", ".", ".", "E", ".", ".", ".", ".", ".", "X", "#"],
            ["#", ".", ".", "#", "#", ".", "#", "#", "#", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", ".", "#", "#", ".", "#", "#", ".", "#", "#", ".", "#", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", ".", "#", "#", "#", "#", ".", "#", "#", ".", "#"],
            ["#", "K", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        ]
    ]

    maze = random.choice(mazes)

    player_row = 0
    player_col = 0
    enemy_row = 0
    enemy_col = 0
    key_row = 0
    key_col = 0
    exit_row = 0
    exit_col = 0

    r = 0
    while r < len(maze):
        c = 0
        while c < len(maze[r]):
            if maze[r][c] == "P":
                player_row = r
                player_col = c
                maze[r][c] = "."
            elif maze[r][c] == "E":
                enemy_row = r
                enemy_col = c
                maze[r][c] = "."
            elif maze[r][c] == "K":
                key_row = r
                key_col = c
            elif maze[r][c] == "X":
                exit_row = r
                exit_col = c
            c += 1
        r += 1

    has_key = False
    game_over = False
    won = False

    while game_over == False:
        clear_screen()
        capturing[0] = False
        banner("LABYRINTH QUEST", MAGENTA)

        r = 0
        while r < len(maze):
            line = ""
            c = 0
            while c < len(maze[r]):
                if r == player_row and c == player_col:
                    line += f"{GREEN}{BOLD}P{RESET} "
                elif r == enemy_row and c == enemy_col:
                    line += f"{RED}{BOLD}E{RESET} "
                elif r == key_row and c == key_col and not has_key:
                    line += f"{YELLOW}{BOLD}K{RESET} "
                elif r == exit_row and c == exit_col:
                    line += f"{CYAN}{BOLD}X{RESET} "
                else:
                    if maze[r][c] == "#":
                        line += f"{BLUE}█{RESET} "
                    else:
                        line += f"{GRAY}·{RESET} "
                c += 1
            print(line)
            r += 1

        print("-" * 27)
        if has_key == True:
            print(f"{GREEN}Status: Key Collected! Head to the exit!{RESET}")
        else:
            print(f"{YELLOW}Status: Key Needed! Find the K.{RESET}")
        flush_pending()

        move = input("Your move (W/A/S/D, Q): ").strip().upper()
        capturing[0] = True

        if move == "Q":
            print("You quit the game. Goodbye!")
            break

        new_row = player_row
        new_col = player_col

        if move == "W":
            new_row = player_row - 1
        elif move == "S":
            new_row = player_row + 1
        elif move == "A":
            new_col = player_col - 1
        elif move == "D":
            new_col = player_col + 1
        else:
            print("Invalid input! Please press W, A, S, D, or Q.")
            continue

        if maze[new_row][new_col] == "#":
            print("Ouch! You hit a wall!")
            continue

        if new_row == enemy_row and new_col == enemy_col:
            print("Oh no! The enemy caught you!")
            game_over = True
            continue

        player_row = new_row
        player_col = new_col

        if player_row == key_row and player_col == key_col:
            if has_key == False:
                has_key = True
                print("You picked up the key!")

        if player_row == exit_row and player_col == exit_col:
            if has_key == True:
                print("You escaped the labyrinth! YOU WIN!")
                won = True
                game_over = True
                continue
            else:
                print("The door is locked! You need the key first!")

        row_diff = abs(enemy_row - player_row)
        col_diff = abs(enemy_col - player_col)

        if row_diff > col_diff:
            if enemy_row < player_row:
                if maze[enemy_row + 1][enemy_col] != "#":
                    enemy_row = enemy_row + 1
                elif enemy_col < player_col and maze[enemy_row][enemy_col + 1] != "#":
                    enemy_col = enemy_col + 1
                elif enemy_col > player_col and maze[enemy_row][enemy_col - 1] != "#":
                    enemy_col = enemy_col - 1
            else:
                if maze[enemy_row - 1][enemy_col] != "#":
                    enemy_row = enemy_row - 1
                elif enemy_col < player_col and maze[enemy_row][enemy_col + 1] != "#":
                    enemy_col = enemy_col + 1
                elif enemy_col > player_col and maze[enemy_row][enemy_col - 1] != "#":
                    enemy_col = enemy_col - 1
        else:
            if enemy_col < player_col:
                if maze[enemy_row][enemy_col + 1] != "#":
                    enemy_col = enemy_col + 1
                elif enemy_row < player_row and maze[enemy_row + 1][enemy_col] != "#":
                    enemy_row = enemy_row + 1
                elif enemy_row > player_row and maze[enemy_row - 1][enemy_col] != "#":
                    enemy_row = enemy_row - 1
            else:
                if maze[enemy_row][enemy_col - 1] != "#":
                    enemy_col = enemy_col - 1
                elif enemy_row < player_row and maze[enemy_row + 1][enemy_col] != "#":
                    enemy_row = enemy_row + 1
                elif enemy_row > player_row and maze[enemy_row - 1][enemy_col] != "#":
                    enemy_row = enemy_row - 1

        if enemy_row == player_row and enemy_col == player_col:
            print("Oh no! The enemy caught you!")
            game_over = True


    flush_pending()
    if won == True:
        win_screen("A0RU", "The letter stays, only the number changes")
        return True
    if game_over == True:
        lose_screen("The enemy caught you!", "A0RU")
    return False


def reactor_puzzle():
    import builtins
    _print = builtins.print
    pending = []
    capturing = [False]

    def print(*a, **k):
        if capturing[0]:
            pending.append((a, k))
        else:
            _print(*a, **k)

    def flush_pending():
        capturing[0] = False
        for a, k in pending:
            _print(*a, **k)
        pending.clear()
    reactor = [
        [{"energy":4,"type":"T"},{"energy":7,"type":"E"},{"energy":3,"type":"T"},{"energy":5,"type":"E"},{"energy":4,"type":"T"}],
        [{"energy":6,"type":"E"},{"energy":5,"type":"T"},{"energy":8,"type":"E"},{"energy":2,"type":"T"},{"energy":1,"type":"E"}],
        [{"energy":2,"type":"T"},{"energy":4,"type":"E"},{"energy":7,"type":"T"},{"energy":3,"type":"E"},{"energy":5,"type":"T"}],
        [{"energy":8,"type":"E"},{"energy":1,"type":"T"},{"energy":6,"type":"E"},{"energy":4,"type":"T"},{"energy":7,"type":"E"}],
        [{"energy":3,"type":"T"},{"energy":5,"type":"E"},{"energy":2,"type":"T"},{"energy":8,"type":"E"},{"energy":4,"type":"T"}]
    ]

    row_letters = ["A", "B", "C", "D", "E"]
    cipher = "Alphabet"
    count = 0

    def print_grid():
        banner("REACTOR CORE", RED)
        print(f"{GREEN}stable{RESET} {RED}unstable{RESET}   T = thermal  E = electric")
        print(f"{CYAN}{BOLD}     1    2    3    4    5{RESET}")
        for row in range(5):
            print(f"{CYAN}{BOLD}{row_letters[row]}{RESET}", end="   ")
            for col in range(5):
                node = reactor[row][col]
                color = GREEN if 1 <= node["energy"] <= 5 else RED
                print(f"{color}{node['type']}{node['energy']}{RESET}", end="   ")
            print()

    def thermal_overload(row, col):
        reactor[row][col]["energy"] = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < 5 and 0 <= new_col < 5:
                reactor[new_row][new_col]["energy"] += 1

        print(
            f"\033[91mTHERMAL OVERLOAD "
            f"at {row_letters[row]}{col+1}\033[0m"
        )

    def electric_overload(row, col):
        reactor[row][col]["energy"] = 0

        directions = [
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < 5 and 0 <= new_col < 5:
                reactor[new_row][new_col]["energy"] += 1

        print(
            f"\033[94mELECTRIC OVERLOAD "
            f"at {row_letters[row]}{col+1}\033[0m"
        )

    def reactor_stable():
        for row in reactor:
            for node in row:
                if node["energy"] < 1 or node["energy"] > 5:
                    return False

        return True

    def find_overload():
        overload = []

        for row in range(5):
            for col in range(5):
                if reactor[row][col]["energy"] >= 10:
                    overload.append((row, col))

        return overload

    def resolve_reactor():
        overload = find_overload()
        safety_breakout = 0

        while overload and safety_breakout < 100:
            row, col = overload.pop(0)
            node_type = reactor[row][col]["type"]

            if node_type == "T":
                thermal_overload(row, col)
            else:
                electric_overload(row, col)

            overload = find_overload()
            safety_breakout += 1

    def hint_system():
        stable_nodes = 0

        for row in reactor:
            for node in row:
                if 1 <= node["energy"] <= 5:
                    stable_nodes += 1

        unstable_count = 25 - stable_nodes

        if unstable_count == 0:
            print("\nEngineering Note:")
            print("All reactor systems stable.")
            return

        if unstable_count > 15:
            print(
                "\nEngineering Note:\n"
                "Many systems remain unstable.\n"
                "Focus on reducing extremely high\n"
                "or extremely low energy values first."
            )
            return

        if unstable_count > 5:
            print(
                "\nEngineering Note:\n"
                "Remember:\n"
                "Thermal nodes affect vertical and horizontal neighbours.\n"
                "Electric nodes affect diagonal neighbours."
            )
            return

        for row in range(5):
            for col in range(5):
                energy = reactor[row][col]["energy"]

                if energy < 1 or energy > 5:
                    print(
                        f"\nEngineering Note:\n"
                        f"Node {row_letters[row]}{col+1} "
                        f"remains unstable.\n"
                        f"Current Energy = {energy}"
                    )
                    return

    while True:
        clear_screen()
        capturing[0] = False
        print_grid()
        flush_pending()

        node_charge = (
            input("\nEnter node (A1-E5, HINT, QUIT): ")
            .strip()
            .replace(" ", "")
            .upper()
        )
        capturing[0] = True

        if node_charge == "QUIT":
            flush_pending()
            print("\nMission Aborted.")
            break

        if node_charge == "HINT":
            hint_system()
            continue

        if len(node_charge) != 2:
            print("Invalid input. Use A1-E5.")
            continue

        letter = node_charge[0]
        number = node_charge[1]

        if (
            letter not in row_letters
            or not number.isdigit()
            or not (1 <= int(number) <= 5)
        ):
            print("Invalid input. Use A1-E5.")
            continue

        target_row = row_letters.index(letter)
        target_col = int(number) - 1

        reactor[target_row][target_col]["energy"] += 1

        print(f"\n{CYAN}Node {letter}{number} charged.{RESET}")

        resolve_reactor()
        count += 1

        stable_nodes = 0

        for row in reactor:
            for node in row:
                if 1 <= node["energy"] <= 5:
                    stable_nodes += 1

        print(f"\n{GREEN}Stable Nodes: {stable_nodes}/25{RESET}   {YELLOW}Moves left: {35-count}{RESET}")

        if stable_nodes <= 5:
            print("\033[91mWARNING: Reactor highly unstable.\033[0m")
        elif stable_nodes >= 24:
            print("Final stabilisation required.")
        elif stable_nodes >= 20:
            print("Reactor fluctuations decreasing.")

        if reactor_stable():
            flush_pending()
            print_grid()

            win_screen("A_J4", "Use alphabet positions (A=1, B=2 ... Z=26)",
                       extra=f"Reactor stabilised in {count} moves!")

            return True

        if count == 35:
            flush_pending()
            print_grid()

            lose_screen("The reactor could not be stabilised in 35 moves.", "A_J4")

            return False


def open_chest_1(wordle_win=None):
    clear_screen()
    print(f"{RED} ----------------{RESET}79{RED}---------------------{RESET}")
    print(f"{RED}|{RESET}                                     47{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET} {GREEN}*{RESET}                      {RED}|{RESET}")
    print(f"98{RED}                                     |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|           {RESET}  {BLUE}#{RESET}                       {RED} |{RESET}")
    print(f"{RED}| {RESET}                                    33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    print(f"{CYAN}{BOLD}=== CHEST 1: WORDLE ==={RESET} 🔤")
    if wordle_win is not None:
        result = "WON" if wordle_win else "LOST"
        print(f"Previous game: Wordle {result}.")
    print(f"Enter the code revealed by Wordle to open this chest.")
    input("Press Enter to enter the Wordle code...")
    if wordle_win:
        notes.append("Chest 1 bonus hint: Num is alpha, alpha is num.")
    clear_screen()
    ###FIRST GAME PUZZLE
    clear_screen()
    print(f"{RED} ----------------{RESET}79{RED}---------------------{RESET}")
    print(f"{RED}|{RESET}                                     47")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET} {GREEN}*{RESET}                    {RED}  |{RESET}")
    print(f"98{RED}                                     |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET}                        |{RESET}")
    print(f"{RED}|{RESET}                                     33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    code=input("Enter the code to open the chest: ").strip()
    while(code!="B@D!"):
        print("Incorrect code. Please try again.")
        code=input("Enter the code to open the chest: ").strip()
    print("You have opened the first chest and found a clue stating: 'The correct door is the one with the number 4 in it's door number.'")
    notes.append("Chest 1 clue: the correct door has a 4 in its number.")
    input("Press Enter to continue...")

def open_chest_2(reactor_win=None):
    clear_screen()
    print(f"{RED} ----------------{RESET}79{RED}---------------------")
    print(f"{RED}|{RESET}                                     47")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET}                      {RED}  |{RESET}")
    print(f"98{RED}                                     |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET} {GREEN}*{RESET}{RED}                      |{RESET}")
    print(f"{RED}|{RESET}                                     33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    print(f"{RED}{BOLD}=== CHEST 2: REACTOR CORE ==={RESET} ⚡")
    if reactor_win is not None:
        result = "WON" if reactor_win else "LOST"
        print(f"Previous game: Reactor {result}.")
    print("Enter the code revealed by the reactor game to open this chest.")
    input("Press Enter to enter the reactor code...")
    if reactor_win:
        notes.append("Chest 2 bonus hint: Use alphabet positions (A=1, B=2 ... Z=26).")
    clear_screen()
    print(f"{RED} ----------------{RESET}79{RED}---------------------{RESET}")
    print(f"{RED}|{RESET}                                     47")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET}                      {RED}  |{RESET}")
    print(f"98{RED}                                     |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET} {GREEN}*{RESET}{RED}                      |{RESET}")
    print(f"{RED}|{RESET}                                     33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
###Puzzle for second chest
    code=input("Enter the code to open the chest: ").strip()
    while(code!="A_J4"):
        print("Incorrect code. Please try again.")
        code=input("Enter the code to open the chest: ").strip()
    print("You have opened the second chest and found a clue stating: 'The correct door is the one with the number 7 in it's door number.'")
    notes.append("Chest 2 clue: the correct door has a 7 in its number.")
    input("Press Enter to continue...")


def escape_room(wordle_win=None, reactor_win=None, maze_win=None):
    notes.clear()
    flag = 0
    clear_screen()
    print("WELCOME TO THE ESCAPE-ROOM GAME")
    print("\nPrevious game results:")
    for game_name, game_won, chest_code in (
        ("Wordle", wordle_win, "B@D!"),
        ("Reactor", reactor_win, "A_J4"),
        ("Maze", maze_win, "A0RU"),
    ):
        if game_won is not None:
            result = "WON" if game_won else "LOST"
            print("{}: {} (chest code: {})".format(game_name, result, chest_code))
    print("You are trapped in a room and you have to escape it by solving puzzles to open each chest.Each chest contain a clue for the escape.")
    print("You are inside one room with two chests and several doors. You can only enter one and only one door leads you to freedom")
    print("To find which door to go to, open each chest to find some clues.")
    print("* represents the player. - represents walls. number represents door number # represents chests")
    input("Press Enter to start the game...")
    clear_screen()
    print(f"{RED} ----------------{RESET}79{RED}---------------------{RESET}")
    print(f"{RED}|{RESET}                                     47")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET}                     {RED}   |{RESET}")
    print(f"98{RED}                                     |{RESET}")
    print(f"{RED}|                                  {RESET} {GREEN}*{RESET}{RED}  |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET} {RED}                       |{RESET}")
    print(f"{RED}|{RESET}                                     33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    print("Enter your command number to move the player.")
    print("Commands: 1. go near chest 1, 2. go near chest 2, N. clue notebook")
    command=ask()
    command=command.lower().strip()

    while(command!="1" and command!="2"):
        clear_screen()
        print(f"{RED} ----------------{RESET}79{RED}---------------------{RESET}")
        print(f"{RED}|{RESET}                                     47")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|{RESET}             {BLUE}#{RESET}                      {RED}  |{RESET}")
        print(f"98{RED}                                     |{RESET}")
        print(f"{RED}|                                  {RESET} {GREEN}*{RESET}{RED}  |{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|{RESET}             {BLUE}#{RESET} {RED}                       |{RESET}")
        print(f"{RED}|{RESET}                                     33")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
        print("Invalid command. Please enter a valid command.")
        command=ask("Enter your command: ")
        command=command.lower().strip()
    if(command=="1"):
        open_chest_1(wordle_win)
        flag=1
    elif(command=="2"):
        open_chest_2(reactor_win)
        flag=2
    print("Now open the other chest to find the other clues.")
    clear_screen()
    print(f"{RED} ----------------{RESET}79{RED}---------------------")
    print(f"{RED}|{RESET}                                     47")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET}                      {RED}  |{RESET}")
    print(f"98{RED}                                     |{RESET}")
    print(f"{RED}|                                  {RESET} {GREEN}*{RESET}{RED}  |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET} {RED}                       |{RESET}")
    print(f"{RED}|{RESET}                                     33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    print("Commands: 1. go near chest 1, 2. go near chest 2, N. clue notebook")
    command=ask("Enter your command number: ")
    command=command.lower().strip()
    while((command!="1" or flag!=2) and (command!="2" or flag!=1)):
        clear_screen()
        print(f"{RED} ----------------{RESET}79{RED}---------------------{RESET}")
        print(f"{RED}|{RESET}                                     47")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|{RESET}             {BLUE}#{RESET}                      {RED}  |{RESET}")
        print(f"98{RED}                                     |{RESET}")
        print(f"{RED}|                                  {RESET} {GREEN}*{RESET}{RED}  |{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|{RESET}             {BLUE}#{RESET} {RED}                       |{RESET}")
        print(f"{RED}|{RESET}                                     33")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
        if(command=="1" and flag==1) or (command=="2" and flag==2):
            print("You have already opened this chest. Move closer to the other chest to open it.")
        else:
            print("Invalid command. Please enter a valid command.")
        command=ask("Enter your command: ")
        command=command.lower().strip()
    if(command=="1" and flag==2):
        open_chest_1(wordle_win)
    elif(command=="2" and flag==1):
        open_chest_2(reactor_win)
    clear_screen()
    print(f"{RED} ----------------{RESET}79{RED}---------------------{RESET}")
    print(f"{RED}|{RESET}                                     47")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET}                      {RED}  |{RESET}")
    print(f"98{RED}                                     |{RESET}")
    print(f"{RED}|                                  {RESET} {GREEN}*{RESET}{RED}  |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|{RESET}             {BLUE}#{RESET} {RED}                       |{RESET}")
    print(f"{RED}|{RESET}                                     33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    print("The clues you have found in the chests are: 'The correct door is the one with the number 4 in it's door number.'")
    print("'The correct door is the one with the number 7 in it's door number.'")
    command=ask("Now that you have opened both chests, enter the door number you want to go through (N = notebook): ").strip()
    while(command!="47" and command!="33" and command!="16" and command!="54" and command!="98" and command!="79"):
        print("Invalid door number. Please enter a valid door number.")
        command=ask("Enter the door number you want to go through: ").strip()
    if(command!="47"):
        print("Incorrect door number,you fell into fire. Game Over. Run the game again to try and escape the room.")
        return False
    clear_screen()
    print("Congratulations! You have escaped one of the rooms. ")
    print("You enter another room and find one more chest. You can open this chest too by the code received after solving another puzzle.")
    print(f"{RED} ----------------{RESET}79{RED}---------------------------------------------------------{RESET}")
    print(f"{RED}|                                       __   {RESET}{GREEN}*{RESET} {RED}                            |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|             {BLUE}#{RESET}                        {RED}|  |                         {BLUE}#{RESET}     {RED} |{RESET}")
    print(f"98                                  {RED}   |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|                                      |  |      {RESET} {CYAN}___________________{RESET}{RED}      |{RESET}")
    print(f"{RED}|       {RESET}      {BLUE}#{RESET}                      {RED}  |   ------{RESET}{CYAN}[VICTORY DOOR:LOCKED]{RESET}{RED}------{RESET}")
    print(f"{RED}|      {RESET}                               33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    print("Enter your command number to move the player.")
    print("Commands: 1. go near chest 3, N. clue notebook")
    command=ask()
    command=command.lower().strip()
    while(command!="1"):
        clear_screen()
        print(f"{RED} ----------------{RESET}79{RED}---------------------------------------------------------{RESET}")
        print(f"{RED}|                                       __   {RESET}{GREEN}*{RESET} {RED}                            |{RESET}")
        print(f"{RED}|                                      |  |                                |{RESET}")
        print(f"{RED}|                                      |  |                                |{RESET}")
        print(f"{RED}|             {BLUE}#{RESET}                        {RED}|  |                         {BLUE}#{RESET}     {RED} |{RESET}")
        print(f"98                                  {RED}   |  |                                |{RESET}")
        print(f"{RED}|                                      |  |                                |{RESET}")
        print(f"{RED}|                                      |  |      {RESET}{CYAN} ___________________{RESET}{RED}      |{RESET}")
        print(f"{RED}|       {RESET}      {BLUE}#{RESET}                      {RED}  |   ------{RESET}{CYAN}[VICTORY DOOR:LOCKED]{RESET}{RED}------{RESET}")
        print(f"{RED}|      {RESET}                               33")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
        print("Invalid command. Please enter a valid command.")
        command=ask("Enter your command: ")
        command=command.lower().strip()

    clear_screen()
    print(f"{RED} ----------------{RESET}79{RED}---------------------------------------------------------{RESET}")
    print(f"{RED}|                                       __   {RESET}  {RED}                            |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|             {BLUE}#{RESET}                        {RED}|  |                    {GREEN}*{RESET}  {BLUE}#{RESET}       {RED} |{RESET}")
    print(f"98                                  {RED}   |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|                                      |  |      {RESET}{CYAN} ___________________{RESET}{RED}      |{RESET}")
    print(f"{RED}|       {RESET}      {BLUE}#{RESET}                      {RED}  |   ------{RESET}{CYAN}[VICTORY DOOR:LOCKED]{RESET}{RED}------{RESET}")
    print(f"{RED}|      {RESET}                               33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    print(f"{MAGENTA}{BOLD}=== CHEST 3: LABYRINTH ==={RESET} 🧭")
    if maze_win is not None:
        result = "WON" if maze_win else "LOST"
        print(f"Previous game: Maze {result}.")
    print("Enter the code revealed by the maze game to open this chest.")
    input("Press Enter to enter the maze code...")
    if maze_win:
        notes.append("Chest 3 bonus hint: The letter stays, only the number changes.")
    input("\nPress Enter to continue...")
    clear_screen()
    print(f"{RED} ----------------{RESET}79{RED}---------------------------------------------------------{RESET}")
    print(f"{RED}|                                       __   {RESET}  {RED}                            |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|             {BLUE}#{RESET}                        {RED}|  |                    {GREEN}*{RESET}  {BLUE}#{RESET}       {RED} |{RESET}")
    print(f"98                                  {RED}   |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|                                      |  |      {RESET}{CYAN} ___________________{RESET}{RED}      |{RESET}")
    print(f"{RED}|       {RESET}      {BLUE}#{RESET}                      {RED}  |   ------{RESET}{CYAN}[VICTORY DOOR:LOCKED]{RESET}{RED}------{RESET}")
    print(f"{RED}|      {RESET}                               33")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    ###Puzzle for third chest
    code=input("Enter the code to open the chest: ").strip()
    while(code!="A0RU"):
        print("Incorrect code. Please try again.")
        code=input("Enter the code to open the chest: ").strip()
    print(f"{GREEN}You opened the third chest and found the key for the victory door!{RESET}")
    print(f"The door glows with three codes: {YELLOW}{BOLD}[E19]  [C1]  [P5]{RESET}")
    notes.append("Victory door codes: E19, C1, P5. Decode them to get the secret word.")
    print(f"{MAGENTA}Decode them and type the secret word to open the door.{RESET}")
    command=input("Secret word: ").strip().upper()
    while(command!="ESCAPE"):
        clear_screen()
        print(f"{RED} ----------------{RESET}79{RED}---------------------------------------------------------{RESET}")
        print(f"{RED}|                                       __   {RESET}  {RED}                            |{RESET}")
        print(f"{RED}|                                      |  |                                |{RESET}")
        print(f"{RED}|                                      |  |                                |{RESET}")
        print(f"{RED}|             {RESET}{BLUE}#{RESET}                        {RED}|  |                      {RESET}{GREEN}*  {RESET}{BLUE}#{RESET}     {RED} |{RESET}")
        print(f"98                                  {RED}   |  |                                |{RESET}")
        print(f"{RED}|                                      |  |                                |{RESET}")
        print(f"{RED}|                                      |  |      {RESET}{CYAN} ___________________{RESET}{RED}      |{RESET}")
        print(f"{RED}|       {RESET}      {BLUE}#{RESET}                      {RED}  |  ------{RESET}{CYAN}[VICTORY DOOR:LOCKED]{RESET}{RED}------{RESET}")
        print(f"{RED}|      {RESET}                               33{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED}|                                      |{RESET}")
        print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
        print(f"{RED}Wrong word, the door stays locked.{RESET}")
        print(f"The door codes: {YELLOW}{BOLD}[E19]  [C1]  [P5]{RESET}")
        command=input("Secret word: ").strip().upper()

    clear_screen()
    print(f"{RED} ----------------{RESET}79{RED}---------------------------------------------------------{RESET}")
    print(f"{RED}|                                       __   {RESET}  {RED}                            |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|             {RESET}{BLUE}#{RESET}                        {RED}|  |                       {RESET}   {BLUE}#{RESET}   {RED}  |{RESET}")
    print(f"98                                  {RED}   |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|                                      |  |                                |{RESET}")
    print(f"{RED}|       {RESET}      {BLUE}#{RESET}                      {RED}  |   -----{RESET}{YELLOW}[VICTORY DOOR:UNLOCKED]{RESET}{RED}-----{RESET}")
    print(f"{RED}|      {RESET}                               33                  {GREEN}*{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED}|                                      |{RESET}")
    print(f"{RED} ---{RESET}54{RED}------------------------{RESET}16{RED}--------{RESET}")
    print("Congratulations! You have opened the victory door and escaped the room. You have won the game.")
    return True


if __name__ == "__main__":
    from main import main

    main()
