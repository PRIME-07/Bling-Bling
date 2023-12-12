import random

# max number of lines available to place bets
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 3,
    "B": 6,
    "C": 8,
    "D": 10,
    "$": 1
}


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


# main function
def main():
    balance = deposit()
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


main()
