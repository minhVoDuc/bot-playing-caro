from modules.map import Map
import modules.agent as player

class Game:
  def __init__(self, h, w):
    self.map = Map(h, w)
    self.p1 = player.Agent()
    self.p2 = player.Agent()
    self.winner = 0
  
  def verify(self, x, y):
    # self.map.is_empty
    pass

  def play(self, p, x, y):
    self.map.play(p, x, y)

  def check(self, p):
    pass 