#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

HUMAN = -1
AI = 1
EMPTY = 0

def print_board(board):
    for row in board:
        print("|", end=" ")
        for cell in row:
            symbol = "X" if cell == HUMAN else "O" if cell == AI else " "
            print(symbol, end=" | ")
        print()
    print()

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    if all(cell != EMPTY for row in board for cell in row):
        return 0
    return None

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner is not None:
        return winner * (10 - depth) if winner == AI else winner * (depth - 10) if winner == HUMAN else 0
    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                eval = minimax(board, 0, False)
                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def main():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    current_player = HUMAN
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        if current_player == HUMAN:
            try:
                row, col = map(int, input("Enter your move (row col): ").split())
                if board[row][col] != EMPTY:
                    print("Invalid move. Try again.")
                    continue
                board[row][col] = HUMAN
            except ValueError:
                print("Invalid input. Please enter two integers separated by space.")
                continue
            except IndexError:
                print("Invalid move. Row and column should be within 0 to 2.")
                continue
        else:
            print("AI is thinking...")
            row, col = find_best_move(board)
            board[row][col] = AI
            print(f"AI played at row {row}, column {col}")
        print_board(board)
        winner = check_winner(board)
        if winner is not None:
            if winner == HUMAN:
                print("You win!")
            elif winner == AI:
                print("AI wins!")
            else:
                print("It's a draw!")
            break
        current_player = -current_player

if __name__ == "__main__":
    main()

