""" Tic Tac Toe
Author: Cameron Fairchild
Date: Oct. 11, 2019
"""
from __future__ import annotations
from typing import Any, List
from Player import Player
from TicTac import TicTac
import os
from AI import AI as ai

board: TicTac

def main():
    mode = _selectMode()
    if mode == 0:
        p1 = Player('X', _askName("P1: "))
        p2 = Player('O', "AI")
    elif mode == 1:
        p1 = Player('X', _askName("P1: "))
        p2 = Player('O', _askName("P2: "))        
    else:
        p1 = Player('X', "AI 1")
        p2 = Player('O', "AI 2")
    
    board = TicTac(mode, p1, p2)
    a = False 
    c = ''
    players = [p1, p2]
    curr = 0
    print(board)
    while not a:
        _playTurn(board, mode, players, curr)
        print(board)
        a, c = board.checkWin()
        curr = abs(curr - 1)
    print("{} Wins".format("Nooone" if c is None else c.name))

def _playTurn(board: TicTac, mode: int, players: List, curr: int) -> None:
    if mode == 0:
        if curr == 0:
            a = False
            while not a:
                a = board.place(players[0], _askPlace())
        else:
            x, y = ai(board, players[1])
            board.place(players[1], y * 3 + x + 1) 
    elif mode == 1:
        a = False
        while not a:
            a = board.place(players[curr], _askPlace())
    else:
        x, y = ai(board, players[curr])
        board.place(players[curr], y * 3 + x + 1)

def _askPlace() -> int:
    a = ''
    while not a.isdigit() or not int(a) in range(1, 9 + 1):
        a = input("Spot #: ")
    return int(a)

def _selectMode() -> int:
    a = ''
    while not a.isnumeric() or not int(a) in range(3):
        _clear()
        a = input("Select gamemode:\n\
                   0. One-Player\n\
                   1. Two-Player\n\
                   2. AI vs AI\n")
    return int(a)

def _askName(prompt: str) -> str:
    a = ''
    while len(a) < 1:
        a = input(prompt)
    return a

def _clear() -> None:
    """ Clears the console
    """
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()