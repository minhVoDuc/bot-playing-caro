from tkinter import Button, Frame, Label, StringVar, messagebox, simpledialog
import threading
import time
from modules.map import Map
import modules.agent as player
import tkinter as tk
def standardize(s):
  if s<9:
    s = 9
  if s>30:
    s = 30
  return s
def get_player_type_input():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    while True:
      type = tk.simpledialog.askstring("Player Type", "Enter player type (H/human, R/random, S/smart):")
      if type:
       return type.lower()
def select_player_type(map, order):
  #root = tk.Tk()
  #root.withdraw()  # Hide the root window
  type = 'undef'
  while type == 'undef':
    type = get_player_type_input()
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

class CaroUI:
  def get_board_dimensions(self):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    while True:
        h = simpledialog.askinteger("Board Dimensions", "Enter board height:")
        w = simpledialog.askinteger("Board Dimensions", "Enter board width:")
        if h is not None and w is not None and h > 0 and w > 0:
           return h, w
        else:
           messagebox.showerror("Error", "Invalid dimensions! Please enter positive integers.")
  def __init__(self, root):
    self.root = root
    self.root.title("Caro Game")
    # create map
    h,w= self.get_board_dimensions()
    self.map = Map(h, w)
    self.lastMove = [(-1, -1), (-1, -1)]
    # select player type [Human, Random or Smart]
    self.p = []
    self.p_index = 0
    for i in range(2):
      p = select_player_type(self.map, i)
      self.p.append(p)

    # init winner - default 0: no winner
    self.winner = 0

    self.buttons = [[None for _ in range(self.map.w)] for _ in range(self.map.h)]
    self.setup_ui()
  
  def setup_ui(self):
    self.main_frame = Frame(self.root)
    self.main_frame.pack()

    for i in range(self.map.h):
      for j in range(self.map.w):
        self.buttons[i][j] = Button(self.main_frame, text="", width=4, height=2, command=lambda i=i, j=j: self.handle_click(i, j))
        self.buttons[i][j].grid(row=i, column=j)

    self.play_button = Button(self.root, text="Play", command=self.play_game)
    self.play_button.pack()

    self.result_label = Label(self.root, text="")
    self.result_label.pack()

  def update_board(self):
    for i in range(self.map.h):
      for j in range(self.map.w):
        if self.map.cells[i][j] == 1:
          self.buttons[i][j].config(text="X", state="disabled")
        elif self.map.cells[i][j] == 2:
          self.buttons[i][j].config(text="O", state="disabled")

 # def handle_click(self, i, j):
  
  #      pass  # Do nothing if the player is not human

  def play_game(self):
    self.play_button.config(state="disabled")
    self.result_label.config(text="")
    self.map.reset()

    def game_loop():
      while True:  
        if self.check_win():
          self.result_label.config(text=f"Player {self.p_index+1} wins!")
          break
        if type(self.p[self.p_index]) != player.Human:
          self.play()
          self.update_board()
          self.root.update_idletasks()
          time.sleep(0.5)  # Add a slight delay for better visualization
          
          if self.check_win():
            self.result_label.config(text=f"Player {self.p_index+1} wins!")
            break

          self.p_index = 1 - self.p_index

      self.play_button.config(state="normal")

    threading.Thread(target=game_loop).start()

  def handle_click(self, row, col):
    # This method gets called when a button in the UI grid is clicked
    x, y = row, col  # Assuming row and col represent the coordinates of the clicked cell
    self.lastMove[self.p_index] = (x,y)
    self.map.play(self.p_index+1, x, y)

    self.p_index = 1 - self.p_index


  def play(self):
    if type(self.p[self.p_index]) != player.Human:
      (x,y) = self.p[self.p_index].choose_cell(self.lastMove[1-self.p_index])
      self.lastMove[self.p_index] = (x,y)
      self.map.play(self.p_index+1, x, y)

  def check_win(self):
    (x,y) = self.lastMove[self.p_index]
    h, w = self.map.get_size()
    scores, hi_scores, x_, y_ = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
    move_type = [-1, 1, 0, 1, 1]
    # print(f'Checking player {p} at ({x}, {y})')
    for i in range (-4,5):
      for j in range(4):
        x_[j], y_[j] = x+move_type[j]*i, y+move_type[j+1]*i
        # print(f'[type {j}] - pos ({x_[j]}, {y_[j]})')

        if check_avai(x_[j], y_[j], h, w):
          if self.map.get(x_[j],y_[j])-1 == self.p_index:
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