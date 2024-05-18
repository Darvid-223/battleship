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
    
def clear_screen():
    """
    Function to clear terminal.
    """
    os.system("cls")

def get_player_input():
    """
    Get player input for name and board size.
    """
    name = input("Enter your name: ")

    while True:
        size_choice = input("Choose board size (small, medium, large): ").lower()
        if size_choice == "small":
            board_size = 5
            break
        elif size_choice == "medium":
            board_size = 7
            break
        elif size_choice == "large":
            board_size = 10
            break
        else:
            print("Invalid choice, please choose again.")
    
    return name, board_size

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['~'] * size for _ in range(size)]
        self.ships = []

    def display(self):
        for row in self.grid:
            print(' '.join(row))
        print()



def main():
    clear_screen()
    welcome_screen()
    get_player_input()

    board_size = 5  
    board = Board(board_size)

    board.display()

main()