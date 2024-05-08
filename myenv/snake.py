from tkinter import Canvas

class Snake:
    def __init__(self, body_parts, canvas, space_size, snake_color, initial_position=None):
        self.body_size = body_parts
        self.coordinates = []
        self.squares = []

        if initial_position:
            start_x, start_y = initial_position
        else:
            # Start the snake in the middle of the canvas
            start_x = canvas.winfo_width() // 2
            # Initialize the snake's body parts vertically within the canvas bounds
            # The snake's body parts will be initialized downwards from the starting position
            # Adjust the start_y position to be lower on the canvas to prevent immediate collision
            start_y = (canvas.winfo_height() // 2) + (space_size * (body_parts - 1))

        for i in range(body_parts):
            body_part_y = start_y + (i * space_size)  # Adjusted to initialize downwards
            # Ensure the body part is within the canvas bounds
            if body_part_y >= canvas.winfo_height():
                # If the body part is below the bottom edge, place it starting from the top
                body_part_y = (i * space_size)
            self.coordinates.append([start_x, body_part_y])
            print(f"Initializing body part {i}: x={start_x}, y={body_part_y}")  # Logging the initialization of each body part

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color, tag='snake')
            self.squares.append(square)
