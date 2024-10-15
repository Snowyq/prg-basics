###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    entered_pin = input("Enter Password: ")

    if entered_pin != pin:
        print('You entered wrong pin')
        continue

    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("5. change PIN")

    choice = input("Choose an option (1-5): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    elif choice == '5':
        is_pin_changed = False
        while not is_pin_changed:
            new_pin = input("Enter new PIN: ")
            is_valid = False
            if len(new_pin) == 4:
                for char in new_pin:
                    if  char.isdigit():
                        is_valid = True
            if not is_valid:
                print("PIN should contain only 4 digits")
            if is_valid:
                pin = new_pin
                is_pin_changed = True
            
    else:
        print("Invalid option. Please try again.")
