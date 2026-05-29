from classes import System, Transaction
from datetime import date

tracker = System()
tracker.load_transactions()

def view_transactions(system):
    print("-" * 40)

    for transaction in system.transactions:
        print(f"{transaction.id}. {transaction.name}, £{transaction.value}, {transaction.date}, {transaction.type}")

    print("-" * 40)

def filter(type):
    if type == "e":
        expenses = tracker.filter(type)
        print("-" * 40)

        for id, transaction in expenses.items():
            print(f"{id}. {transaction.name}, £{transaction.value}, {transaction.date}, {transaction.type}")

        print("-" * 40)
        
    elif type == "s":
        subscriptions = tracker.filter(type)
        print("-" * 40)

        for id, transaction in subscriptions.items():
            print(f"{id}. {transaction.name}, £{transaction.value}, {transaction.date}, {transaction.type}")

        print("-" * 40)
            
    elif type == "i":
        incomes = tracker.filter(type)
        print("-" * 40)

        for id, transaction in incomes.items():
            print(f"{id}. {transaction.name}, £{transaction.value}, {transaction.date}, {transaction.type}")
    
        print("-" * 40)

def timefilter(timeamount):
    timefilter_transactions = tracker.filter_by_time(timeamount)
    timesummary_expenses, timesummary_income, timesummary_netincome = tracker.summaries(timeamount)
    print("-" * 40)

    print(f"Net Income: £{timesummary_netincome}")
    print(f"Gross Income: £{timesummary_income}")
    print(f"Gross Expense: £{timesummary_expenses}")

    print("-" * 40)

    for transaction in timefilter_transactions:
        print(f"{transaction.id}. {transaction.name}, £{transaction.value}, {transaction.date}, {transaction.type}")
        
    print("-" * 40)

def searchresults(search):
    searchfilter_transactions = tracker.search(search)
    print("-" * 40)

    for transaction in searchfilter_transactions:
        print(f"{transaction.id}. {transaction.name}, £{transaction.value}, {transaction.date}, {transaction.type}")
    
    print("-" * 40)

while True:
    
    print("1. View Transactions")
    print("2. Add Transaction")
    print("3. Delete Transaction")
    print("4. Rename Transaction")
    print("5. Filter By Type")
    print("6. Filter By Timeframe")
    print("7. Search")
    print("8. Exit")
    
    gross_expense = str(tracker.calculate("gross_expense"))
    gross_income = str(tracker.calculate("gross_income"))
    net_income = str(tracker.calculate("net_income"))

    print(f"Net Income: £{net_income}")
    print(f"Gross Income: £{gross_income}")
    print(f"Gross Expense: £{gross_expense}")

    choice = input("\nChoose Option: ")

    if choice == "1":
        view_transactions(tracker)

    elif choice == "2":
        tracker.add_transaction()
        tracker.save_transactions()

    elif choice == "3":
        tracker.delete_transaction(int(input("Choose Transaction: ")))
        tracker.save_transactions()

    elif choice == "4":
        while True:
            try:
                id = int(input("Choose Transaction: "))
                break

            except ValueError:
                print("Invalid Choice")

        new_name = input("New Name: ").strip().title()
        tracker.rename_transaction(id, new_name)

    elif choice == "5":
        print("'e': Expense, 's': Subscription, 'i': Income")
        type = input("Filter By Type: ")
        filter(type)

    elif choice == "6":
        while True:
            try:
                timeamount = int(input("Choose Timeframe: "))
                break

            except ValueError:
                print("Invalid Input")

        timefilter(timeamount)

    elif choice == "7":
            search = input("Search: ")
            searchresults(search)

    elif choice == "8":
        tracker.save_transactions()
        break

    else:
        print("Invalid Choice")