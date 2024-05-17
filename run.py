"""
Import randint from random to generate bot coordinates.
Import os to clear the terminal.
Import ascii_art to display ASCII art.
"""
from random import randint
import os
import ascii_art

def welcome_screen():
    print(ascii_art.BATTLESHIP)

class Board:
    """
    Main class that takes size as argument
    """
    def __init__(self, size):
        self.size = size

    
def scoreboard():
    pass


def main():
    """
    Main function to run the Battleship game.
    """
    welcome_screen()
    

main()




