from tkinter import Canvas

class Snake:
    def __init__(self, body_parts, canvas, space_size, snake_color):
        self.body_size = body_parts
        self.coordinates = []
        self.squares = []

        # Start the snake in the middle of the canvas
        start_x = canvas.winfo_width() // 2
        # Initialize the snake's body parts vertically within the canvas bounds
        # The snake's body parts will be initialized upwards from the starting position
        # Adjust the start_y position to be higher up on the canvas to prevent immediate collision
        start_y = (canvas.winfo_height() // 2) - (space_size * (body_parts - 1))

        for i in range(body_parts):
            body_part_y = start_y - (i * space_size)  # Adjusted to initialize upwards
            # Ensure the body part is within the canvas bounds
            if body_part_y < 0:
                # If the body part is above the top edge, place it starting from the bottom
                body_part_y = canvas.winfo_height() - ((body_parts - i) * space_size)
            self.coordinates.append([start_x, body_part_y])
            print(f"Initializing body part {i}: x={start_x}, y={body_part_y}")  # Logging the initialization of each body part

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color, tag='snake')
            self.squares.append(square)
