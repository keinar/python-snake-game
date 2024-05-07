import random

class Food:
    def __init__(self, game_width, game_height, space_size, canvas, food_color):
        x = random.randint(0, (game_width//space_size) - 1) * space_size
        y = random.randint(0, (game_height//space_size) - 1) * space_size

        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + space_size, y + space_size, fill=food_color, tag='food')
