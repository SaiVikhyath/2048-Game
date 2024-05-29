

# Author: Sai Vikhyath K
# Date: 24 May 2024


import random


def startGame():
    board = [[0 for _ in range(4)] for _ in range(4)]
    return board


def addRandomTwo(board):
    row = random.randint(0, 3)
    column = random.randint(0, 3)

    while board[row][column] != 0:
        row = random.randint(0, 3)
        column = random.randint(0, 3)

    board[row][column] = 2


def getCurrentState(board):

    for r in range(4):
        for c in range(4):
            if board[r][c] == 2048:
                return "WON"
    
    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:
                return "GAME NOT OVER"

    for r in range(3):
        for c in range(3):
            if board[r][c] == board[r + 1][c] or board[r][c] == board[r][c + 1]:
                return "GAME NOT OVER"
    
    for c in range(3):
        if board[3][c] == board[3][c + 1]:
            return "GAME NOT OVER"
    
    for r in range(3):
        if board[r][3] == board[r + 1][3]:
            return "GAME NOT OVER"
    
    return "LOST"


def compress(board):
    newBoard = [[0 for _ in range(4)] for _ in range(4)]
    changed = False
    for r in range(4):
        pos = 0
        for c in range(4):
            if board[r][c] != 0:
                if pos != c:
                    changed = True
                newBoard[r][pos] = board[r][c]
                pos += 1
    return newBoard, changed


def merge(board):
    changed = False
    for r in range(4):
        for c in range(3):
            if board[r][c] == board[r][c + 1] and board[r][c] != 0:
                changed = True
                board[r][c] = board[r][c] * 2
                board[r][c + 1] = 0
    return board, changed


def reverse(board):
    newBoard = [[0 for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(3, -1, -1):
            newBoard[r][3 - c] = board[r][c]
    return  newBoard


def transpose(board):
    newBoard = [[0 for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            newBoard[c][r] = board[r][c]
    return newBoard


def moveLeft(board):
    tempBoard, changed1 = compress(board)
    tempBoard, changed2 = merge(tempBoard)
    changed = changed1 or changed2
    tempBoard, tmpChanged = compress(tempBoard)
    return tempBoard, changed


def moveRight(board):
    tempBoard = reverse(board)
    tempBoard, changed1 = compress(tempBoard)
    tempBoard, changed2 = merge(tempBoard)
    changed = changed1 or changed2
    tempBoard, tmpChanged = compress(tempBoard)
    tempBoard = reverse(tempBoard)
    return tempBoard, changed


def moveUp(board):
    tempBoard = transpose(board)
    tempBoard, changed1 = compress(tempBoard)
    tempBoard, changed2 = merge(tempBoard)
    changed = changed1 or changed2
    tempBoard, tmpChanged = compress(tempBoard)
    tempBoard = transpose(tempBoard)
    return tempBoard, changed

def moveDown(board):
    tempBoard = transpose(board)
    tempBoard = reverse(tempBoard)
    tempBoard, changed1 = compress(tempBoard)
    tempBoard, changed2 = merge(tempBoard)
    changed = changed1 or changed2
    tempBoard, tmpChanged = compress(tempBoard)
    tempBoard = reverse(tempBoard)
    tempBoard = transpose(tempBoard)
    return tempBoard, changed



