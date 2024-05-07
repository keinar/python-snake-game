from tkinter import *
from food import Food
from snake import Snake

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

    def check_collision(self):
        x, y = self.snake.coordinates[0]

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

    def start_game(self):
        self.direction = "up"  # Set the initial direction to 'up' to avoid immediate collision
        self.score = 0
        self.speed = 80
        self.score_label.config(text="Score:{}".format(self.score))
        self.canvas.delete("gameover")

        # Delay the snake's creation until the canvas is fully initialized
        self.window.after(100, self.initialize_game_objects)

    def initialize_game_objects(self):
        self.snake = Snake(self.body_parts, self.canvas, self.space_size, self.snake_color)
        self.food = Food(self.game_width, self.game_height, self.space_size, self.canvas, self.food_color)
        self.next_turn()

    def restart_game(self, event):
        self.start_game()

    def next_turn(self):
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
            self.score_label.config(text="Score:{}".format(self.score))
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
