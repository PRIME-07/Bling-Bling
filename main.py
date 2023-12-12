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

deposit()
