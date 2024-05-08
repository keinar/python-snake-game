from tkinter import Canvas

class Snake:
    def __init__(self, body_parts, canvas, space_size, snake_color, initial_position=None):
        self.body_size = body_parts
        self.coordinates = []
        self.squares = []
        self.space_size = space_size

        if initial_position:
            start_x, start_y = initial_position
        else:
            # Start the snake in the middle of the canvas
            start_x = canvas.winfo_width() // 2
            # Initialize the snake's body parts vertically within the canvas bounds
            # The snake's body parts will be initialized downwards from the starting position
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

    def reposition_snake(self, canvas, game_width, game_height, space_size):
        """Reposition the snake to a safe starting location on the canvas."""
        # Find a safe starting position for the snake's head
        safe_x = game_width // 2
        safe_y = game_height // 2

        # Adjust the y-coordinate to ensure it's not too close to the top or bottom
        safe_y = max(space_size * self.body_size, min(safe_y, game_height - space_size * self.body_size))

        # Update the snake's coordinates to the new safe position
        self.coordinates = [[safe_x, safe_y - i * space_size] for i in range(self.body_size)]

        # Update the canvas with the new position of the snake
        for square in self.squares:
            canvas.delete(square)
        self.squares = []
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color, tag='snake')
            self.squares.append(square)

    def get_next_head_position(self, direction):
        """Calculate the next position of the snake's head based on the given direction."""
        # Get the current head position
        head_x, head_y = self.coordinates[0]
        # Determine the next position based on the direction
        if direction == 'up':
            head_y -= self.space_size
        elif direction == 'down':
            head_y += self.space_size
        elif direction == 'left':
            head_x -= self.space_size
        elif direction == 'right':
            head_x += self.space_size
        # Return the new position
        return head_x, head_y
