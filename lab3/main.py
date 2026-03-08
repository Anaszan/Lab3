import time
import math

# ==================================================
# GLOBAL VARIABLES (สถิติการทำงาน)
# ==================================================
nodes_explored = 0
pruned_branches = 0

# ==================================================
# PLAYER & BOARD SYMBOLS
# ==================================================
EMPTY = " "
HUMAN = ""
AI = ""

# ==================================================
# BASIC BOARD FUNCTIONS
# ==================================================
def print_board(board):
    """แสดงกระดานเกม"""
    print()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                print(f" {i*3 + j + 1} ", end="")
            else:
                print(f" {board[i][j]} ", end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print("---+---+---")
    print()

def check_winner(board):
    """ตรวจสอบผู้ชนะ"""
    win_patterns = [
        # rows
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        # columns
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        # diagonals
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)]
    ]

    for pattern in win_patterns:
        a, b, c = pattern
        if board[a[0]][a[1]] != EMPTY and \
           board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]]:
            return board[a[0]][a[1]]
    return None

def is_draw(board):
    """ตรวจสอบเสมอ"""
    for row in board:
        if EMPTY in row:
            return False
    return True

def is_game_over(board):
    """ตรวจสอบว่าเกมจบหรือยัง"""
    return check_winner(board) is not None or is_draw(board)

def get_available_moves(board):
    """หาตำแหน่งที่ยังว่าง"""
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i, j))
    return moves

def make_move(board, row, col, player):
    """ลงหมาก"""
    board[row][col] = player
# ==================================================
# EVALUATION FUNCTION
# ==================================================
def evaluate(board):
    """
    ประเมินคะแนนของกระดาน
    AI ชนะ = +10
    HUMAN ชนะ = -10
    เสมอ / ยังไม่จบ = 0
    """
    winner = check_winner(board)
    if winner == AI:
        return 10
    elif winner == HUMAN:
        return -10
    return 0

# ==================================================
# MINIMAX ALGORITHM
# ==================================================
def minimax(board, depth, is_max):
    global nodes_explored
    nodes_explored += 1

    score = evaluate(board)
    if score != 0 or depth == 0 or is_draw(board):
        return score

    if is_max:
        best = -math.inf
        for (r, c) in get_available_moves(board):
            board[r][c] = AI
            best = max(best, minimax(board, depth - 1, False))
            board[r][c] = EMPTY
        return best
    else:
        best = math.inf
        for (r, c) in get_available_moves(board):
            board[r][c] = HUMAN
            best = min(best, minimax(board, depth - 1, True))
            board[r][c] = EMPTY
        return best

# ==================================================
# MINIMAX WITH ALPHA-BETA PRUNING
# ==================================================
def minimax_alpha_beta(board, depth, alpha, beta, is_max):
    global nodes_explored, pruned_branches
    nodes_explored += 1

    score = evaluate(board)
    if score != 0 or depth == 0 or is_draw(board):
        return score

    if is_max:
        best = -math.inf
        for (r, c) in get_available_moves(board):
            board[r][c] = AI
            best = max(best, minimax_alpha_beta(board, depth - 1, alpha, beta, False))
            board[r][c] = EMPTY
            alpha = max(alpha, best)
            if beta <= alpha:
                pruned_branches += 1
                break
        return best
    else:
        best = math.inf
        for (r, c) in get_available_moves(board):
            board[r][c] = HUMAN
            best = min(best, minimax_alpha_beta(board, depth - 1, alpha, beta, True))
            board[r][c] = EMPTY
            beta = min(beta, best)
            if beta <= alpha:
                pruned_branches += 1
                break
        return best

# ==================================================
# FIND BEST MOVE
# ==================================================
def find_best_move(board, use_alpha_beta=False):
    global nodes_explored, pruned_branches
    nodes_explored = 0
    pruned_branches = 0

    best_value = -math.inf
    best_move = None

    start_time = time.time()

    for (r, c) in get_available_moves(board):
        board[r][c] = AI
        if use_alpha_beta:
            move_val = minimax_alpha_beta(board, 9, -math.inf, math.inf, False)
        else:
            move_val = minimax(board, 9, False)
        board[r][c] = EMPTY

        if move_val > best_value:
            best_value = move_val
            best_move = (r, c)

    elapsed_time = time.time() - start_time
    return best_move, elapsed_time

# ==================================================
# GAME LOOP
# ==================================================
def game_loop():
    global HUMAN, AI

    board = [[EMPTY]*3 for _ in range(3)]

    print("TIC-TAC-TOE WITH AI")
    print("===================")

    print("Select your symbol:")
    print("1. X (play first)")
    print("2. O (play second)")
    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        HUMAN = "X"
        AI = "O"
        turn = HUMAN
    else:
        HUMAN = "O"
        AI = "X"
        turn = AI

    print("\nSelect AI algorithm:")
    print("1. Minimax")
    print("2. Minimax with Alpha-Beta Pruning")
    algo = input("Enter choice (1 or 2): ")
    use_alpha_beta = algo == "2"

    total_ai_time = 0
    total_moves = 0

    while not is_game_over(board):
        print_board(board)

        if turn == HUMAN:
            while True:
                try:
                    pos = int(input(f"Your turn ({HUMAN}). Enter position (1-9): "))
                    if pos < 1 or pos > 9:
                        print("Error: Enter number 1-9")
                        continue
                    r, c = divmod(pos - 1, 3)
                    if board[r][c] != EMPTY:
                        print("Error: Position already taken!")
                        continue
                    make_move(board, r, c, HUMAN)
                    break
                except:
                    print("Error: Invalid input!")
        else:
            print("AI is thinking...")
            move, elapsed = find_best_move(board, use_alpha_beta)
            make_move(board, move[0], move[1], AI)
            total_ai_time += elapsed

            print(f"[AI] Nodes explored: {nodes_explored}")
            if use_alpha_beta:
                print(f"[AI] Pruned branches: {pruned_branches}")
            print(f"[AI] Time: {elapsed:.4f} sec")

        total_moves += 1
        turn = AI if turn == HUMAN else HUMAN

    print_board(board)
    winner = check_winner(board)

    print("===================")
    if winner == AI:
        print("GAME OVER - AI WINS!")
    elif winner == HUMAN:
        print("GAME OVER - YOU WIN!")
    else:
        print("GAME OVER - DRAW!")
    print("===================")

    print("Game Statistics:")
    print(f"- Total moves: {total_moves}")
    print(f"- AI Algorithm: {'Alpha-Beta Pruning' if use_alpha_beta else 'Minimax'}")
    print(f"- Total nodes explored by AI: {nodes_explored}")
    if use_alpha_beta:
        print(f"- Total branches pruned: {pruned_branches}")
    print(f"- Average AI time: {total_ai_time / max(1, total_moves):.4f} sec")

# ==================================================
# MAIN
# ==================================================
if __name__ == "__main__":
    game_loop()