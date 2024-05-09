#from modules.game import Game

#new_game = Game()
#new_game.map.show() 

#p = 0
# for i in range(1):
#while True:
# new_game.play(p)
#  new_game.map.show()
#  if new_game.check_win(p):
#    print(f'Winner is player {p}!')
#    break
#  p = 1 - p

import tkinter as tk
from modules.game import Game

class CaroGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Caro Game")
        self.game = Game()
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for i in range(self.game.map.h):
            row = []
            for j in range(self.game.map.w):
                btn = tk.Button(self.master, text=" ", font=('Helvetica', 24), width=2, height=1,
                                command=lambda x=i, y=j: self.button_click(x, y))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def button_click(self, x, y):
     if not self.game.map.is_empty(x, y):
        return
     self.game.play(x, y)
     self.update_board()

     if self.game.check_win():
        winner = "Player 1" if self.game.current_player == 0 else "Player 2"
        tk.messagebox.showinfo("Game Over", f"{winner} wins!")
        self.master.quit()


    def update_board(self):
        for i in range(self.game.map.h):
            for j in range(self.game.map.w):
                cell_value = self.game.map.get(i, j)
                if cell_value == 1:
                    self.buttons[i][j].config(text="X", state="disabled")
                elif cell_value == 2:
                    self.buttons[i][j].config(text="O", state="disabled")

def main():
    root = tk.Tk()
    app = CaroGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
