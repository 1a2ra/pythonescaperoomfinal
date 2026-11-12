def maze_game(reactor_win=None, quit_attempt=1):
    import random
    import os

    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

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

    clear_screen()
    print("=" * 31)
    print("     THE LABYRINTH QUEST")
    print("=" * 31)
    print("Find the key (K) and reach the exit (X)!")
    print("Avoid the enemy (E)!\n")

    if reactor_win is not None:
        if reactor_win:
            print("Previous game: Reactor WON.")
        else:
            print("Previous game: Reactor LOST.")
        print("Reactor chest code: A_J4")
    if quit_attempt > 1:
        print("Maze attempt {}/3.".format(quit_attempt))

    print("CONTROLS:")
    print("  [W] Up")
    print("  [S] Down")
    print("  [A] Left")
    print("  [D] Right")
    print("  [Q] Quit")
    print("=" * 31)
    input("Press Enter to start...")

    while game_over == False:
        clear_screen()
        print("\n" + "-" * 27)

        r = 0
        while r < len(maze):
            line = ""
            c = 0
            while c < len(maze[r]):
                if r == player_row and c == player_col:
                    line += "P "
                elif r == enemy_row and c == enemy_col:
                    line += "E "
                elif r == key_row and c == key_col and not has_key:
                    line += "K "
                elif r == exit_row and c == exit_col:
                    line += "X "
                else:
                    line += maze[r][c] + " "
                c += 1
            print(line)
            r += 1

        print("-" * 27)
        if has_key == True:
            print("Status: Key Collected! Head to the exit!")
        else:
            print("Status: Key Needed!")

        move = input("Your move (W/A/S/D, Q): ").strip().upper()

        if move == "Q":
            print("You quit the game. Goodbye!")
            if quit_attempt < 3:
                return maze_game(reactor_win, quit_attempt + 1)
            game_over = True
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
            input("Press Enter to continue...")
            continue

        if maze[new_row][new_col] == "#":
            print("Ouch! You hit a wall!")
            input("Press Enter to continue...")
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
                input("Press Enter to continue...")

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


    clear_screen()
    if won == True:
        print("\nCONGRATULATIONS! YOU BEAT THE GAME!")
        print()
        print("CHEST 3 CODE: A0RU")
        print("Hint: Alpha is number, number is alpha")
        return True
    elif game_over == True:
        print("\nGAME OVER! Better luck next time.")
        print()
        print("CHEST 3 CODE: A0RU")
        print("Penalty: No bonus hint.")
        return False
if __name__ == "__main__":
    maze_game()
