account = {
    "name": "Faith",
    "balance": 50000
}

def account_menu():
    choice = 1
    while choice != 4:
        print(f"Hello {account['name']}")
        print("1 = Check Balnance")
        print("2 = deposit")
        print("3 = Withdraw")
        print("4 = Exit")
        choice = int(input("Choose an option: "))
        if choice == 1:
            print(f"Your balance is ₦{account['balance']}")
        elif choice == 2:
            deposit_amount = int(input("How much would you like to deposit? "))
            if deposit_amount > 0:
                account['balance'] += deposit_amount 
                print(f"Your new balnce is {account['balance']}")
            else:
                print("INVALID DEPOSIT AMOUNT")
        elif choice == 3:
            withdrawal_amount = int(input("How much would you like to withdraw? "))
            if withdrawal_amount > 0 and withdrawal_amount <= account['balance']:
                account['balance'] -= withdrawal_amount
                print(f"Your new balance is {account['balance']}")
            else:
                print("INSUFFICIENT FUNDS")
        elif choice == 4:
            print("Thank you for banking with us. Goodbye")
        else:
            print("INVALID OPTION. Please choose 1-4")
account_menu()