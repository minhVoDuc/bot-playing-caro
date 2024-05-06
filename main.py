from modules.game import Game

new_game = Game()
new_game.map.show() 

p = 0
# for i in range(1):
while True:
  new_game.play(p)
  new_game.map.show()
  if new_game.check_win(p):
    print(f'Winner is player {p}!')
    break
  p = 1 - p