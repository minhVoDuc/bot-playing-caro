class Map:
	def __init__(self, h=20, w=20):
		self.h = h
		self.w = w
		# self.cells = [[1,2,2,2,0,0,0,0,0],[0, 1, 0, 0, 0, 0 ,0, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]]
		self.cells = [[0 for _ in range(w)] for _ in range(h)]

	def get(self):
		return self.cells
	
	def get(self, x, y):
		return self.cells[x][y]
	
	def get_size(self):
		return self.h, self.w
	
	def is_empty(self, x, y):
		return self.cells[x][y] == 0
	
	def play(self, p, x, y):
		self.cells[x][y] = p

	def show(self):
		for line in self.cells:
			p_line = ""
			for cell in line:
				p_line = p_line + str(cell) + ' '
			print(p_line)
		print()

	def reset(self):
		for i in range(self.h):
			for j in range(self.w):
				self.cells[i][j] = 0