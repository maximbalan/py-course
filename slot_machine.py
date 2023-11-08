import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
INVALID_NUMBER_INPUT = "Invalid input. Please enter a number."

ROWS = 3
COLS = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}

symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}


def check_win(columns, lines, bet, values):
    """
    This function checks if there is a win in a game based on the provided columns and lines.

    Args:
        columns (list): A list of lists where each sublist represents a column in the game.
            Each element in the sublist is a symbol.
        lines (int): The number of lines in the game.
        bet (int or float): The amount that the player has bet.
        values (dict): A dictionary where the keys are symbols and the values
            are the corresponding winnings for those symbols.

    Returns:
        int or float: The total winnings based on the symbols in the lines and the bet amount.
    """
    # Initialize winnings to 0
    winnings = 0
    winning_lines = []

    # Iterate over each line
    for line in range(lines):
        # Get the symbol in the first column of the current line
        symbol = columns[0][line]

        # Check each column in the current line
        for column in columns:
            # Get the symbol to check in the current column
            symbol_to_check = column[line]

            # If the symbol to check does not match the initial symbol, break the loop
            if symbol != symbol_to_check:
                break
        else:
            # If all symbols in the line are the same,
            # add the winnings for that symbol times the bet to the total winnings
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    # Return the total winnings
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    This function simulates a spin of a slot machine.
    It generates a 2D list where each sublist represents a column in the slot machine.

    Args:
        rows (int): The number of rows in the slot machine.
        cols (int): The number of columns in the slot machine.
        symbols (dict): A dictionary where the keys are symbols and
            the values are the number of times each symbol should appear in the slot machine.

    Returns:
        list: A 2D list representing the state of the slot machine after the spin.
            Each sublist is a column and contains symbols.
    """
    # Initialize an empty list to hold all symbols
    all_symbols = []

    # Populate the all_symbols list based on the symbols dictionary
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # Initialize an empty list to hold the columns
    columns = []

    # Generate each column
    for _ in range(cols):
        # Initialize an empty list to hold the current column
        column = []

        # Make a copy of all_symbols to use for this column
        current_symbols = all_symbols[:]

        # Add a symbol to the column for each row
        for _ in range(rows):
            # Choose a random symbol from the current symbols
            value = random.choice(current_symbols)

            # Remove the chosen symbol from the current symbols
            current_symbols.remove(value)

            # Add the chosen symbol to the column
            column.append(value)

        # Add the column to the columns list
        columns.append(column)

    # Return the columns
    return columns


def print_slot_machine(columns):
    """
    This function prints the contents of a slot machine.
    The slot machine is represented as a list of columns, where each column is a list of symbols.

    Args:
        columns (List[List[str]]): A list of lists representing the slot machine.
                                   Each inner list is a column in the slot machine, and should have the same length.
    """
    # Iterate over each row in the columns
    for row in range(len(columns[0])):
        # Iterate over each column in the columns
        for i, column in enumerate(columns):
            # If this is not the last column, print the symbol in this row and column, followed by a separator
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            # If this is the last column, print the symbol in this row and column without a separator
            else:
                print(column[row])


def deposit():
    """
    This function prompts the user to enter an amount to deposit.
    It checks if the input is a positive integer and keeps prompting until a valid input is received.

    Returns:
        int: The amount to be deposited.
    """

    # Start an infinite loop
    while True:
        # Prompt the user to enter the amount to deposit
        amount = input("Enter amount to deposit in €: ")

        # Check if the input is a digit
        if amount.isdigit():
            # Convert the string input to an integer
            amount = int(amount)

            # Check if the amount is greater than 0
            if amount > 0:
                # If it is, break the loop
                break
            else:
                # If it's not, print an error message and continue the loop
                print("Amount must be greater than 0.")
        else:
            # If the input is not a digit, print an error message and continue the loop
            print(INVALID_NUMBER_INPUT)

    # Return the valid amount entered by the user
    return amount


def get_number_of_lines():
    """
    This function prompts the user to enter a number of lines to bet on.
    It validates the input to ensure it is a digit and within the range 1 to MAX_LINES.

    Returns:
        int: The valid number of lines entered by the user.
    """
    # Infinite loop until valid input is received
    while True:
        # Prompt the user to enter a number of lines to bet on
        lines = input(f"Enter number of lines to bet on (1-{str(MAX_LINES)}): ")

        # Check if the input is a digit
        if lines.isdigit():
            # Convert the input to an integer
            lines = int(lines)

            # Check if the input is within the valid range
            if 1 <= lines <= MAX_LINES:
                # Break the loop if the input is valid
                break
            else:
                # Print error message if the input is not within the valid range
                print("Please enter a valid number of lines.")
        else:
            # Print error message if the input is not a digit
            print(INVALID_NUMBER_INPUT)

    # Return the valid number of lines
    return lines


def get_bet():
    """
    This function prompts the user to enter a bet amount for each line.
    It checks if the entered amount is a digit and within the defined minimum and maximum bet limits.
    If the input is not a digit or not within the limits, it will keep asking until a valid input is provided.

    Returns:
        int: The validated bet amount entered by the user.
    """

    # Start an infinite loop to keep asking for input until a valid one is provided
    while True:
        # Prompt the user to enter the bet amount
        amount = input("Enter bet amount in € for each line: ")

        # Check if the entered amount is a digit
        if amount.isdigit():
            # Convert the amount to integer
            amount = int(amount)

            # Check if the amount is within the defined minimum and maximum bet limits
            if MIN_BET <= amount <= MAX_BET:
                # If the amount is valid, break the loop
                break

            else:
                # If the amount is not within the limits, print an error message
                print(f"Amount must be between €{MIN_BET} and €{MAX_BET}.")

        else:
            # If the entered amount is not a digit, print an error message
            print(INVALID_NUMBER_INPUT)

    # Return the validated bet amount
    return amount


def spin(balance):
    """
    This function simulates a spin in a slot machine game.
    It first gets the number of lines to bet on and the bet amount per line.
    It then checks if the total bet is within the player's balance.
    If it is, it proceeds to spin the slot machine, calculate the winnings, and print the results.

    Args:
        balance (int): The current balance of the player.

    Returns:
        int: The net gain or loss from the spin (winnings minus total bet).
    """

    # Get the number of lines to bet on
    lines = get_number_of_lines()

    # Start an infinite loop to keep asking for input until a valid one is provided
    while True:
        # Get the bet amount per line
        bet = get_bet()

        # Calculate the total bet
        total_bet = lines * bet

        # Check if the total bet is within the player's balance
        if total_bet > balance:
            # If not, print an error message
            print(
                f"You do not have enough to bet that amount, your current balance is €{balance}."
            )
        else:
            # If the total bet is within the player's balance, break the loop
            break

    # Print the total bet and the number of lines
    print(f"You are betting € {total_bet} on {lines} lines.")

    # Spin the slot machine
    slots = get_slot_machine_spin(rows=ROWS, cols=COLS, symbols=symbol_count)

    # Print the result of the spin
    print_slot_machine(slots)

    # Check the winnings and the winning lines
    winnings, winning_lines = check_win(
        columns=slots, lines=lines, bet=bet, values=symbol_value
    )

    # Print the winnings and the winning lines
    print(f"You won €{winnings}")
    print("You won on lines: ", *winning_lines)

    # Return the net gain or loss from the spin
    return winnings - total_bet


def main():
    """
    This is the main function that runs the slot machine game.
    It first asks the player to deposit money, then enters a game loop where the player can spin or quit.
    The player's balance is updated after each spin.
    When the player quits, the remaining balance is printed.

    Args:
        None

    Returns:
        None
    """

    # Ask the player to deposit money and store the amount in 'balance'
    balance = deposit()

    # Start an infinite loop for the game
    while True:
        # Print the current balance
        print(f"Current balance is €{balance}")

        # Ask the player if they want to spin or quit
        game = input("Press enter to spin (q to quit)")

        # If the player wants to quit, break the loop
        if game == "q":
            break

        # If the player wants to spin, run the 'spin' function and add the result to 'balance'
        elif game == "":
            balance += spin(balance)

    # Print the remaining balance when the game ends
    print(f"Balance left: ${balance}")


# Call the main function to start the game
main()