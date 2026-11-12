def reactor_puzzle(wordle_win=None):
    import os
    import shutil

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def check_terminal_size():
        width, height = shutil.get_terminal_size()
        return width >= 80 and height >= 24

    clear_screen()

    # Initial title / log intro printed once at startup
    print(
        "\033[91m"
        "==================================================\n"
        "WARNING: REACTOR CORE UNSTABLE\n"
        "==================================================\n"
        "\033[0m\n"
        "\033[93mChief Engineer's Log\033[0m\n\n"
        "The thermal and electric subsystems are interacting\n"
        "in unexpected ways.\n\n"
        "Stabilise all 25 nodes within 35 moves or the station\n"
        "will be lost.\n\n"
        "\033[96mREACTOR STABILISATION PROTOCOL\033[0m\n\n"
        "Enter coordinates A1-E5 | HINT | QUIT\n"
        "\033[92mT = Thermal (Orthogonal) | E = Electric (Diagonal)\033[0m\n"
    )

    if wordle_win is not None:
        if wordle_win:
            print("Previous game: Wordle WON.")
            print("Bonus hint earned. Wordle chest code: B@D!")
        else:
            print("Previous game: Wordle NOT WON.")
            print("Recovery code revealed: B@D!. Bonus hint was lost.")

    if not check_terminal_size():
        print("Note: Terminal is smaller than the recommended 80x24.")

    input("Press Enter to begin stabilisation protocol...")

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
    status_message = "Awaiting input."

    def print_grid(status_message=""):
        clear_screen()
        stable_nodes = sum(1 for row in reactor for node in row if 1 <= node["energy"] <= 5)

        print("\033[91m==================================================\033[0m")
        print(f" REACTOR CORE | Stable: {stable_nodes}/25 | Moves Left: {35 - count}")
        print("\033[91m==================================================\033[0m")
        print("       1   2   3   4   5")
        
        for row in range(5):
            line_str = f" {row_letters[row]}   "
            for col in range(5):
                node = reactor[row][col]
                line_str += f" {node['type']}{node['energy']}  "
            print(line_str)

        print("-" * 50)
        print(f"STATUS: {status_message[:70]}")
        print("-" * 50)

    def thermal_overload(row, col):
        nonlocal status_message
        reactor[row][col]["energy"] = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 5 and 0 <= nc < 5:
                reactor[nr][nc]["energy"] += 1
        status_message = f"THERMAL OVERLOAD at {row_letters[row]}{col+1}"

    def electric_overload(row, col):
        nonlocal status_message
        reactor[row][col]["energy"] = 0
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 5 and 0 <= nc < 5:
                reactor[nr][nc]["energy"] += 1
        status_message = f"ELECTRIC OVERLOAD at {row_letters[row]}{col+1}"

    def reactor_stable():
        return all(1 <= node["energy"] <= 5 for row in reactor for node in row)

    def find_overload():
        return [(r, c) for r in range(5) for c in range(5) if reactor[r][c]["energy"] >= 10]

    def resolve_reactor():
        overload = find_overload()
        safety_breakout = 0
        while overload and safety_breakout < 100:
            row, col = overload.pop(0)
            if reactor[row][col]["type"] == "T":
                thermal_overload(row, col)
            else:
                electric_overload(row, col)
            overload = find_overload()
            safety_breakout += 1

    def hint_system():
        stable_nodes = sum(1 for row in reactor for node in row if 1 <= node["energy"] <= 5)
        unstable_count = 25 - stable_nodes

        if unstable_count == 0:
            return "All reactor systems stable."
        if unstable_count > 15:
            return "Focus on reducing extremely high or extremely low energy values first."
        if unstable_count > 5:
            return "Thermal = orthogonal neighbors | Electric = diagonals."

        for r in range(5):
            for c in range(5):
                energy = reactor[r][c]["energy"]
                if energy < 1 or energy > 5:
                    return f"Node {row_letters[r]}{c+1} unstable (Energy={energy})."
        return "Analyze subsystem interactions carefully."

    while True:
        print_grid(status_message)

        node_charge = (
            input("\nEnter node (A1-E5): ").strip().replace(" ", "").upper()
        )

        if node_charge == "QUIT":
            clear_screen()
            print("\nMission Aborted.")
            print("Chest 2 code: A_J4")
            return False

        if node_charge == "HINT":
            status_message = hint_system()
            continue

        if len(node_charge) != 2:
            status_message = "Invalid input. Use A1-E5."
            continue

        letter = node_charge[0]
        number = node_charge[1]

        if letter not in row_letters or not number.isdigit() or not (1 <= int(number) <= 5):
            status_message = "Invalid input. Use A1-E5."
            continue

        target_row = row_letters.index(letter)
        target_col = int(number) - 1

        reactor[target_row][target_col]["energy"] += 1
        status_message = f"Node {letter}{number} charged."

        resolve_reactor()
        count += 1

        stable_nodes = sum(1 for row in reactor for node in row if 1 <= node["energy"] <= 5)

        if stable_nodes <= 5:
            status_message = f"Node {letter}{number} charged. \033[91mWARNING: Reactor highly unstable.\033[0m"
        elif stable_nodes >= 24:
            status_message = f"Node {letter}{number} charged. Final stabilisation required."
        elif stable_nodes >= 20:
            status_message = f"Node {letter}{number} charged. Reactor fluctuations decreasing."

        if reactor_stable():
            clear_screen()
            efficiency = count / 35
            print("\n" + "=" * 50)
            print("REACTOR STABILISED")
            print("=" * 50)
            print(f"Efficiency Rating: {efficiency}")
            print("\nBonus Hint: Use alphabet positions (A=1, B=2, ..., Z=26).")
            print("Code Chest 2:A_J4")
            return True

        if count == 35:
            clear_screen()
            print("=" * 50)
            print("MISSION FAILED")
            print("=" * 50)
            print(f"Stable nodes: {stable_nodes}/25")
            print("The reactor could not be stabilised in 35 moves.")
            print("Chest 2 code: A_J4")
            print("Penalty: No bonus hint.")
            return False

if __name__ == "__main__":
    reactor_puzzle()
