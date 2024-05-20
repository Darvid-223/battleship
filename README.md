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
