EMPTY = 0
BLACK = 1
WHITE = -1

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0), (1, 1)
]

def create_board():
    board = [[EMPTY for _ in range(8)] for _ in range(8)]
    board[3][3] = WHITE
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[4][4] = WHITE
    return board

def print_board(board):
    print("  0 1 2 3 4 5 6 7")
    for i, row in enumerate(board):
        print(i, end=" ")
        for cell in row:
            if cell == BLACK:
                print("B", end=" ")
            elif cell == WHITE:
                print("W", end=" ")
            else:
                print(".", end=" ")
        print()
def is_valid_move(board, row, col, player):
    if board[row][col] != EMPTY:
        return False

    opponent = -player

    for dr, dc in DIRECTIONS:
        r, c = row + dr, col + dc
        found_opponent = False

        while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
            r += dr
            c += dc
            found_opponent = True

        if found_opponent and 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
            return True

    return False
def get_valid_moves(board, player):
    moves = []
    for r in range(8):
        for c in range(8):
            if is_valid_move(board, r, c, player):
                moves.append((r, c))
    return moves
def apply_move(board, row, col, player):
    new_board = [row[:] for row in board]
    new_board[row][col] = player
    opponent = -player

    for dr, dc in DIRECTIONS:
        r, c = row + dr, col + dc
        tiles_to_flip = []

        while 0 <= r < 8 and 0 <= c < 8 and new_board[r][c] == opponent:
            tiles_to_flip.append((r, c))
            r += dr
            c += dc

        if tiles_to_flip and 0 <= r < 8 and 0 <= c < 8 and new_board[r][c] == player:
            for rr, cc in tiles_to_flip:
                new_board[rr][cc] = player

    return new_board

if __name__ == "__main__":
    board = create_board()
    print_board(board)

    moves = get_valid_moves(board, BLACK)
    print("Valid moves for BLACK:", moves)
