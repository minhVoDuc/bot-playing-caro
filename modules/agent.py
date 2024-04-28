import numpy as np
import math

WIN_TARGET = 5

# f = open("res2.txt", "a")

class Agent:
	def __init__(self, map, order):
		self.map = map
		self.player_order = order

	def choose_cell(self, lastMove):
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
				if (count == 0 and checkVal == -1 and self.map.cells[i][j] != 0):
					checkVal = self.map.cells[i][j]
					count += 1
				elif (self.map.cells[i][j] == checkVal):
					count += 1
				else:
					if self.map.cells[i][j] != 0:
						checkVal = self.map.cells[i][j]
						count = 1
					else:
						checkVal = -1
						count = 0
				# if (count > self.bestPossible[1]):
				# 	self.bestPossible = (self.map.cells[i][j], count)	
				if count >= WIN_TARGET:
					# self.bestPossible = (self.map.cells[i][j], count)
					# f.write("WIN ROW!\n")
					return self.map.cells[i][j]
					# return (i, j)
		# f.write("NOT WIN ROW!\n")
		return 0
		# return (-1, -1)

	def checkCol(self): 	#return index
		for i in range(self.map.w):
			checkVal = -1
			count = 0
			for j in range(self.map.h):
				if (count == 0 and checkVal == -1 and self.map.cells[j][i] != 0):
					checkVal = self.map.cells[j][i]
					count += 1
				elif (self.map.cells[j][i] == checkVal):
					count += 1
				else:
					if self.map.cells[j][i] != 0:
						checkVal = self.map.cells[j][i]
						count = 1
					else:
						checkVal = -1
						count = 0
				# if (count > self.bestPossible[1]):
				# 	self.bestPossible = (self.map.cells[j][i], count)
				if count >= WIN_TARGET:
					# f.write("WIN COL!\n")
					# self.bestPossible = (self.map.cells[j][i], count)
					return self.map.cells[j][i]
					# return (j, i)
		# f.write("NOT WIN COL!\n")
		return 0
		# return (-1, -1)

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
				if (count == 0 and checkVal == -1 and tmp_map[tmp][j] != 0):
					checkVal = tmp_map[tmp][j]
					count += 1
				elif (tmp_map[tmp][j] == checkVal):
					count += 1
				else:
					if tmp_map[tmp][j] != 0:
						checkVal = tmp_map[tmp][j]
						count = 1
					else:
						checkVal = -1
						count = 0
				# if (count > self.bestPossible[1]):
				# 	self.bestPossible = (tmp_map[tmp][j], count)
				if count >= WIN_TARGET:
					# self.bestPossible = (tmp_map[tmp][j], count)
					# f.write("WIN DIAG LOWER!\n")
					return tmp_map[tmp][j]
					# return (tmp, j)	
				tmp += 1
		# f.write("NOT WIN DIAG LOWER!\n")

		for i in range(1, self.map.w): # upper triangle
			tmp = i
			checkVal = -1
			count = 0
			for j in range(0, self.map.h):
				if (tmp >= self.map.w):
					break
				if (count == 0 and checkVal == -1 and tmp_map[j][tmp] != 0):
					checkVal = tmp_map[j][tmp]
					count += 1
				elif (tmp_map[j][tmp] == checkVal):
					count += 1
				else:
					if tmp_map[j][tmp] != 0:
						checkVal = tmp_map[j][tmp]
						count = 1
					else:
						checkVal = -1
						count =0
				# if (count > self.bestPossible[1]):
				# 	self.bestPossible = (tmp_map[j][tmp], count)
				if count >= WIN_TARGET:
					# self.bestPossible = (tmp_map[j][tmp], count)
					# f.write("WIN DIAG UPPER!\n")
					return tmp_map[j][tmp]
					# return (j, tmp)
				tmp += 1
		# f.write("NOT WIN DIAG UPPER!\n")

		# r->l
		tmp_map = np.fliplr(tmp_map)
		for i in range(0, self.map.h):	# lower triangle
			tmp = i
			checkVal = -1
			count = 0
			for j in range(0, self.map.w):
				if (tmp >= self.map.h):
					break
				if (count == 0 and checkVal == -1 and tmp_map[tmp][j] != 0):
					checkVal = tmp_map[tmp][j]
					count += 1
				elif (tmp_map[tmp][j] == checkVal):
					count += 1
				else:
					if tmp_map[tmp][j] != 0:
						checkVal = tmp_map[tmp][j]
						count = 1
					else:
						checkVal = -1
						count = 0
				# if (count > self.bestPossible[1]):
				# 	self.bestPossible = (tmp_map[tmp][j], count)
				if count >= WIN_TARGET:
					# self.bestPossible = (tmp_map[tmp][j], count)
					# f.write("WIN DIAG FLIPPED LOWER!\n")
					return tmp_map[tmp][j]
					# return (tmp, j)	
				tmp += 1
		# f.write("NOT WIN DIAG FLIPPED LOWER!\n")

		for i in range(1, self.map.w): # upper triangle
			tmp = i
			checkVal = -1
			count = 0
			for j in range(0, self.map.h):
				if (tmp >= self.map.w):
					break
				if (count == 0 and checkVal == -1 and tmp_map[j][tmp] != 0):
					checkVal = tmp_map[j][tmp]
					count += 1
				elif (tmp_map[j][tmp] == checkVal):
					count += 1
				else:
					if tmp_map[j][tmp] != 0:
						checkVal = tmp_map[j][tmp]
						count = 1
					else:
						checkVal = -1
						count =0
				# if (count > self.bestPossible[1]):
				# 	self.bestPossible = (tmp_map[j][tmp], count)
				if count >= WIN_TARGET:
					# self.bestPossible = (tmp_map[j][tmp], count)
					# f.write("WIN DIAG FLIPPED UPPER!\n")
					return tmp_map[j][tmp]
					# return (j, tmp)
				tmp += 1
		# f.write("NOT WIN DIAG FLIPPED UPPER!\n")
		# f.write("NOT WIN DIAG!\n")
		return 0
		# return (-1, -1)

	def checkWinner(self):
		for check in [self.checkRow, self.checkCol, self.checkDiag]:
			# indices = check()
			# if indices != (-1, -1):
			# 	return self.map.cells[indices[0]][indices[1]]
			val = check()
			if val != 0:
				return val
		return 0
 
	def isBoardFinished(self):
		return not np.any(np.array(self.map.cells) == 0)
	
	def evaluateBoard(self):
		player_potential_wins = 0
		opponent_potential_wins = 0
		tmp_map = np.array(self.map.cells)

		# Check rows and columns
		for i in range(self.map.h):
			for j in range(self.map.w - WIN_TARGET + 1):
				row = tmp_map[i, j:j+WIN_TARGET]
				col = tmp_map[j:j+WIN_TARGET, i]
				if 0 in row:
					if self.player_order + 1 in row and 1 - self.player_order + 1 not in row:
						unique, countVal = np.unique(row, return_counts=True)
						counts = dict(zip(unique, countVal))
						if counts[self.player_order + 1] >= WIN_TARGET // 2:
							player_potential_wins += 1
					elif 1 - self.player_order + 1 in row and self.player_order + 1 not in row:
						unique, countVal = np.unique(row, return_counts=True)
						counts = dict(zip(unique, countVal))
						if counts[1 - self.player_order + 1] >= WIN_TARGET // 2:
							opponent_potential_wins += 1
				if 0 in col:
					if self.player_order + 1 in col and 1 - self.player_order + 1 not in col:
						unique, countVal = np.unique(col, return_counts=True)
						counts = dict(zip(unique, countVal))
						if counts[self.player_order + 1] >= WIN_TARGET // 2:
							player_potential_wins += 1
					elif 1 - self.player_order + 1 in col and self.player_order + 1 not in col:
						unique, countVal = np.unique(col, return_counts=True)
						counts = dict(zip(unique, countVal))
						if counts[1 - self.player_order + 1] >= WIN_TARGET // 2:
							opponent_potential_wins += 1

		# Check diagonals
		for i in range(self.map.h - WIN_TARGET + 1):
			for j in range(self.map.w - WIN_TARGET + 1):
				diag1 = [tmp_map[i+k, j+k] for k in range(WIN_TARGET)]
				diag2 = [tmp_map[i+k, j+WIN_TARGET-1-k] for k in range(WIN_TARGET)]
				for diag in [diag1, diag2]:
					if 0 in diag:
						if self.player_order + 1 in diag and 1 - self.player_order + 1 not in diag:
							unique, countVal = np.unique(diag, return_counts=True)
							counts = dict(zip(unique, countVal))
							if counts[self.player_order + 1] >= WIN_TARGET // 2:
								player_potential_wins += 1
						elif 1 - self.player_order + 1 in diag and self.player_order + 1 not in diag:
							unique, countVal = np.unique(diag, return_counts=True)
							counts = dict(zip(unique, countVal))
							if counts[1 - self.player_order + 1] >= WIN_TARGET // 2:
								opponent_potential_wins += 1

		# The score is the difference between the potential wins
		score = player_potential_wins - opponent_potential_wins
		return score

 
	def minimax(self, depth, alpha, beta, isMax, lastMove, maxDepth):
		state = tuple(map(tuple, self.map.cells))
		if (state, depth, isMax) in self.memo:
			return self.memo[(state, depth, isMax)]

		winner = self.checkWinner()
		if winner == self.player_order + 1:
			# self.show()
			# f.write(f"WINNER VALUE VS PLAYER ORDER: {winner}, {self.player_order}\n")
			# f.write("PLAYER WON\n")
			return 100 - depth
		elif winner == 1 - self.player_order + 1:
			# f.write(f"WINNER VALUE VS PLAYER ORDER: {winner}, {self.player_order}\n")
			# f.write("OPPONENT WON\n")
			return -100 + depth
		elif depth == maxDepth:
			return self.evaluateBoard()
			# return 0
			# if self.bestPossible[0] == self.player_order + 1:
			# 	return 100 - (100 // self.bestPossible[1])
			# elif self.bestPossible[0] == 1 - self.player_order + 1:
			# 	return -100 + (100 // self.bestPossible[1])
		elif self.isBoardFinished():
			return 0

		bestScore = -math.inf if isMax else math.inf
		# empty_cells = np.where(np.array(self.map.cells) == 0)
		# for i, j in zip(*empty_cells):
		# Calculate the boundaries of the window
		start_i = max(0, lastMove[0] - 1)
		end_i = min(self.map.h, lastMove[0] + 2)
		start_j = max(0, lastMove[1] - 1)
		end_j = min(self.map.w, lastMove[1] + 2)

		for i in range(start_i, end_i):
			for j in range(start_j, end_j):
				if self.map.cells[i][j] == 0:
					self.map.cells[i][j] = self.player_order + 1 if isMax else 1 - self.player_order + 1
					# f.write(f"ITERATE MINIMAX: {(i,j)}, {isMax}\n")
					self.show()
					score = self.minimax(depth + 1, alpha, beta, not isMax, (i,j), maxDepth)
					self.map.cells[i][j] = 0

					if isMax:
						# f.write(f"CURRENT SCORE MAX VS CANDIDATE: {(i,j)}, {bestScore}, {score}\n")
						bestScore = max(score, bestScore)
						# f.write(f"BEST SCORE MINIMAX AFTER: {(i,j)}, {isMax}, {bestScore}\n")
						alpha = max(alpha, score)
					else:
						# f.write(f"CURRENT SCORE MIN VS CANDIDATE: {(i,j)}, {bestScore}, {score}\n")
						bestScore = min(score, bestScore)
						# f.write(f"BEST SCORE MINIMAX AFTER: {(i,j)}, {isMax}, {bestScore}\n")
						beta = min(beta, score)

					if beta <= alpha:
						break
		self.memo[(state, depth, isMax)] = bestScore
		return bestScore

	def show(self):
		for line in self.map.cells:
			p_line = ""
			for cell in line:
				p_line = p_line + str(cell) + ' '
			# f.write(f"{p_line}\n")
		# f.write("\n")

	def findBestMove(self, lastMove):
		bestScore = -math.inf
		bestMove = (-1, -1)

		# Calculate the boundaries of the window
		start_i = max(0, lastMove[0] - 1)
		end_i = min(self.map.h, lastMove[0] + 2)
		start_j = max(0, lastMove[1] - 1)
		end_j = min(self.map.w, lastMove[1] + 2)

		for i in range(start_i, end_i):
			for j in range(start_j, end_j):
				if self.map.cells[i][j] == 0:
					self.map.cells[i][j] = self.player_order + 1
					# f.write(f"SEARCH NEW STATE: {(i, j)}\n")
					self.show()
					moveScore = self.minimax(0, -math.inf, math.inf, False, (i,j), maxDepth = 4)
					self.map.cells[i][j] = 0
					# f.write(f"MOVE SCORE AFTER MINIMAX VS BEST SCORE: {(i,j)}, {moveScore}, {bestScore}\n")
					if moveScore > bestScore:
						bestMove = (i, j)
						bestScore = moveScore
		# f.close()
		return bestMove

	def choose_cell(self, lastMove):
		print("AI chose:")
		return self.findBestMove(lastMove)

class Human(Agent):
	def __init__(self):
		pass

	def choose_cell(self, lastMove):
		x = int(input('Cell x-axis: '))    
		y = int(input('Cell y-axis: '))
		return (x,y)