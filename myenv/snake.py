from tkinter import Canvas

class Snake:
    def __init__(self, body_parts, canvas, space_size, snake_color):
        self.body_size = body_parts
        self.coordinates = []
        self.squares = []

        # Start the snake in the middle of the canvas
        start_x = canvas.winfo_width() // 2
        # Ensure the snake starts away from the top edge of the canvas
        # Increase the y-coordinate to place the snake further down the canvas
        start_y = (canvas.winfo_height() // 2) + (3 * space_size)

        for i in range(0, body_parts):
            self.coordinates.append([start_x, start_y + i * space_size])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color, tag='snake')
            self.squares.append(square)
