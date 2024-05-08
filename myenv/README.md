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

### Integration Process

The AI trainer was integrated into the game by embedding the Q-learning algorithm within the `Game` class. The AI observes the game state through a series of sensors that provide information about the environment, such as the distance to the food, the presence of walls, and the position of the snake's body. The AI uses this information to make decisions and update its Q-table, which stores the expected rewards for taking certain actions in specific states.

### Epsilon Decay Strategy

To balance the exploration of new actions and the exploitation of known rewarding actions, the AI employs an epsilon decay strategy. Initially, the AI is more likely to choose actions at random to explore the game environment. Over time, as it learns, the epsilon value decays, and the AI becomes more confident in exploiting the knowledge it has gained to make more informed decisions.

### Testing and Performance

The AI trainer was tested in both training and play modes. During testing, the AI demonstrated an ability to learn from its actions and improve its gameplay over time. The AI started with a high rate of collisions and gradually learned to navigate the game environment more effectively, avoiding walls and its own body while pursuing food.

### Observing AI Learning

To observe the AI's learning process, users can watch the console logs that output the AI's chosen actions and the resulting state of the game after each turn. Additionally, visual cues in the game's interface, such as changes in the snake's movement or speed, can indicate the AI's decision-making and learning progress.

### Troubleshooting

If you encounter issues while running the game with the AI trainer, consider the following common problems and solutions:

- **Game does not start**: Ensure all dependencies are installed and the Python environment is correctly set up as per the installation instructions.
- **AI behaves erratically**: Check if the AI is still in the exploration phase of learning, indicated by a high epsilon value. As the epsilon value decays, the AI's decisions should become more consistent.
- **Errors in console**: Review the error messages and tracebacks to identify any issues in the code. Common issues may include incorrect file paths or missing imports.

### Future Improvements

Future updates to the AI trainer could include:

- Enhancing the state representation to include more detailed information about the game environment.
- Optimizing the Q-learning algorithm for faster convergence and better performance.
- Introducing additional learning strategies, such as deep reinforcement learning, to improve the AI's capabilities.

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
