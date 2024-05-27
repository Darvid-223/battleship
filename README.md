# Battleship Game

## Introduction & Overview 

Battleship Game is a classic naval warfare strategy game brought to life as a Python-based command-line application. This project showcases the application of Python programming concepts, including object-oriented design, randomization, and user interaction in a terminal-based environment. The game is designed for both casual players and coding enthusiasts who enjoy strategy games and wish to experience the nostalgic feel of playing Battleship.

The Battleship Game offers a turn-based gameplay experience where players compete against a computer opponent. Players and the computer take turns to guess the location of each other's ships on a grid, aiming to sink all enemy ships first. The game provides immediate feedback on hits and misses, enhancing the interactive aspect and keeping players engaged throughout.

## Features

This implementation includes features such as:

- A welcome screen with ASCII art for an immersive start

- Configurable board sizes for varied difficulty levels

- Randomized ship placement for both player and computer

- Clear visual feedback for hits, misses, and the final state of the game board

- Cross-platform compatibility, ensuring smooth execution on different operating systems including Windows and Unix-based systems like Heroku

## Rationale for Board Class Design

### Introduction

The decision to implement the game board as a class in this Battleship game project was made to use the principles of object-oriented programming (OOP). This approach provides a structured and modular way to handle the game logic, making the code more maintainable and extensible. Normally, I would not use a class in a project as simple as this, but I am using it here to demonstrate and apply OOP principles.

### Why Use a Class for the Board?

**Reusability:** The class can be easily reused and extended for different versions of the game. For example, if we wanted to add more complex features like different ship sizes or special rules, we can do so by extending the Board class without affecting the rest of the code.

**Readability:** Classes help in breaking down the code into manageable parts. By separating the board logic into its own class, the main game logic becomes clearer and easier to follow.

**Maintainability:** If any changes need to be made to the board logic, such as changing how ships are placed or how the board is displayed, these changes can be made within the Board class without affecting other parts of the program.

### My Python Training

I have previously studied Python through courses on [Udemy](https://www.udemy.com/course/100-days-of-code/) and [Codecademy](https://www.codecademy.com/catalog/language/python), which included lessons on object-oriented programming. This background knowledge helped me understand and apply the principles of OOP effectively in this project.


### Validator Testing

### Bugs

- Clear Screen Bug

There was an issue where the clear_screen function did not work properly when the game was deployed on Heroku. The cls command, which is used to clear the screen on Windows, is not recognized on Unix-based systems like those used by Heroku.

- Resolution

The bug was resolved by updating the clear_screen function to use the appropriate command based on the operating system. The updated function checks the OS type and uses cls for Windows and clear for Unix-based systems:

import os

def clear_screen():
    """
    Function to clear terminal.
    """
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    else:
        print("\n" * 100)  # Fallback in case of other OS types

## Technologies Used
### Tools and Resources

- [Git](https://git-scm.com/): Employed for version control, enabling regular commits to Git and updates to GitHub from the terminal in Gitpod.

- [GitHub](https://github.com/): Hosts the repository containing the project's code. GitHub Pages also hosts the live version of the website.

- [Visual Studio Code](https://code.visualstudio.com/): The code editor of choice for developing the website, offering powerful coding and debugging tools.

- [OpenAI's ChatGPT](https://openai.com/): Assisted in validating code, checking spelling, providing translations, offering coding advice, and supporting the refinement of the website's content and functionality. ChatGPT also played a role in generating content for documentation and assisting with real-time troubleshooting during development.

## Deployment

### Github Pages

### Heroku

## Local Development Setup

### Introduction

### Why Visual Studio Code and WSL?

Visual Studio Code is a powerful and versatile code editor that supports a wide range of programming languages and frameworks. Its extensive library of extensions makes it highly customizable, fitting perfectly into my workflow. Furthermore, by leveraging the Windows Subsystem for Linux (WSL), I was able to create a Linux-like development environment on Windows. This setup allowed me to use Linux commands and tools directly in Windows, offering the best of both worlds for web development.

Choosing Visual Studio Code and WSL over Codeanywhere was a strategic decision to optimize my development process, capitalizing on speed and efficiency without sacrificing the versatility and power needed for complex web development tasks.

### Prerequisites

### Setting Up the Environment

## Credits & Acknowledgments

### Acknowledgements

- I am deeply grateful to my mentor, Sheryl Goldberg, for her invaluable feedback and insightful suggestions, which greatly enhanced this project.

- Special thanks to my friend Lucas Behrendt, whose feedback and tips from his experience in the same course were immensely helpful.

- Special thanks to https://www.asciiart.eu/ for providing the ASCII art used in this project.

This project was developed with the assistance of OpenAI's ChatGPT in the following areas:
- **Code Validation**: ChatGPT helped validate the syntax and logic of the code.
- **Spelling and Grammar Checks**: Assisted in checking and correcting spelling and grammar in the documentation and code comments.
- **Translations**: Provided translations for multilingual support in the documentation.
- **Coding Advice**: Offered suggestions and advice on coding practices and problem-solving approaches.
- **Content Generation**: Assisted in generating content for the README and other documentation.
- **Real-Time Troubleshooting**: Supported real-time debugging and troubleshooting during the development process.

Special thanks to [OpenAI's ChatGPT](https://openai.com/) for its invaluable support in refining the content and functionality of this project.
