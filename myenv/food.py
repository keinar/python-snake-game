import random
from game import Game

class Food:
    def __init__(self, game):
        x = random.randint(0, (game.game_width//game.space_size) - 1) * game.space_size
        y = random.randint(0, (game.game_height//game.space_size) - 1) * game.space_size

        self.coordinates = [x, y]
        game.canvas.create_oval(x, y, x + game.space_size, y + game.space_size, fill=game.food_color, tag='food')
