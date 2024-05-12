from modules.map import Map
import modules.agent as player

def standardize(s):
  if s<9:
    s = 9
  if s>30:
    s = 30
  return s

def select_player_type(map, order):
  type = 'undef'
  while type == 'undef':
    type = input('Choose player type ([H]uman/[R]andom/[S]mart): ')
    if type == 'H' or type == 'h' or type == 'human':
      p = player.Human(map, order)
    elif type == 'R' or type == 'r' or type == 'random':
      p = player.RandomAgent(map, order)
    elif type == 'S' or type == 's' or type == 'smart':
      p = player.SmartAgent(map, order)
    else:
      type = 'undef'
      print('Insert error! Retry!')
  return p

def check_avai(x,y,h,w):
  return x >= 0 and y >=0 and x < h and y < w

class Game:
  def __init__(self):
    # create map
    h = standardize(int(input('Insert map height (9-30): ')))
    w = standardize(int(input('Insert map width (9-30): ')))
    self.map = Map(h, w)
    self.lastMove = [(-1, -1), (-1, -1)]
    # select player type [Human, Random or Smart]
    self.p = []
    for i in range(2):
      p = select_player_type(self.map, i)
      self.p.append(p)

    # init winner - default 0: no winner
    self.winner = 0
  
  def verify(self, x, y):
    # self.map.is_empty
    pass

  def play(self, i):
    (x,y) = self.p[i].choose_cell(self.lastMove[1-i])
    self.lastMove[i] = (x,y)
    self.map.play(i+1, x, y)

  def check_win(self, p):
    (x,y) = self.lastMove[p]
    h, w = self.map.get_size()
    scores, hi_scores, x_, y_ = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
    move_type = [-1, 1, 0, 1, 1]
    # print(f'Checking player {p} at ({x}, {y})')
    for i in range (-4,5):
      for j in range(4):
        x_[j], y_[j] = x+move_type[j]*i, y+move_type[j+1]*i
        # print(f'[type {j}] - pos ({x_[j]}, {y_[j]})')

        if check_avai(x_[j], y_[j], h, w):
          if self.map.get(x_[j],y_[j])-1 == p:
            scores[j] += 1
            if i == 4:
              if scores[j] > hi_scores[j]:
                hi_scores[j] = scores[j]
          else:
            if scores[j] > hi_scores[j]:
              hi_scores[j] = scores[j]
            scores[j] = 0
        else:
          if scores[j] > hi_scores[j]:
            hi_scores[j] = scores[j]
          scores[j] = 0

    # print('score', score)
    # print('hi-score', hi_score)
    for score in hi_scores:
      if score > 4: 
        return True
      
    return False