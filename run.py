"""
Import randint from random to generate bot coordinates.
Import os to clear the terminal.
Import ascii_art to display ASCII art.
"""
from random import randint
import os
import ascii_art

def welcome_screen():
    """
    Display the welcome screen with ASCII art and game instructions.
    """
    clear_screen()
    print(ascii_art.BATTLESHIP)
    print("\nWelcome to Battleship!\n")
    
def settings():
    """
    Prompts the user to choose the board size by entering a size name.
    Continues to prompt until a valid input ('small', 'medium', or 'large') is entered.
    """
    valid_sizes = ["small", "medium", "large"]
    
    while True:
        try:
            size = input("Choose board size: small, medium, or large: ").strip().lower()
            if size in valid_sizes:
                return size
            else:
                raise ValueError("Invalid choice")
        except ValueError as e:
            print(e)
            print("Please enter 'small', 'medium', or 'large'.")



def clear_screen():
    """
    Function to clear terminal.
    """
    os.system("cls")

class Board:
    """
    Main class that takes size as argument and initializes the game board.
    """
    def __init__(self, size):
        size_mapping = {"small": 5, "medium": 7, "large": 10}
        self.size = size_mapping[size]
        self.grid = [['~'] * self.size for _ in range(self.size)]
        self.ships = []

    def display(self, reveal_ships=False):
        """
        Display the board.
        
        Parameters:
        - reveal_ships: bool, if True, show ships positions
        """
        for row in self.grid:
            if reveal_ships:
                print(' '.join(row))
            else:
                print(' '.join(['~' if cell == 'S' else cell for cell in row]))


class Ship:
    """
    Class to represent ships on the board.
    """
    def __init__(self, length):
        self.length = length
        self.hits = 0
        self.position = []

    def hit(self):
        """
        Register hit.
        """
        self.hits += 1
    
    def is_sunk(self):
        """
        Check if the ship is sunk.
        """
        return self.hits >= self.length


def scoreboard():
    pass


def main():
    """
    Main function to run the Battleship game.
    This function initializes the game.
    """
    welcome_screen()
    board_size_choice = settings()
    board = Board(board_size_choice)
    board.display(reveal_ships=True)

main()




