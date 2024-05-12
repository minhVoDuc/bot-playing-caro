<<<<<<< Updated upstream
from modules.game import Game

new_game = Game()
new_game.map.show() 

p = 0
# for i in range(1):
while True:
  new_game.play(p)
  new_game.map.show()
  if new_game.check_win(p):
    print(f'Winner is player {p} after play at {new_game.lastMove[p]}!')
    break
  p = 1 - p
=======
'''
import tkinter as tk
from modules.game import Game

class CaroUI:
    def __init__(self, master):
        self.master = master
        self.game = None
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        tk.Label(self.frame, text="Map Height (9-30):").grid(row=0, column=0)
        self.height_entry = tk.Entry(self.frame)
        self.height_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Map Width (9-30):").grid(row=1, column=0)
        self.width_entry = tk.Entry(self.frame)
        self.width_entry.grid(row=1, column=1)

        self.start_button = tk.Button(self.frame, text="Start Game", command=self.start_game)
        self.start_button.grid(row=2, columnspan=2)

    def start_game(self):
        height = int(self.height_entry.get())
        width = int(self.width_entry.get())
        self.game = Game(height, width)
        self.frame.destroy()
        self.create_game_ui()

    def create_game_ui(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.buttons = []
        for i in range(self.game.map.h):
            row_buttons = []
            for j in range(self.game.map.w):
                button = tk.Button(self.frame, text="", width=2, height=1,
                                   command=lambda i=i, j=j: self.play_move(i, j))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def play_move(self, i, j):
        if self.game is not None and self.game.map.is_empty(i, j):
            self.game.play(0, i, j)  # Assuming the human player is always player 0
            self.update_ui()

            if self.game.check_win(0):
                tk.messagebox.showinfo("Game Over", "You win!")
                self.reset_game()

            # Here you can add logic to let the AI make a move and check if it wins

    def update_ui(self):
        for i in range(self.game.map.h):
            for j in range(self.game.map.w):
                value = self.game.map.cells[i][j]
                if value == 1:
                    self.buttons[i][j].config(text="O", state=tk.DISABLED)
                elif value == 2:
                    self.buttons[i][j].config(text="X", state=tk.DISABLED)

    def reset_game(self):
        self.frame.destroy()
        self.create_widgets()

def main():
    root = tk.Tk()
    root.title("Caro Game")
    app = CaroUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
'''
from tkinter import Tk, Button, Frame, Label, StringVar
from modules.game import Game
import threading
import time

class CaroUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Caro Game")
        
        self.game = Game()
        
        self.buttons = [[None for _ in range(self.game.map.w)] for _ in range(self.game.map.h)]
        
        self.setup_ui()
    
    def setup_ui(self):
        self.main_frame = Frame(self.root)
        self.main_frame.pack()

        for i in range(self.game.map.h):
            for j in range(self.game.map.w):
                self.buttons[i][j] = Button(self.main_frame, text="", width=4, height=2, command=lambda i=i, j=j: self.handle_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        self.play_button = Button(self.root, text="Play", command=self.play_game)
        self.play_button.pack()

        self.result_label = Label(self.root, text="")
        self.result_label.pack()

    def update_board(self):
        for i in range(self.game.map.h):
            for j in range(self.game.map.w):
                if self.game.map.cells[i][j] == 1:
                    self.buttons[i][j].config(text="X", state="disabled")
                elif self.game.map.cells[i][j] == 2:
                    self.buttons[i][j].config(text="O", state="disabled")

    def handle_click(self, i, j):
        pass

    def play_game(self):
        self.play_button.config(state="disabled")
        self.result_label.config(text="")

        def game_loop():
            while not self.game.check_win(0) and not self.game.check_win(1):
                self.game.play(0)
                self.update_board()
                self.root.update_idletasks()
                time.sleep(0.5)  # Add a slight delay for better visualization

                if self.game.check_win(0):
                    self.result_label.config(text="Player 1 wins!")
                    break

                self.game.play(1)
                self.update_board()
                self.root.update_idletasks()
                time.sleep(0.5)  # Add a slight delay for better visualization

                if self.game.check_win(1):
                    self.result_label.config(text="Player 2 wins!")
                    break

            self.play_button.config(state="normal")

        threading.Thread(target=game_loop).start()

def main():
    root = Tk()
    app = CaroUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()


>>>>>>> Stashed changes
