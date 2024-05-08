from tkinter import *
from food import Food
from snake import Snake
import time
import random

class Game:
    def __init__(self):
        self.game_width = 1000
        self.game_height = 700
        self.speed = 80
        self.space_size = 40
        self.body_parts = 3
        self.snake_color = "#00FF00"
        self.food_color = "#FF0000"
        self.background_color = "#000000"
        self.score = 0
        self.direction = 'down'
        self.window = Tk()
        self.window.title("Snake Game")
        self.window.resizable(False, False)

        self.turn_counter = 0  # Initialize the turn counter at 0
        self.max_turns = 100  # Set the maximum number of turns for the game

        self.score_label = Label(self.window, text="Score: {}".format(self.score), font=("Consolas", 25))
        self.score_label.grid(row=0, column=0, sticky="w")

        self.canvas = Canvas(self.window, bg=self.background_color, height=self.game_height, width=self.game_width)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.snake = None
        self.food = None
        self.start_game()

        # Update key bindings to call methods on the Game class instance
        self.window.bind('<Left>', lambda event: self.change_direction('left'))
        self.window.bind('<Right>', lambda event: self.change_direction('right'))
        self.window.bind('<Up>', lambda event: self.change_direction('up'))
        self.window.bind('<Down>', lambda event: self.change_direction('down'))
        self.window.bind('<Return>', self.restart_game)

        # The action space is static, so we can define it in the __init__ method
        self.action_space = ['up', 'down', 'left', 'right']

        self.q_table = {}  # Initialize the Q-table as an empty dictionary
        self.initialize_q_table()  # Call the method to populate the Q-table with default values

    def initialize_q_table(self):
        """Initialize the Q-table with default values."""
        # The Q-table will be populated with new states as they are encountered
        # No pre-population is necessary as the state space is large
        pass  # Placeholder for any future initialization logic

    def check_collision(self, position=None):
        if position is None:
            position = self.snake.coordinates[0]
        x, y = position

        if x < 0 or x >= self.game_width:
            print("GAME OVER: Collision with wall on x-axis")
            return True
        elif y < 0 or y >= self.game_height:
            print("GAME OVER: Collision with wall on y-axis")
            return True

        for body_part in self.snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                print("GAME OVER: Collision with self")
                return True

        return False

    def game_over(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2, fill="red", text="GAME OVER", font=("consolas", 70), tag="gameover")
        self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2 + 50, fill="blue", text="Press Enter to restart", font=("consolas", 30), tag="gameover")

    def change_direction(self, new_direction):
        if new_direction == 'left' and self.direction != 'right':
            self.direction = new_direction
        elif new_direction == 'right' and self.direction != 'left':
            self.direction = new_direction
        elif new_direction == 'up' and self.direction != 'down':
            self.direction = new_direction
        elif new_direction == 'down' and self.direction != 'up':
            self.direction = new_direction

    def get_state(self):
        """Return the current state of the game as a string."""
        # Convert the positions to a string format
        snake_position = '-'.join(f"{x},{y}" for x, y in self.snake.coordinates)
        food_position = f"{self.food.coordinates[0]},{self.food.coordinates[1]}"
        # Concatenate the positions and current direction into a single string
        state = f"{snake_position}|{food_position}|{self.direction}"
        return state

    def get_reward(self):
        """Calculate and return the reward based on the game's rules."""
        if self.check_collision():
            return -10  # Negative reward for collision
        elif self.snake.coordinates[0] == self.food.coordinates:
            return 10  # Positive reward for eating food
        else:
            return -1  # Slight negative reward to encourage faster food finding

    def start_game(self):
        # Removed setting initial direction here; will set it in initialize_game_objects after canvas dimensions are confirmed
        self.score = 0
        self.speed = 80
        self.score_label.config(text="Score:{}".format(self.score))
        self.canvas.delete("gameover")
        # Delay the start of the game to ensure the canvas is fully rendered
        # Increase the delay to allow more time for the canvas to be fully rendered
        self.window.after(500, self.initialize_game_objects)

    def initialize_game_objects(self):
        print("Initializing game objects...")
        self.check_canvas_dimensions()
        safe_directions = self.get_safe_actions()
        if safe_directions:
            self.direction = safe_directions[0]  # Set the initial direction to the first safe direction
        else:
            self.direction = 'right'  # Default direction if no safe actions are found
        self.snake = Snake(self.body_parts, self.canvas, self.space_size, self.snake_color, initial_position=(self.game_width // 2, self.game_height // 4))
        self.food = Food(self.game_width, self.game_height, self.space_size, self.canvas, self.food_color)
        self.next_turn()

    def check_canvas_dimensions(self):
        if not hasattr(self, 'init_attempts'):
            self.init_attempts = 0  # Initialize the counter on the first method call
        # Log the current canvas dimensions
        current_width = self.canvas.winfo_width()
        current_height = self.canvas.winfo_height()
        print(f"Current canvas dimensions: width={current_width}, height={current_height}")
        # Allow a larger margin of error in the canvas size
        width_tolerance = self.game_width + 10  # Increased tolerance for width
        height_tolerance = self.game_height + 10  # Increased tolerance for height
        if self.game_width <= current_width <= width_tolerance and self.game_height <= current_height <= height_tolerance:
            self.snake = Snake(self.body_parts, self.canvas, self.space_size, self.snake_color, initial_position=(self.game_width // 2, self.game_height // 4))
            self.food = Food(self.game_width, self.game_height, self.space_size, self.canvas, self.food_color)
            self.next_turn()
        else:
            self.init_attempts += 1
            if self.init_attempts < 50:  # Maximum number of attempts before timing out
                self.window.after(100, self.check_canvas_dimensions)
            else:
                print("Error: Canvas dimensions could not be confirmed after multiple attempts.")

    def restart_game(self, event):
        self.start_game()

    def next_turn(self):
        self.turn_counter += 1  # Increment the turn counter
        if self.turn_counter > self.max_turns:  # Check if the maximum number of turns has been reached
            self.game_over()  # Terminate the game
            return  # Exit the function to prevent further game progression

        if self.score == 0:  # On the first turn, ensure the snake moves in a safe direction
            # Determine a safe initial direction based on the starting position of the snake
            safe_directions = self.get_safe_actions()
            if 'down' in safe_directions:
                self.change_direction('down')
            elif 'right' in safe_directions:
                self.change_direction('right')
            elif 'left' in safe_directions:
                self.change_direction('left')
            elif 'up' in safe_directions:
                self.change_direction('up')
        else:
            state = self.get_state()
            action = self.select_action(state)
            # Execute the action and get the reward
            reward = self.execute_action(action)
            # Get the next state after the action
            next_state = self.get_state()
            # Update the Q-table with the new information
            self.update_q_table(state, action, reward, next_state)

        if self.check_collision():
            self.game_over()
        else:
            self.window.after(self.speed, self.next_turn)

    def select_action(self, state):
        """Select an action based on the epsilon-greedy strategy, avoiding immediate collisions."""
        epsilon = 0.1  # Exploration probability
        safe_actions = self.get_safe_actions()  # Get the list of safe actions based on the current state

        if random.uniform(0, 1) < epsilon:
            # Explore: select a random safe action
            return random.choice(safe_actions)
        else:
            # Exploit: select the best action based on the current state and Q-table
            q_values = self.q_table.get(state, {})
            if q_values:
                # Filter out unsafe actions from the Q-values dictionary
                safe_q_values = {action: q for action, q in q_values.items() if action in safe_actions}
                if safe_q_values:
                    return max(safe_q_values, key=safe_q_values.get)
                else:
                    # If no safe actions have Q-values, choose a safe action randomly
                    return random.choice(safe_actions)
            else:
                # If the state is not in the Q-table, choose a safe action randomly
                return random.choice(safe_actions)

    def get_safe_actions(self):
        """Return a list of safe actions that won't result in immediate collisions."""
        safe_actions = []
        x, y = self.snake.coordinates[0]

        # Check if moving in each direction would result in a collision
        if y - self.space_size >= 0 and not any((x, y - self.space_size) == body_part for body_part in self.snake.coordinates):
            safe_actions.append('up')
        if y + self.space_size < self.game_height and not any((x, y + self.space_size) == body_part for body_part in self.snake.coordinates):
            safe_actions.append('down')
        if x - self.space_size >= 0 and not any((x - self.space_size, y) == body_part for body_part in self.snake.coordinates):
            safe_actions.append('left')
        if x + self.space_size < self.game_width and not any((x + self.space_size, y) == body_part for body_part in self.snake.coordinates):
            safe_actions.append('right')

        return safe_actions if safe_actions else ['up', 'down', 'left', 'right']  # Return all actions if no safe actions are found

    def execute_action(self, action):
        """Execute the selected action and update the game state."""
        x, y = self.snake.coordinates[0]

        if action == "up":
            y -= self.space_size
        elif action == "down":
            y += self.space_size
        elif action == "left":
            x -= self.space_size
        elif action == "right":
            x += self.space_size

        self.snake.coordinates.insert(0, (x, y))
        square = self.canvas.create_rectangle(x, y, x + self.space_size, y + self.space_size, fill=self.snake_color)
        self.snake.squares.insert(0, square)

        # Initialize reward
        reward = 0

        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            self.score += 1
            self.score_label.config(text="Score:{}".format(self.score))
            self.canvas.delete("food")
            self.food = Food(self.game_width, self.game_height, self.space_size, self.canvas, self.food_color)
            self.speed = max(30, self.speed - 1)  # Decrease speed by 1, minimum of 30 to avoid too high speed
            reward = 10  # Positive reward for eating food
        else:
            del self.snake.coordinates[-1]
            self.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]
            reward = -1  # Slight negative reward to encourage faster food finding

        # Check for collisions and continue the game loop
        if self.check_collision():
            self.game_over()
            reward = -10  # Negative reward for collision

        return reward

    def update_q_table(self, state, action, reward, next_state):
        """Update the Q-table based on the action taken and the resulting state."""
        # Learning rate and discount factor
        alpha = 0.1
        gamma = 0.9

        # Initialize the state in the Q-table if it does not exist
        if state not in self.q_table:
            self.q_table[state] = {a: 0 for a in self.action_space}
        if next_state not in self.q_table:
            self.q_table[next_state] = {a: 0 for a in self.action_space}

        # Current Q-value for the state-action pair
        current_q_value = self.q_table[state][action]

        # Maximum Q-value for the next state
        next_max_q_value = max(self.q_table[next_state].values())

        # Q-learning update rule
        self.q_table[state][action] = current_q_value + alpha * (reward + gamma * next_max_q_value - current_q_value)
