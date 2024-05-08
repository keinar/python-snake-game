# Python Snake Game

Welcome to the Python Snake Game! This is a simple yet fun implementation of the classic snake game where the player controls a snake to eat food while avoiding collisions with the game boundaries or itself.

## Installation

To run this game, you will need Python installed on your system. Clone the repository to your local machine using the following command:

```
git clone https://github.com/keinar/python-snake-game.git
```

Navigate to the cloned directory and install the required dependencies:

```
cd python-snake-game/myenv
pip install -r requirements.txt
```

## Running the Game

To start the game, run the following command in the terminal:

```
python main.py
```

## Game Controls

- Use the arrow keys to change the direction of the snake.
- The game speeds up slightly each time the snake eats food.

## Object-Oriented Design

The game is designed with an Object-Oriented Programming (OOP) approach, with separate classes for the `Game`, `Snake`, and `Food` components.

## AI Trainer

The AI trainer in the Python Snake Game is designed to learn how to play the game autonomously through reinforcement learning, specifically using a Q-learning algorithm. The AI observes the state of the game, makes decisions on the next move, and learns from the outcomes to improve over time.

### Epsilon Decay Strategy

To balance the exploration of new actions and the exploitation of known rewarding actions, the AI employs an epsilon decay strategy. Initially, the AI is more likely to choose actions at random to explore the game environment. Over time, as it learns, the epsilon value decays, and the AI becomes more confident in exploiting the knowledge it has gained to make more informed decisions.

### Running the Game with AI Trainer

To run the game with the AI trainer in training mode, use the following command:

```
python ai_train.py
```

This will start the game with the AI making decisions and learning from each turn. The game's interface will display the moves chosen by the AI, and the game speed will adjust according to the AI's performance.

For more information on the AI's implementation and the Q-learning algorithm, please refer to the `ai_train.py` file, which contains the AI trainer's logic and parameters.

## Contributing

Contributions to the game are welcome! Please feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
