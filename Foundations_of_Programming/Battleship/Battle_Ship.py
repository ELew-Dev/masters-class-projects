import random

def setupBoard():
    # Create a 10x10 board filled with '.'
    board = [['.' for _ in range(10)] for _ in range(10)]
    
    # Place 5 ships ('S') randomly on the board
    num_ships = 5
    placed_ships = 0
    
    while placed_ships < num_ships:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        
        if board[row][col] == '.':  # ships won't overlap
            board[row][col] = 'S'
            placed_ships += 1
    
    return board

def drawBoard(board):
    print("  " + " ".join(str(i) for i in range(10)))  # Column labels
    for i, row in enumerate(board):
        print(str(i) + " " + " ".join(row))  # Row labels with board data

def checkHitOrMiss(board, row, col):
    if board[row][col] == 'S':
        board[row][col] = 'X'
        return "HIT"
    elif board[row][col] == 'X':
        return "HIT"
    else:
        board[row][col] = 'O'
        return "MISS"

def isGameOver(board):
    for row in board:
        if 'S' in row:
            return False
    return True

def main():
    board = setupBoard()
    
    while not isGameOver(board):
        drawBoard(board)
        
        # Get user input for column
        while True:
            try:
                col = int(input("Enter a column (X): "))
                if 0 <= col < 10:
                    break
                print("Invalid column.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Get user input for row
        while True:
            try:
                row = int(input("Enter a row (Y): "))
                if 0 <= row < 10:
                    break
                print("Invalid row.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Check hit or miss
        result = checkHitOrMiss(board, row, col)
        print(result)
        
    drawBoard(board)
    print("GAME OVER!")

if __name__ == "__main__":
    main()
