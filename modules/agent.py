import numpy as np
import math
from random import randint

WIN_TARGET = 5

# f = open("res2.txt", "a")

class Agent:
	def __init__(self, map, order):
		self.map = map
		self.player_order = order

	def choose_cell(self, lastMove):
		pass

class RandomAgent(Agent):
	def __init__(self, map, order):
		Agent.__init__(self, map, order)
	
	def choose_cell(self, lastMove):
		print("Random chose:")
		x, y = randint(0, self.map.h-1), randint(0, self.map.w-1)
		while not self.map.is_empty(x, y):
			x, y = randint(0, self.map.h-1), randint(0, self.map.w-1)			
		return x, y


class SmartAgent(Agent):
	def __init__(self, map, order):
		Agent.__init__(self, map, order)
		# self.memo = {}

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
				if count >= WIN_TARGET:
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
				if count >= WIN_TARGET:
					# f.write("WIN COL!\n")
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
				if count >= WIN_TARGET:
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
				if count >= WIN_TARGET:
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
				if count >= WIN_TARGET:
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
				if count >= WIN_TARGET:
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
			row_flag = 0
			col_flag = 0
			diag_flag = 0
			optimize_flag_2 = 0
			optimize_flag_3 = 0

			for j in range(self.map.w - WIN_TARGET + 1):
				row = tmp_map[i, j:j+WIN_TARGET]
				col = tmp_map[j:j+WIN_TARGET, i]
				# if row_flag == 1:					
					# print(f"    FLAG_CHANGE: {row_flag}")
				if 0 in row:
					if self.player_order + 1 in row and 1 - self.player_order + 1 not in row:
						unique, countVal = np.unique(row, return_counts=True)
						counts = dict(zip(unique, countVal))
						if counts[self.player_order + 1] >= 4: #math.ceil(WIN_TARGET / 2):
							player_potential_wins += 3
						elif counts[self.player_order + 1] == 3 and optimize_flag_3 == 0: #math.ceil(WIN_TARGET / 2):
							player_potential_wins += 2
							optimize_flag_3 = 1
						elif counts[self.player_order + 1] == 2 and optimize_flag_2 == 0: #math.ceil(WIN_TARGET / 2):
							player_potential_wins += 1
							optimize_flag_2 = 1
					if 1 - self.player_order + 1 in row and self.player_order + 1 not in row:
						unique, countVal = np.unique(row, return_counts=True)
						counts = dict(zip(unique, countVal))
						if counts[1 - self.player_order + 1] >= 4 and row_flag == 0: #math.ceil(WIN_TARGET / 2):
							#print(f"Count: {counts[1 - self.player_order + 1]}")
							# print(f"    FLAG: {row_flag}")
							opponent_potential_wins += 4
							# print(f"	EVAL POS: {i, j}, FLAG; {row_flag}, TYPE: +2, POTENTIAL: {opponent_potential_wins}")
				elif 1 - self.player_order + 1 in row and self.player_order + 1 in row:
					unique, countVal = np.unique(row, return_counts=True)
					counts = dict(zip(unique, countVal))
					if counts[self.player_order + 1] >= 4: #math.ceil(WIN_TARGET / 2):
						player_potential_wins += 3
					if counts[1 - self.player_order + 1] >= 4 and row_flag == 0: #math.ceil(WIN_TARGET / 2):
						#print(f"Count: {counts[1 - self.player_order + 1]}")
						# print(f"    FLAG: {row_flag}")
						opponent_potential_wins += 3
						row_flag = 1
						# print(f"	EVAL POS: {i, j}, FLAG; {row_flag}, TYPE: +1, POTENTIAL: {opponent_potential_wins}")
				
							
				if 0 in col:
					if self.player_order + 1 in col and 1 - self.player_order + 1 not in col:
						unique, countVal = np.unique(col, return_counts=True)
						counts = dict(zip(unique, countVal))
						if counts[self.player_order + 1] >= 4: #math.ceil(WIN_TARGET / 2):
							player_potential_wins += 3
						elif counts[self.player_order + 1] == 3 and optimize_flag_3 == 0: #math.ceil(WIN_TARGET / 2):
							player_potential_wins += 2
							optimize_flag_3 = 1
						elif counts[self.player_order + 1] == 2 and optimize_flag_2 == 0: #math.ceil(WIN_TARGET / 2):
							# print(f"	COUNTS: {counts}")
							player_potential_wins += 1
							# print(f"	PLAYER: {player_potential_wins}")
							optimize_flag_2 = 1
					if 1 - self.player_order + 1 in col and self.player_order + 1 not in col:
						unique, countVal = np.unique(col, return_counts=True)
						counts = dict(zip(unique, countVal))
						if counts[1 - self.player_order + 1] >= 4 and col_flag == 0: #math.ceil(WIN_TARGET / 2):
							opponent_potential_wins += 4
				elif 1 - self.player_order + 1 in col and self.player_order + 1 in col:
					unique, countVal = np.unique(col, return_counts=True)
					counts = dict(zip(unique, countVal))
					if counts[self.player_order + 1] >= 4: #math.ceil(WIN_TARGET / 2):
						player_potential_wins += 3
					if counts[1 - self.player_order + 1] >= 4 and col_flag == 0: #math.ceil(WIN_TARGET / 2):
						opponent_potential_wins += 3
						col_flag = 1

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
							if counts[self.player_order + 1] >= 4: #math.ceil(WIN_TARGET / 2):
								player_potential_wins += 3
							elif counts[self.player_order + 1] == 3 and optimize_flag_3 == 0: #math.ceil(WIN_TARGET / 2):
								player_potential_wins += 2
								optimize_flag_3 = 1
							elif counts[self.player_order + 1] == 2 and optimize_flag_2 == 0: #math.ceil(WIN_TARGET / 2):
								player_potential_wins += 1
								optimize_flag_2 = 1
						if 1 - self.player_order + 1 in diag and self.player_order + 1 not in diag:
							unique, countVal = np.unique(diag, return_counts=True)
							counts = dict(zip(unique, countVal))
							if counts[1 - self.player_order + 1] >= 4 and diag_flag == 0: #math.ceil(WIN_TARGET / 2):
								opponent_potential_wins += 4
					elif 1 - self.player_order + 1 in diag and self.player_order + 1 in diag:
						unique, countVal = np.unique(diag, return_counts=True)
						counts = dict(zip(unique, countVal))
						if counts[self.player_order + 1] >= 4: #math.ceil(WIN_TARGET / 2):
							player_potential_wins += 3
						if counts[1 - self.player_order + 1] >= 4 and diag_flag == 0: #math.ceil(WIN_TARGET / 2):
							opponent_potential_wins += 3
							diag_flag = 1

		# The score is the difference between the potential wins
		score = player_potential_wins - opponent_potential_wins
		#print(f"Player: {player_potential_wins}, Opponent: {opponent_potential_wins}")
		return score

 
	def minimax(self, depth, alpha, beta, isMax, lastMove, maxDepth):
		# state = tuple(map(tuple, self.map.cells))
		# if (state, depth, isMax) in self.memo:
		# 	return self.memo[(state, depth, isMax)]

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
		window_size = 5

		# Calculate the boundaries of the window
		# start_i = max(0, lastMove[0] - window_size // 2)
		# end_i = min(self.map.h, start_i + window_size)
		# start_j = max(0, lastMove[1] - window_size // 2)
		# end_j = min(self.map.w, start_j + window_size)

		for i in range(0, self.map.h): #(start_i, end_i):
			for j in range(0, self.map.w): #(start_j, end_j):
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
						# print(f"Best Score: {bestScore}")
						# f.write(f"CURRENT SCORE MIN VS CANDIDATE: {(i,j)}, {bestScore}, {score}\n")
						bestScore = min(score, bestScore)
						# f.write(f"BEST SCORE MINIMAX AFTER: {(i,j)}, {isMax}, {bestScore}\n")
						beta = min(beta, score)

					if beta <= alpha:
						break
		# self.memo[(state, depth, isMax)] = bestScore
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
		window_size = 5

		# Calculate the boundaries of the window
		# start_i = max(0, lastMove[0] - window_size // 2)
		# end_i = min(self.map.h, start_i + window_size)
		# start_j = max(0, lastMove[1] - window_size // 2)
		# end_j = min(self.map.w, start_j + window_size)
  
		# print(f"Start from i = {start_i} to {end_i}")
		# print(f"Start from j = {start_j} to {end_j}")

		for i in range(0, self.map.h): #(start_i, end_i):
			for j in range(0, self.map.w): #(start_j, end_j):
				if self.map.cells[i][j] == 0:
					self.map.cells[i][j] = self.player_order + 1
					# f.write(f"SEARCH NEW STATE: {(i, j)}\n")
					self.show()
					moveScore = self.minimax(0, -math.inf, math.inf, False, (i,j), maxDepth = 1)
					self.map.cells[i][j] = 0
					# f.write(f"MOVE SCORE AFTER MINIMAX VS BEST SCORE: {(i,j)}, {moveScore}, {bestScore}\n")
					print(f"POS = {i, j}, MOVE = {moveScore}, BEST = {bestScore}")
					if moveScore > bestScore:
						bestMove = (i, j)
						bestScore = moveScore
		#f.close()
		return bestMove

	def choose_cell(self, lastMove):
		print("AI chose:")
		if lastMove == (-1, -1):
			return (self.map.h // 2, self.map.w // 2)
		return self.findBestMove(lastMove)

class Human(Agent):
	def __init__(self, map, order):
		Agent.__init__(self, map, order)

	def choose_cell(self, lastMove):
		x = int(input('Cell x-axis: '))    
		y = int(input('Cell y-axis: '))
		while self.map.is_empty(x,y) == False:
			print('Invalid move!')
			x = int(input('Cell x-axis: '))    
			y = int(input('Cell y-axis: '))
		return (x,y)