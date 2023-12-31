import random

# max number of lines available to place bets
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 6,
    "B": 12,
    "C": 16,
    "D": 20,
    "$": 3
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "$": 10
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(lines + 1)
    return winnings, winnings_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


# takes input for deposit amount
def deposit():
    while True:
        amount = input("Enter amount to deposit: $")
        if amount.lstrip("-").isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than $0.")
        else:
            print("Enter valid amount")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to place bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
        else:
            print("Please pick number of lines.")
    return lines


def get_bet():
    while True:
        amount = input("Enter amount to bet on each line: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter valid amount")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet <= balance:
            print(f"you are betting ${balance} on {lines} lines. Total bet placed is ${total_bet}")
            break
        else:
            extra = total_bet - balance
            print(f"Not sufficient balance. Your bet exceeds account balance by {extra}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet


# main function
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance} ")
        answer = input("Press A key to add balance, press ENTER key to play. Press Q key to quit.")
        if answer == "a":
            add_bal = int(input("Enter amount to add to balance: $"))
            balance += add_bal
            print(f"Current balance is {balance}")
        if answer == "q":
            print("Game ended! Thanks for playing!")
            break
        balance += spin(balance)
    print(f"You are left with ${balance}")


main()
