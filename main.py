from modules.game import Game

new_game = Game()
new_game.map.show() 

p = 0
for i in range(25):
  new_game.play(p)
  new_game.map.show()
  p = 1 - p