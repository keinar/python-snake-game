from game import Game
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the snake game in manual or AI mode.')
    parser.add_argument('--mode', type=str, default='manual', choices=['manual', 'ai'],
                        help='Start the game in manual or AI mode. Default is manual.')
    args = parser.parse_args()

    game_instance = Game(mode=args.mode)
    game_instance.window.mainloop()
