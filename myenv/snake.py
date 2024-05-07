
class Snake:
    def __init__(self, game):
        self.body_size = game.body_parts
        self.coordinates = []
        self.squares = []

        for i in range(0, game.body_parts):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = game.canvas.create_rectangle(x, y, x + game.space_size, y + game.space_size, fill=game.snake_color, tag='snake')
            self.squares.append(square)