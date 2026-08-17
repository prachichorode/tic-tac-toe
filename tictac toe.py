# CODSOFT Task 2: Tic-Tac-Toe AI

board = [" " for _ in range(9)]


def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def is_full():
    return " " not in board


def minimax(is_maximizing):
    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_full():
        return 0

    if is_maximizing:
        best_score = -1000

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = 1000

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def ai_move():
    best_score = -1000
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


print("TIC-TAC-TOE")
print("You are X")
print("AI is O")

while True:
    print_board()

    try:
        move = int(input("Enter position (1-9): ")) - 1

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move. Try again.")
            continue

        board[move] = "X"

    except ValueError:
        print("Please enter a number from 1 to 9.")
        continue

    if check_winner("X"):
        print_board()
        print("You win!")
        break

    if is_full():
        print_board()
        print("It's a draw!")
        break

    print("AI is thinking...")
    ai_move()

    if check_winner("O"):
        print_board()
        print("AI wins!")
        break

    if is_full():
        print_board()
        print("It's a draw!")
        break