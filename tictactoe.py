"""
Tic Tac Toe Player
"""

import math


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # X get's the first move
    nX=0 # number of 'X'
    nO=0 # number of 'Y
    for i in range(3):
        for j in range(3):
            if (board[i][j]==X):
                nX=nX+1
            elif (board[i][j]==O):
                nO=nO+1
    if nX==nO:
        return X
    elif nX>nO:
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available=set()
    for i in range(3):
        for j in range(3):
            if (board[i][j]==EMPTY):
                available.add((i,j))
    return available
                



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    currentPlayer=player(board)
    newboard=board
    newboard[action[0]][action[1]]=currentPlayer
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #checking rows
    for i in range(3):
        nX=0
        nO=0
        for j in range(3):
            if (board[i][j]==X):
                nX=nX+1
            elif (board[i][j]==O):
                nO=nO+1
        if (nX==3):
            return X
        elif (nO==3):
            return O
    #checking columns
    for j in range(3):
        nX=0
        nO=0
        for i in range(3):
            if (board[i][j]==X):
                nX=nX+1
            elif (board[i][j]==O):
                nO=nO+1
        if (nX==3):
            return X
        elif (nO==3):
            return O
    #checking diagnol
    nX=0
    nO=0
    for i in range(3):
        for j in range(3):
            if i==j:
                if (board[i][j]==X):
                    nX=nX+1
                elif (board[i][j]==O):
                    nO=nO+1
            else:
                continue
                
    if (nX==3):
        return X
    elif (nO==3):
        return O
    return None 


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move

def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move
