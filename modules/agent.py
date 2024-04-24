import numpy as np

WIN_TARGET = 3

class Agent:
	def __init__(self, map, order):
		self.map = map
		self.player_order = order

	def choose_cell(self):
		pass

class RandomAgent(Agent):
	pass

class SmartAgent(Agent):
	def checkRow(self): 	#return index
		for i in range(self.map.h):
			checkVal = -1
			count = 0
			for j in range(self.map.w):
				if (count == 0 and checkVal == -1):
					checkVal = self.map.cells[i][j]
					count += 1
				elif (self.map.cells[i][j] == checkVal):
					count += 1
				else:
					checkVal = self.map.cells[i][j]
					count = 1
				if count >= WIN_TARGET:
					return (i, j)
		return (-1, -1)

	def checkCol(self): 	#return index
		for i in range(self.map.w):
			checkVal = -1
			count = 0
			for j in range(self.map.h):
				if (count == 0 and checkVal == -1):
					checkVal = self.map.cells[j][i]
					count += 1
				elif (self.map.cells[j][i] == checkVal):
					count += 1
				else:
					checkVal = self.map.cells[j][i]
					count = 1
				if count >= WIN_TARGET:
					return (j, i)
		return (-1, -1)

	def checkDiag(self):	#return index
		tmp_map = np.array(self.map.cells)
		# l->r
		for i in range(0, self.map.h):	# lower triangle
			tmp = i
			checkVal = -1
			count = 0
			for j in range(0, self.map.w):
				if (tmp >= self.map.h):
					break
				if (count == 0 and checkVal == -1):
					checkVal = tmp_map[tmp][j]
					count += 1
				elif (tmp_map[tmp][j] == checkVal):
					count += 1
				else:
					checkVal = tmp_map[tmp][j]
					count = 1
				if count >= WIN_TARGET:
					return (tmp, j)	
				tmp += 1

		for i in range(1, self.map.w): # upper triangle
			tmp = i
			checkVal = -1
			count = 0
			for j in range(0, self.map.h):
				if (tmp >= self.map.w):
					break
				if (count == 0 and checkVal == -1):
					checkVal = tmp_map[j][tmp]
					count += 1
				elif (tmp_map[j][tmp] == checkVal):
					count += 1
				else:
					checkVal = tmp_map[j][tmp]
					count = 1
				if count >= WIN_TARGET:
					return (j, tmp)
				tmp += 1
		
		# r->l
		tmp_map = np.fliplr(tmp_map)
		for i in range(0, self.map.h):	# lower triangle
			tmp = i
			checkVal = -1
			count = 0
			for j in range(0, self.map.w):
				if (tmp >= self.map.h):
					break
				if (count == 0 and checkVal == -1):
					checkVal = tmp_map[tmp][j]
					count += 1
				elif (tmp_map[tmp][j] == checkVal):
					count += 1
				else:
					checkVal = tmp_map[tmp][j]
					count = 1
				if count >= WIN_TARGET:
					return (tmp, j)	
				tmp += 1

		for i in range(1, self.map.w): # upper triangle
			tmp = i
			checkVal = -1
			count = 0
			for j in range(0, self.map.h):
				if (tmp >= self.map.w):
					break
				if (count == 0 and checkVal == -1):
					checkVal = tmp_map[j][tmp]
					count += 1
				elif (tmp_map[j][tmp] == checkVal):
					count += 1
				else:
					checkVal = tmp_map[j][tmp]
					count = 1
				if count >= WIN_TARGET:
					return (j, tmp)
				tmp += 1
  
		return (-1, -1)

	def checkWinner(self):
		indices = self.checkRow()
		if (indices != (-1, -1)):
			return self.map.cells[indices[0]][indices[1]]
		indices = self.checkCol()
		if (indices != (-1, -1)):
			return self.map.cells[indices[0]][indices[1]]
		indices = self.checkDiag()
		if (indices != (-1, -1)):
			return self.map.cells[indices[0]][indices[1]]
		return 0
	
	def isBoardFinished(self):
		for i in range(self.map.h):
			for j in range(self.map.w):
				if self.map.cells[i][j] == 0:
					return False
		return True
	
	def minimax(self, depth, isMax):
		# Base cases
		winner = self.checkWinner()
		if (winner == self.player_order + 1):
			score = 100 - depth
			return score
		elif (winner == 1 - self.player_order + 1):
			score = -100 + depth
			return score
		if (self.isBoardFinished()):
			return 0
		
		# Max: agent
		if (isMax == True):
			bestScore = -1000
			for i in range(self.map.h):
				for j in range(self.map.w):
					if self.map.cells[i][j] == 0:
						self.map.cells[i][j] = self.player_order + 1
						bestScore = max(bestScore, self.minimax(depth+1, not isMax))
						self.map.cells[i][j] = 0
			return bestScore
		
		# Min: opponent
		elif (isMax == False):
			bestScore = 1000
			for i in range(self.map.h):
				for j in range(self.map.w):
					if self.map.cells[i][j] == 0:
						self.map.cells[i][j] = (1 - self.player_order) + 1
						bestScore = min(bestScore, self.minimax(depth+1, not isMax))
						self.map.cells[i][j] = 0
			return bestScore

	def findBestMove(self):
		# Find Max
		bestScore = -1000
		bestMove = (-1, -1)
		for i in range(self.map.h):
			for j in range(self.map.w):
				if (self.map.cells[i][j] == 0):
					self.map.cells[i][j] = self.player_order + 1
					# check Min to fin largest min
					moveScore = self.minimax(0, False)
					# print("MOVE SCORE:", moveScore)
					# print(f'MOVE: ({i},{j})')
					self.map.cells[i][j] = 0
					if (moveScore > bestScore):
						bestMove = (i, j)
						bestScore = moveScore
					# print("BEST SCORE:", bestScore)
		return bestMove
	
	def choose_cell(self):
		# print("IN")
		print("AI chose:")
		return self.findBestMove()

class Human(Agent):
	def __init__(self):
		pass

	def choose_cell(self):
		x = int(input('Cell x-axis: '))    
		y = int(input('Cell y-axis: '))
		return (x,y)