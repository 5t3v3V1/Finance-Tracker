from classes import System, Transaction
from datetime import date

tracker = System()
tracker.load_transactions()

def view_transactions(system):
    print("\n")

    for index, transaction in enumerate(system.transactions):
        print(f"{index}. {transaction.name}, £{transaction.value}, {transaction.date}, {transaction.type}")

while True:
    
    print("1. View Transactions")
    print("2. Add Transaction")
    print("3. Delete Transaction")
    print("4. Rename Transaction")
    print("5. Filter")
    print("6. Exit")
    
    gross_expense = str(tracker.calculate_gross_expense())
    gross_profit = str(tracker.calculate_gross_profit())
    net_profit = str(tracker.calculate_net_profit())

    print(f"Net Profit: £{net_profit}")
    print(f"Gross Profit: £{gross_profit}")
    print(f"Gross Expense: £{gross_expense}")

    choice = input("\nChoose Option: ")

    if choice == "1":
        view_transactions(tracker)

    elif choice == "2":
        tracker.add_transaction()

    elif choice == "3":
        tracker.delete_transaction(int(input("Choose Habit: ")))

    elif choice == "4":
        index = int(input("Choose Habit: "))
        new_name = input("New Name: ").strip().title()
        tracker.rename_transaction(index, new_name)

    elif choice == "5":
        print("'e': Expense, 's': Subscription, 'i': Income")
        type = input("Filter By Type: ")
        if type == "e":
            expenses = tracker.filter_by_expense()
            for index, transaction in expenses.items():
                print(f"{index}. {transaction.name}, £{transaction.value}, {transaction.date}, {transaction.type}")
        
        elif type == "s":
            subscriptions = tracker.filter_by_subscription()
            for index, transaction in subscriptions.items():
                print(f"{index}. {transaction.name}, £{transaction.value}, {transaction.date}, {transaction.type}")
            
        elif type == "i":
            incomes = tracker.filter_by_income()
            for index, transaction in incomes.items():
                print(f"{index}. {transaction.name}, £{transaction.value}, {transaction.date}, {transaction.type}")

    elif choice == "6":
        tracker.save_transactions()
        break

    else:
        print("Invalid Choice")