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