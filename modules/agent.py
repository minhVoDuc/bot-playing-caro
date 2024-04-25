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
	def __init__(self, map, order):
		Agent.__init__(self, map, order)
		self.memo = {}
		self.bestPossible = (0, 0)

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
				if (count > self.bestPossible[1]):
					self.bestPossible = (self.map.cells[i][j], count)	
				if count >= WIN_TARGET:
					self.bestPossible = (self.map.cells[i][j], count)	
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
				if (count > self.bestPossible[1]):
					self.bestPossible = (self.map.cells[j][i], count)
				if count >= WIN_TARGET:
					self.bestPossible = (self.map.cells[j][i], count)
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
				if (count > self.bestPossible[1]):
					self.bestPossible = (tmp_map[tmp][j], count)
				if count >= WIN_TARGET:
					self.bestPossible = (tmp_map[tmp][j], count)
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
				if (count > self.bestPossible[1]):
					self.bestPossible = (tmp_map[j][tmp], count)
				if count >= WIN_TARGET:
					self.bestPossible = (tmp_map[j][tmp], count)
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
				if (count > self.bestPossible[1]):
					self.bestPossible = (tmp_map[tmp][j], count)
				if count >= WIN_TARGET:
					self.bestPossible = (tmp_map[tmp][j], count)
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
				if (count > self.bestPossible[1]):
					self.bestPossible = (tmp_map[j][tmp], count)
				if count >= WIN_TARGET:
					self.bestPossible = (tmp_map[j][tmp], count)
					return (j, tmp)
				tmp += 1
  
		return (-1, -1)

	def checkWinner(self):
		for check in [self.checkRow, self.checkCol, self.checkDiag]:
			indices = check()
			if indices != (-1, -1):
				return self.map.cells[indices[0]][indices[1]]
		return 0
 
	def isBoardFinished(self):
		return not np.any(np.array(self.map.cells) == 0)
 
	def minimax(self, depth, alpha, beta, isMax, maxDepth):
		state = tuple(map(tuple, self.map.cells))
		if (state, depth, isMax) in self.memo:
			return self.memo[(state, depth, isMax)]

		winner = self.checkWinner()
		if winner == self.player_order + 1:
			return 100 - depth
		elif winner == 1 - self.player_order + 1:
			return -100 + depth
		elif depth == maxDepth:
			if self.bestPossible[0] == self.player_order + 1:
				return 100 - (100 // self.bestPossible[1])
			elif self.bestPossible[0] == 1 - self.player_order + 1:
				return -100 + (100 // self.bestPossible[1])
		elif self.isBoardFinished():
			return 0

		bestScore = -1000 if isMax else 1000
		empty_cells = np.where(np.array(self.map.cells) == 0)
		for i, j in zip(*empty_cells):
			self.map.cells[i][j] = self.player_order + 1 if isMax else 1 - self.player_order + 1
			score = self.minimax(depth + 1, alpha, beta, not isMax, maxDepth)
			self.map.cells[i][j] = 0

			if isMax:
				bestScore = max(score, bestScore)
				alpha = max(alpha, score)
			else:
				bestScore = min(score, bestScore)
				beta = min(beta, score)

			if beta <= alpha:
				break
		self.memo[(state, depth, isMax)] = bestScore
		return bestScore

	def findBestMove(self):
		bestScore = -1000
		bestMove = (-1, -1)
		empty_cells = np.where(np.array(self.map.cells) == 0)
		for i, j in zip(*empty_cells):
			self.map.cells[i][j] = self.player_order + 1
			moveScore = self.minimax(0, -1000, 1000, False, maxDepth = 3)
			self.map.cells[i][j] = 0
			if moveScore > bestScore:
				bestMove = (i, j)
				bestScore = moveScore
		return bestMove

	def choose_cell(self):
		print("AI chose:")
		return self.findBestMove()

class Human(Agent):
	def __init__(self):
		pass

	def choose_cell(self):
		x = int(input('Cell x-axis: '))    
		y = int(input('Cell y-axis: '))
		return (x,y)