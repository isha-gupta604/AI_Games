import random
def create_board():
    board=[]
    for i in range(3):
        row = []
        for j in range(3):
            row.append('-')
        board.append(row)
    return board
def show_board(board):
        for row in board:
            for item in row:
                print(item, end=" ")
            print()
def fix_spot(board,row,col,player):
     board[row][col]=player
def player_win(board,player):
    n = len(board)
    for i in range(n):
        if all([board[i][j] == player for j in range(n)]):
            return True
    for i in range(n):
        if all([board[j][i] == player for j in range(n)]):
            return True
    if all([board[i][i] == player for i in range(n)]):
        return True
    if all([board[i][n - 1 - i] == player for i in range(n)]):
        return True
    return False
def board_filled(board):
    n=len(board)
    for row in range(n):
        if any([board[row][j]=='-' for j in range(n)]):
            return False
    return True
def swap_player_turn(player):
    return 'X' if player == 'O' else 'O'
def TicTacToe():
    board=create_board()
    player="X" if random.randint(0, 1)==0 else "O"
    while True:
        print(f"It's {player} turn: ")
        show_board(board)
        try:
            row, col = map(int, input("Enter row and column numbers (1-3): ").split())
            if board[row - 1][col - 1] != '-':
                print("Spot already taken. Try again.\n")
                continue
            fix_spot(board,row - 1, col - 1, player)
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 1 and 3.\n")
            continue
        if player_win(board,player):
            print(f"\n\n*******Player {player} wins the game!********")
            break
        if board_filled(board):
            print("Match Draw!")
            break
        player = swap_player_turn(player)
        print()
    show_board(board)
TicTacToe()