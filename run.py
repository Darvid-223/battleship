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

    def display(self, show_ships=False):
        # Print column numbers
        print("  " + " ".join([str(i) for i in range(1, self.size + 1)]))
        for idx, row in enumerate(self.grid):
            if show_ships:
                # Print row numbers and grid row as is
                print(str(idx + 1) + " " + " ".join(row))
            else:
                # Replace 'S' with '~' if ships should not be shown
                print(str(idx + 1) + " " + " ".join([cell if cell != 'S' else '~' for cell in row]))
        print()

    def place_ships(self, num_ships):
        placed_ships = 0
        while placed_ships < num_ships:
            row = randint(0, self.size - 1)
            col = randint(0, self.size - 1)
            if self.grid[row][col] == '~':
                self.grid[row][col] = 'S'
                placed_ships += 1


def main():
    clear_screen()
    welcome_screen()

    name, board_size = get_player_input()
    print(f"\nWelcome, {name}!\n")

    player_board = Board(board_size)
    computer_board = Board(board_size)

    num_ships = 5  # Define the number of ships to be placed on the board

    player_board.place_ships(num_ships)
    computer_board.place_ships(num_ships)

    print("Player's Board:")
    player_board.display(show_ships=True)

    print("Computer's Board:")
    computer_board.display(show_ships=False)

main()