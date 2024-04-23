class Agent:
	def choose_cell(self):
		pass

class RandomAgent(Agent):
	pass

class SmartAgent(Agent):
	pass

class Human(Agent):
	def choose_cell(self):
		x = int(input('Cell x-axis: '))    
		y = int(input('Cell y-axis: '))
		return (x,y)