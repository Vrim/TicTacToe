from __future__ import annotations
from typing import Any, List
from Player import Player

class TicTac():
	""" Tic Tac Toe
	Author: Cameron Fairchild
	Date: Oct. 11, 2019

	----- TicTac -----
	TicTac class represents the gameboard and board state.

	Keeps track of placements on the board
	"""
	board: List[List[Player]]
	player1: Player
	player2: Player
	mode: int

	def __init__(self, mode: int, p1: Player, p2: Player) -> None:
		b = [
			[None, None, None],
			[None, None, None],
			[None, None, None]
		]
		self.board = b
		self.player1 = p1
		self.player2 = p2
		self.mode = mode
	
	def __str__(self) -> str:
		board = self.board
		s = ''
		# First row	
		s += (" {} | {} | {} \n".format(
			('7' if board[0][2] is None else board[0][2].symbol),
			('8' if board[1][2] is None else board[1][2].symbol),
			('9' if board[2][2] is None else board[2][2].symbol)
			 ))
		# Line
		s += ("-----------\n")
		# Middle row
		s += (" {} | {} | {} \n".format(
			('4' if board[0][1] is None else board[0][1].symbol),
			('5' if board[1][1] is None else board[1][1].symbol),
			('6' if board[2][1] is None else board[2][1].symbol)
			))
		# Line
		s += ("-----------\n")
		# Last row
		s += (" {} | {} | {} \n".format(
			('1' if board[0][0] is None else board[0][0].symbol),
			('2' if board[1][0] is None else board[1][0].symbol),
		 	('3' if board[2][0] is None else board[2][0].symbol)
			))
		return s

	def place(self, p: Player, i: int) -> bool:
		"""Attempts to place and returns bool for success
		"""
		x = (i-1) % 3
		y = (i - x - 1)//3

		if self.board[x][y] is not None:
			return False
		self.board[x][y] = p
		return True

	def checkWin(self) -> (bool, Player):
		""" Checks if there is a win in the board
		Returns bool for win and Player that won
		Returns True, None for draw
		"""
		# Col-win
		board = self.board
		for x in range(3):
			first = board[x][0]
			if first is None:
				continue
			for y in range(2):
				if board[x][y + 1] != first:
					break
			else:
				return (True, first)
		
		# Row-win
		for y in range(3):
			first = board[0][y]
			if first is None:
				continue
			for x in range(2):
				if board[x + 1][y] != first:
					break
			else:
				return (True, first)
		
		# Diagonal win
		center = board[1][1]
		if center is not None:			
			# First diagonal \
			if board[0][2] == center and board[2][0] == center:
				return (True, center)
			# Other diagonal /
			elif board[0][0] == center and board[2][2] == center:
				return (True, center)

		# Draw
		for x in range(3):
			for y in range(3):
				if board[x][y] is None:
					return (False, None)
		return (True, None)
		
if __name__ == "__main__":
	import doctest
	doctest.testmod()