"""
Import randint from random to generate bot coordinates.
Import os to clear the terminal.
Import ascii_art to display ASCII art.
Import fontstyle for terminal font
"""
from random import randint
import os
import ascii_art
import fontstyle


def welcome_screen():
    """
    Display the welcome screen with ASCII art and game instructions.
    """
    clear_screen()
    print(ascii_art.BATTLESHIP)
    print(fontstyle.apply("\nWelcome to Battleship!\n", "bold/italic"))


def clear_screen():
    """
    Function to clear terminal. Uses 'cls' on windows
    and 'clear' on UNIX-based OS.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        # For UNIX based OS.
        os.system("clear")


def get_player_input():
    """
    Get player input for name and board size and number of ships.
    """
    name = input("Enter your name:\n")

    while True:
        size_choice = input("Choose board size (small, medium, large):\n")\
                      .lower()

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

    while True:
        try:
            num_ships = int(input("Choose the number of ships (1-10):\n"))
            if 1 <= num_ships <= 10:
                break
            else:
                print(
                    "Invalid choice, please choose a number between 1 and 10.")
        except ValueError:
            print("Invalid input, please enter a number between 1 and 10.")

    print("\nEach ship occupies 1 coordinate or cell space.\n")
    
    return name, board_size, num_ships


class Board:
    def __init__(self, size):
        """
        Initialize the game board with a given size.

        Parameters:
        size (int): The size of the board (number of rows and columns).
        """
        self.size = size
        self.grid = [["~"] * size for _ in range(size)]
        self.ships = []

    def display(self, show_ships=False):
        """
        Display the game board.

        Parameters:
        show_ships (bool): If True, display the ships' positions.
        If False, hide the ships' positions.
        This function was created with the assistance of OpenAI's ChatGPT.
        """
        # Print column numbers
        print("  " + " ".join([str(i) for i in range(1, self.size + 1)]))
        # Get index and row from self.grid.
        for idx, row in enumerate(self.grid):
            if show_ships:
                # Print row numbers and grid row as is
                print(str(idx + 1) + " " + " ".join(row))
            else:
                # Replace S with ~ if ships should not be shown
                print(str(idx + 1) + " " + " ".join(
                    [cell if cell != "S" else "~" for cell in row]
                ))

        print()

    def place_ships(self, num_ships):
        """
        Place a specified number of ships randomly on the board.

        Parameters:
        num_ships (int): The number of ships to place on the board.
        This function was created with the assistance of OpenAI's ChatGPT.
        """
        self.ships = []
        placed_ships = 0
        while placed_ships < num_ships:
            row = randint(0, self.size - 1)
            col = randint(0, self.size - 1)
            if self.grid[row][col] == "~":
                self.grid[row][col] = "S"
                self.ships.append((row, col))
                placed_ships += 1

    def take_shot(self, row, col):
        """
        Take a shot at the specified position.
        """
        if self.grid[row][col] == "S":
            self.grid[row][col] = "X"  # Hit
            return True
        elif self.grid[row][col] == "~":
            self.grid[row][col] = "O"  # Miss
            return False
        return None  # Invalid shot (already taken)

    def all_ships_sunk(self):
        """
        Check if Game is Over.
        """
        for row in self.grid:
            if "S" in row:
                return False
        return True


def player_turn(board, board_size):
    """
    Handle the player's turn.
    """
    while True:
        try:
            shot_row = int(input(f"Enter row to shoot (1-{board_size}): ")) - 1
            shot_col = int(input(
                f"Enter column to shoot (1-{board_size}): ")) - 1
            if 0 <= shot_row < board_size and 0 <= shot_col < board_size:
                result = board.take_shot(shot_row, shot_col)
                if result is not None:
                    if result:
                        clear_screen()
                        print("Hit!")
                    else:
                        clear_screen()
                        print("Miss!")
                    break
                else:
                    print("Invalid shot. Try again.")
            else:
                print(f"Invalid input. Please enter numbers between 1 and "
                      f"{board_size}.")
        except ValueError:
            print("Invalid input. Enter numbers only.")


def computer_turn(board, board_size):
    """
    Handle the computer's turn with random integer.
    """
    while True:
        shot_row = randint(0, board_size - 1)
        shot_col = randint(0, board_size - 1)
        if board.take_shot(shot_row, shot_col) is not None:

            print(f"Computer shoots at ({shot_row + 1}, {shot_col + 1})")
            break


def setup_game():
    """
    Set up the game.
    """
    clear_screen()
    welcome_screen()
    name, board_size, num_ships = get_player_input()
    clear_screen()
    print(f"\nWelcome, {name}!\n")
    return name, board_size, num_ships


def create_boards(board_size, num_ships):
    """
    Create and place ships on player and computer boards.
    """
    player_board = Board(board_size)
    computer_board = Board(board_size)
    player_board.place_ships(num_ships)
    computer_board.place_ships(num_ships)
    return player_board, computer_board


def game_loop(player_board, computer_board, board_size):
    """
    Main game loop where player and computer take turns.
    """
    while True:
        print("Player's Board:")
        player_board.display(show_ships=True)

        print("Computer's Board:")
        computer_board.display(show_ships=False)
        # For debugging, show ship position (1 index)
        print(f"Computer's ship positions: "
              f"{[(row + 1, col + 1) for row, col in computer_board.ships]} "
              f"(1 index)")
        # Player's turn
        player_turn(computer_board, board_size)
        if computer_board.all_ships_sunk():
            print("Congratulations, you won!")
            break

        # Computer's turn
        computer_turn(player_board, board_size)
        if player_board.all_ships_sunk():
            print("Sorry, you lost. Computer won!")
            break


def main():
    """
    Main function to initialize and run the Battleship game.
    """
    name, board_size, num_ships = setup_game()
    player_board, computer_board = create_boards(board_size, num_ships)
    game_loop(player_board, computer_board, board_size)


main()
