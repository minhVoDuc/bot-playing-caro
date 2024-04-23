from modules.map import Map
import modules.agent as player

def standardize(s):
  if s<20:
    s = 20
  if s>100:
    s = 100
  return s

def select_player_type():
  type = 'undef'
  while type == 'undef':
    type = input('Choose player type ([H]uman/[R]andom/[S]mart): ')
    if type == 'H' or type == 'h' or type == 'human':
      p = player.Human()
    elif type == 'R' or type == 'r' or type == 'random':
      p = player.RandomAgent()
    elif type == 'S' or type == 's' or type == 'smart':
      p = player.SmartAgent()
    else:
      type = 'undef'
      print('Insert error! Retry!')
  return p

class Game:
  def __init__(self):
    # create map
    h = standardize(int(input('Insert map height (20-100): ')))
    w = standardize(int(input('Insert map width (20-100): ')))
    self.map = Map(h, w)
    # select player type [Human, Random or Smart]
    self.p = []
    for _ in range(2):
      p = select_player_type()
      self.p.append(p)

    # init winner - default 0: no winner
    self.winner = 0
  
  def verify(self, x, y):
    # self.map.is_empty
    pass

  def play(self, i):
    (x,y) = self.p[i].choose_cell()
    self.map.play(i+1, x, y)

  def check(self, p):
    pass 