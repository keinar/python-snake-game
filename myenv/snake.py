from tkinter import Canvas

class Snake:
    def __init__(self, body_parts, canvas, space_size, snake_color):
        self.body_size = body_parts
        self.coordinates = []
        self.squares = []

        # Start the snake in the middle of the canvas
        start_x = canvas.winfo_width() // 2
        # Ensure the snake starts away from the top edge of the canvas
        # Adjust the y-coordinate to ensure it's well within the canvas bounds and not too close to the edges
        # The snake will be initialized vertically in the middle of the canvas
        # Adjust the starting y-coordinate to be in the middle of the canvas and account for the total length of the snake
        # The snake's head should be positioned away from the top edge to prevent immediate collision
        # Adjust the starting y-coordinate to be lower on the canvas to prevent collision with the wall on y-axis
        # The snake's body parts should be spaced out vertically to prevent self-collision
        start_y = canvas.winfo_height() // 2 - (space_size * (body_parts // 2))

        # Initialize the snake's body parts vertically within the canvas bounds
        for i in range(body_parts):
            body_part_y = start_y + (i * space_size)
            self.coordinates.append([start_x, body_part_y])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color, tag='snake')
            self.squares.append(square)
