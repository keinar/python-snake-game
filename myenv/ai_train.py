import tkinter as tk
from game import Game

def main():
    # Set up the root tkinter window
    root = tk.Tk()
    root.title("Snake AI Trainer")

    # Create an instance of the Game class
    game_instance = Game()

    # Start the AI training process
    game_instance.start_game()

    # Start the tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
