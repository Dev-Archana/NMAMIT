pin = 1234
balance = 1000.0  

def validate_pin():
    entered_pin = int(input("Enter your PIN: "))
    if entered_pin == pin:
        return True
    else:
        print("Incorrect PIN")
        return False

def Deposit():
    global balance
    if validate_pin():
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid Amount. Must be greater than 0.")
        else:
            balance += amount
            print("Amount Deposited Successfully")
            print(f"Deposited Amount: {amount}")
            print(f"Updated Balance: {balance}")

def Withdraw():
    global balance
    if validate_pin():
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid Amount. Must be greater than 0.")
        elif amount > balance:
            print("Insufficient Balance")
        else:
            balance -= amount
            print("Amount Withdrawn Successfully")
            print(f"Withdrawn Amount: {amount}")
            print(f"Remaining Balance: {balance}")

def CheckBalance():#called method
    if validate_pin():
        print(f"Your current balance is: {balance}")

def main():
    while True:
        print("\nWelcome to the ATM")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            Deposit()
        elif choice == '2':
            Withdraw()
        elif choice == '3':
            CheckBalance() #calling method
        elif choice == '4':
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

main()
