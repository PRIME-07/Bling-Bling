# max number of lines available to place bets
MAX_LINES = 3


# takes input for deposit amount
def deposit():
    while True:
        amount = input("Enter amount to deposit: ")
        if amount.lstrip("-").isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
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

# main function
def main():
    balance = deposit()
    lines = get_number_of_lines()
    print("Deposit amount = Rs.", end="")
    print(balance)
    print("Number of lines = ", end="")
    print(lines)

main()

