TOTAL_PIECES = 16  # Per player
TOTAL_PAWNS = 8
BOARD_DIMS = 8  # Always square
VALID_COLORS = ['b', 'w']
VALID_PIECE_NAMES = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
BOARD = {'1a': 'wking', '1b': 'wpawn'}


def isValidChessBoard(board):
    # Check King Count
    wking_count = 0
    bking_count = 0
    for piece in board.values():
        if piece == 'wking':
            wking_count += 1
        elif piece == 'bking':
            bking_count += 1

    if wking_count != 1:
        raise Exception(f"Incorrect number of white kings! Found {wking_count}")
    if bking_count != 1:
        raise Exception(f"Incorrect number of black kings! Found {bking_count}")

    # Check total pieces
    black_count = 0
    white_count = 0
    for piece in board.values():
        if piece[:1] == 'w':
            white_count += 1
        elif piece[:1] == 'b':
            black_count += 1
        else:
            raise Exception(f"Unexpected first letter for a piece: {piece}")

    if white_count > 16:
        raise Exception("White has too many pieces!")
    if black_count > 16:
        raise Exception("Black has too many pieces")

    # Check pawn counts
    # TODO Complete later
    # Check valid spaces
    for space in board:
        space_number = int(space[:1])
        space_letter = space[1:]
        if (
            space_number < 1
            or space_number > BOARD_DIMS
            or (ord(space_letter) - 96) < 1
            or (ord(space_letter) - 96) > BOARD_DIMS
        ):
            raise Exception(f"Invalid space: {space}")

    # Check valid names
    for piece in board.values():
        if piece[1:] not in VALID_PIECE_NAMES:
            raise Exception(f"Invalid piece name: {piece[1:]}")


if __name__ == "__main__":
    isValidChessBoard(BOARD)
