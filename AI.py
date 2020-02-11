from __future__ import annotations

import math
import sys
from typing import List, Union

from Player import Player
from TicTac import TicTac


def AI(board: TicTac, p: Player) -> (int, int):
    """TicTacToe AI
    Calculaes the best move for the AI using minimax
    """
    r = _minimax(board, p.symbol, p.symbol)
    return r

def _minimax(board: TicTac, p: str, curr: str):
    

    b = board.board
    empty = []
    moves = []
    for x in range(3):
        for y in range(3):
            if b[x][y] is None:
                empty.append((x, y))
    
    for e in empty:
        move = {}
        move['loc'] = e
        new_board = _copyBoard(board)
        x, y = e
        new_board.board[x][y] = p
        if curr == p: # AI
            result = _score(new_board, p, 'X' if p == 'O' else 'O')
        else:
            result = _score(new_board, p, p)        
        move['score'] = result
        moves.append(move)

    bestMove = None
    if curr == p:
        best = math.inf * -1
        for move in moves:
            if move['score'] > best:
                best = move['score']
                bestMove = move['loc']
    else:
        best = math.inf
        for move in moves:
            if move['score'] < best:
                best = move['score']
                bestMove = move['loc']
    return bestMove

def _score(b: TicTac, p: str, curr: str) -> int:
    done, winner = b.checkWin()
    if done and winner == p:
        return 1
    elif done and winner is not None:
        return -1
    else:
        return 0
        
def _copyBoard(b1: TicTac) -> TicTac:
    b = b1.board
    new = TicTac(b1.mode, b1.player1, b1.player2)
    newb = new.board
    for x in range(3):
        for y in range(3):
            newb[x][y] = b[x][y]
    return new

    score: int
    x: int
    y: int

    def __gt__(self, other: Player) -> bool:
        return self.score > other.score

    def __eq__(self, other: Player) -> bool:
        return self.score == other.score
