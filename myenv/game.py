from tkinter import *
from food import Food
from snake import Snake
import numpy as np

class Game:
    def __init__(self, mode='manual'):
        self.mode = mode  # 'manual' for playing manually, 'ai' for AI mode
        self.game_width = 1000
        self.game_height = 700
        self.speed = 150
        self.speed_to_display = 0
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

        # AI attributes
        self.epsilon = 1.0  # Starting value for epsilon
        self.epsilon_min = 0.01  # Minimum value for epsilon
        self.epsilon_decay = 0.995  # Decay rate for epsilon after each game iteration
        self.actions = ['up', 'down', 'left', 'right']  # Possible actions
        self.q_table = {}  # Q-table for storing state-action values
        self.initialize_q_table()

    def initialize_q_table(self):
        # Initialize the Q-table with default values for all possible states and actions
        for state in self.all_possible_states():
            self.q_table[state] = {action: 0.0 for action in self.actions}

    def all_possible_states(self):
        states = []
        # Consider only the relative position of the food to the snake's head and immediate dangers
        for food_x in range(0, self.game_width, self.space_size):
            for food_y in range(0, self.game_height, self.space_size):
                for direction in ['up', 'down', 'left', 'right']:
                    # Relative position of food from the snake's head
                    food_relative_x = (food_x - self.snake.coordinates[0][0]) // self.space_size
                    food_relative_y = (food_y - self.snake.coordinates[0][1]) // self.space_size
                    # Immediate danger checks
                    if direction == 'up':
                        danger_straight = self.check_collision(self.snake.coordinates[0][0], self.snake.coordinates[0][1] - self.space_size)
                        danger_right = self.check_collision(self.snake.coordinates[0][0] + self.space_size, self.snake.coordinates[0][1])
                        danger_left = self.check_collision(self.snake.coordinates[0][0] - self.space_size, self.snake.coordinates[0][1])
                    elif direction == 'down':
                        danger_straight = self.check_collision(self.snake.coordinates[0][0], self.snake.coordinates[0][1] + self.space_size)
                        danger_right = self.check_collision(self.snake.coordinates[0][0] - self.space_size, self.snake.coordinates[0][1])
                        danger_left = self.check_collision(self.snake.coordinates[0][0] + self.space_size, self.snake.coordinates[0][1])
                    elif direction == 'left':
                        danger_straight = self.check_collision(self.snake.coordinates[0][0] - self.space_size, self.snake.coordinates[0][1])
                        danger_right = self.check_collision(self.snake.coordinates[0][0], self.snake.coordinates[0][1] - self.space_size)
                        danger_left = self.check_collision(self.snake.coordinates[0][0], self.snake.coordinates[0][1] + self.space_size)
                    elif direction == 'right':
                        danger_straight = self.check_collision(self.snake.coordinates[0][0] + self.space_size, self.snake.coordinates[0][1])
                        danger_right = self.check_collision(self.snake.coordinates[0][0], self.snake.coordinates[0][1] + self.space_size)
                        danger_left = self.check_collision(self.snake.coordinates[0][0], self.snake.coordinates[0][1] - self.space_size)
                    else:
                        danger_straight = danger_right = danger_left = False
                    # Create a state representation
                    state = (food_relative_x, food_relative_y, direction, danger_straight, danger_right, danger_left)
                    states.append(state)
        return states

        self.score_label = Label(self.window, text="Score: {}".format(self.score), font=("Consolas", 25))
        self.score_label.grid(row=0, column=0, sticky="w")
        self.speed_label = Label(self.window, text="Current Speed: {}".format(self.speed_to_display), font=("Consolas", 25))
        self.speed_label.grid(row=0, column=1, sticky="e")
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

    def check_collision(self, future_head_x=None, future_head_y=None):
        # Use current head position if no future position is provided
        if future_head_x is None or future_head_y is None:
            future_head_x, future_head_y = self.snake.coordinates[0]

        # Check collision with walls
        if future_head_x < 0 or future_head_x >= self.game_width:
            return True
        elif future_head_y < 0 or future_head_y >= self.game_height:
            return True

        # Check collision with self
        for body_part in self.snake.coordinates[1:]:
            if future_head_x == body_part[0] and future_head_y == body_part[1]:
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

    def start_game(self):
        self.direction = "down"
        self.score = 0
        self.speed = 150
        self.speed_to_display = 0
        self.score_label.config(text="Score:{}".format(self.score))
        self.speed_label.config(text="Current Speed:{}".format(self.speed_to_display))
        self.canvas.delete("gameover")
        self.snake = Snake(self)
        self.food = Food(self.game_width, self.game_height, self.space_size, self.canvas, self.food_color)
        self.next_turn()

    def restart_game(self, event):
        self.start_game()

    def next_turn(self):
        if self.mode == 'ai':
            self.ai_next_turn()
        else:
            x, y = self.snake.coordinates[0]

            if self.direction == "up":
                y -= self.space_size
            elif self.direction == "down":
                y += self.space_size
            elif self.direction == "left":
                x -= self.space_size
            elif self.direction == "right":
                x += self.space_size

            self.snake.coordinates.insert(0, (x, y))
            square = self.canvas.create_rectangle(x, y, x + self.space_size, y + self.space_size, fill=self.snake_color)
            self.snake.squares.insert(0, square)

            if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
                self.score += 1
                self.speed_to_display += 1
                self.score_label.config(text="Score:{}".format(self.score))
                self.speed_label.config(text="Current Speed:{}".format(self.speed_to_display))
                self.canvas.delete("food")
                self.food = Food(self.game_width, self.game_height, self.space_size, self.canvas, self.food_color)
                self.speed = max(30, self.speed - 1)  # Decrease speed by 1, minimum of 30 to avoid too high speed
            else:
                del self.snake.coordinates[-1]
                self.canvas.delete(self.snake.squares[-1])
                del self.snake.squares[-1]

            if self.check_collision():
                self.game_over()
            else:
                self.window.after(self.speed, self.next_turn)
                # Epsilon decay after each turn
                if self.mode == 'ai':
                    self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)

    def execute_action(self, action):
        # Change the snake's direction based on the action
        self.change_direction(action)
        # Move the snake and check for collisions or food consumption
        self.next_turn()
        # Calculate the reward based on the game state changes
        reward = self.calculate_reward()
        # Get the next state after the action is executed
        next_state = self.get_state()
        return reward, next_state

    def calculate_reward(self):
        # Check if the snake has eaten food
        if self.snake.coordinates[0] == self.food.coordinates:
            return 10  # Positive reward for eating food
        # Check if the snake has collided with the wall or itself
        elif self.check_collision(self.snake.coordinates[0][0], self.snake.coordinates[0][1]):
            return -10  # Negative reward for collision
        else:
            # Calculate the Manhattan distance to the food
            head_x, head_y = self.snake.coordinates[0]
            food_x, food_y = self.food.coordinates
            distance_to_food = abs(head_x - food_x) + abs(head_y - food_y)
            # Smaller negative reward for each move to encourage finding the shortest path
            return -1 * distance_to_food / 100

    # AI functionalities
    def get_state(self):
        head_x, head_y = self.snake.coordinates[0]
        food_x, food_y = self.food.coordinates
        state = [
            # Distance from the snake's head to the food
            abs(head_x - food_x) + abs(head_y - food_y),
            # Danger straight
            self.direction == 'up' and self.check_collision((head_x, head_y - self.space_size)) or
            self.direction == 'down' and self.check_collision((head_x, head_y + self.space_size)) or
            self.direction == 'left' and self.check_collision((head_x - self.space_size, head_y)) or
            self.direction == 'right' and self.check_collision((head_x + self.space_size, head_y)),
            # Danger right
            self.direction == 'up' and self.check_collision((head_x + self.space_size, head_y)) or
            self.direction == 'down' and self.check_collision((head_x - self.space_size, head_y)) or
            self.direction == 'left' and self.check_collision((head_x, head_y - self.space_size)) or
            self.direction == 'right' and self.check_collision((head_x, head_y + self.space_size)),
            # Danger left
            self.direction == 'up' and self.check_collision((head_x - self.space_size, head_y)) or
            self.direction == 'down' and self.check_collision((head_x + self.space_size, head_y)) or
            self.direction == 'left' and self.check_collision((head_x, head_y + self.space_size)) or
            self.direction == 'right' and self.check_collision((head_x, head_y - self.space_size)),
            # Current direction of the snake's movement
            self.direction == 'up',
            self.direction == 'down',
            self.direction == 'left',
            self.direction == 'right',
        ]
        return np.array(state, dtype=int)

    def select_action(self, state):
        # Epsilon-greedy strategy
        if np.random.rand() < self.epsilon:
            # Exploration: choose a random action
            return np.random.choice(self.actions)
        else:
            # Exploitation: choose the best action based on max Q-value
            q_values = self.q_table[state]
            return max(q_values, key=q_values.get)

    def update_q_table(self, state, action, reward, next_state):
        # Learning rate
        alpha = 0.1
        # Discount factor
        gamma = 0.6
        # Current Q value
        current_q_value = self.q_table[state][action]
        # Maximum Q value for the next state
        max_next_q_value = max(self.q_table[next_state].values())
        # Q-learning formula
        self.q_table[state][action] = current_q_value + alpha * (reward + gamma * max_next_q_value - current_q_value)

    def ai_next_turn(self):
        # Get the current state of the game
        state = self.get_state()
        # Select an action based on the current state
        action = self.select_action(state)
        # Execute the chosen action and get the reward
        reward, next_state = self.execute_action(action)
        # Update the Q-table with the new state and reward information
        self.update_q_table(state, action, reward, next_state)
        # Schedule the next turn
        self.window.after(self.speed, self.ai_next_turn)
