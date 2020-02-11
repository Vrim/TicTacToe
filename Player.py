from __future__ import annotations
from typing import Any, Tuple, List

class Player():
	""" Tic Tac Toe
	Author: Cameron Fairchild
	Date: Oct. 11, 2019

	----- Player -----
	Player class represents the Player(s)

	Keeps track of Players in the game and their scores, symbols, names.
	"""
	symbol: str
	name: str
	_wins: int
	_losses: int
	_ties: int

	def __init__(self, symbol : str, name: str) -> None:
		self.symbol = symbol
		self.name = name
		self._wins = 0
		self._losses = 0
		self._ties = 0

	def getScore(self) -> Tuple[int, int, int]:
		return (self._wins, self._losses, self._ties)

	def calcGamesPlayed(self) -> int:
		"""Returns the number of games played

		>>>p1 = Player('x', "Hi")
		>>>p2 = Player('y', "Bye")
		>>>t = TicTac()
		>>>t.play(0, p1)
		>>>t.play(3, p2)
		>>>t.play(1, p1)
		>>>t.play(4, p2)
		>>>t.play(2, p1)
		>>>p1.calcGamesPlayed()
		1

		"""
		gamesPlayed = self._wins + self._losses + self._ties
		return gamesPlayed



if __name__ == "__main__":
	import doctest
	doctest.testmod()