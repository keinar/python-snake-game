# Python Snake Game

## Introduction
This repository contains a Python-based snake game that utilizes the Tkinter library for its GUI. The game has been enhanced with an Object-Oriented Programming (OOP) design and includes an AI trainer that uses a Q-learning algorithm to learn and play the game.

## Installation
To set up the game environment, ensure that you have Python 3.6 or higher and Tkinter installed on your system. Tkinter can typically be installed with Python by default. If you need to install it separately and have administrative access, you can use the following command:
```
sudo apt-get install python3-tk
```
If you do not have administrative access or prefer not to use `sudo`, please consult the documentation for your specific operating system on how to install Tkinter without administrative privileges.

Clone the repository to your local machine and navigate to the project directory.

## Running the Game
To run the game in manual mode, use the following command:
```
python3 main.py --mode manual
```
To activate AI mode and watch the AI play the game, use the command:
```
python3 main.py --mode ai
```
The game can be played in two modes:
- Manual mode: where the player controls the snake using the keyboard.
- AI mode: where the AI controls the snake and learns to play over time.

## AI Trainer
The AI trainer is implemented using a Q-learning algorithm, which is a model-free reinforcement learning technique. It is currently in a developmental stage and is designed to improve its gameplay over time by learning from its actions. The AI makes decisions based on the state of the game, which includes the position of the snake, the position of the food, and the direction of the snake.

## Contributing
Contributions to the game's development are welcome. Please ensure to follow best practices for code style and commit messages as outlined in the [Python Style Guide](https://www.python.org/dev/peps/pep-0008/). For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate. To run the tests, navigate to the project directory and execute the following command:
```
python3 -m unittest discover -s tests
```

For more information on the Q-learning algorithm and its implementation in this game, you can refer to [this resource](https://en.wikipedia.org/wiki/Q-learning).

If you have any questions or need support, please open an issue in the repository, and we will be happy to assist you.

Please note that this project is open for collaboration, and we encourage you to contribute and share your ideas to improve the game further.
