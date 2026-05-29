from datetime import date, timedelta, datetime
import json

class Transaction:
    def __init__ (self, id, name, value, date, type):
        self.id = id
        self.name = name
        self.value = value
        self.date = date
        self.type = type

    def to_dict(self):
        transaction_json = {
            "id": self.id,
            "name": self.name,
            "value": self.value,
            "date": self.date,
            "type": self.type
        }
        return transaction_json


class System:
    def __init__ (self):
        self.transactions = []
        self.next_id = 0

    def add_transaction(self):
        transaction_name = input("Transaction Name: ").strip().title()
        while True:
            try:
                transaction_value = float(input("Transaction Value: "))
                break

            except ValueError:
                print("Invalid Input")

        transaction_date = str(date.today())
        print("'e': Expense, 's': Subscription, 'i': Income")
        while True:
            transaction_type = input("Transaction Type: ")
            if transaction_type not in ["e", "s", "i"]:
                print("Invalid Choice")
                continue
            else:
                break

        if transaction_type == "e":
            transaction_type = "Expense"
        elif transaction_type == "s":
            transaction_type = "Subscription"
        elif transaction_type == "i":
            transaction_type = "Income"

        new_transaction = Transaction(self.next_id, transaction_name, transaction_value, transaction_date, transaction_type)
        self.transactions.append(new_transaction)
        self.next_id += 1
        return self.transactions
    
    def delete_transaction(self, id):
        i = 0
        for transaction in self.transactions:
            if transaction.id == id:
                self.transactions.pop(i)
                
            else:
                i += 1
                continue
        
        return self.transactions
    
    def rename_transaction(self, id, rename):
        i = 0
        for transaction in self.transactions:
            if transaction.id == id:
                transaction = self.transactions[i]

            else:
                i += 1
                continue
        transaction.name = rename
        return self.transactions
    
    def save_transactions(self):
        jsontransactions = {}

        for transaction in self.transactions:
            jsontransactions[transaction.id] = transaction.to_dict()

        with open("finances.json", "w", encoding="utf-8") as file:
            json.dump(jsontransactions, file, indent = 4)

    def load_transactions(self):
        self.transactions = []

        try:
            with open("finances.json", "r", encoding="utf-8") as file:
                loaded_transactions = json.load(file)

            for transaction_data in loaded_transactions.values():
                loaded_transaction = Transaction(transaction_data["id"], transaction_data["name"], transaction_data["value"], transaction_data["date"], transaction_data["type"])

                self.transactions.append(loaded_transaction)      
    
        except FileNotFoundError:
            pass

        return self.transactions

    def calculate(self, info):
        if info == "gross_income":
            income_sum = 0
            for transaction in self.transactions:
                if transaction.type == "Income":
                    income_sum += transaction.value
                else:
                    continue

            return income_sum
        
        elif info == "gross_expense":
            expense_sum = 0
            for transaction in self.transactions:
                if transaction.type == "Expense" or transaction.type == "Subscription":
                    expense_sum += transaction.value
                else:
                    continue

            return expense_sum
        
        elif info == "net_income":
            income_sum = 0
            for transaction in self.transactions:
                if transaction.type == "Income":
                    income_sum += transaction.value
                else:
                    continue

            expense_sum = 0
            for transaction in self.transactions:
                if transaction.type == "Expense" or transaction.type == "Subscription":
                    expense_sum += transaction.value
                else:
                    continue

            net_profit = income_sum - expense_sum

            return net_profit

    
    def filter(self, type):
        if type == "i":
            incomes = {}
            for transaction in self.transactions:
                if transaction.type == "Income":
                    incomes[transaction.id] = transaction
                else:
                    continue

            return incomes

        elif type == "s":
            subscriptions = {}
            for transaction in self.transactions:
                if transaction.type == "Subscription":
                    subscriptions[transaction.id] = transaction
                else:
                    continue

            return subscriptions

        elif type == "e":
            expenses = {}
            for transaction in self.transactions:
                if transaction.type == "Expense":
                    expenses[transaction.id] = transaction
                else:
                    continue

            return expenses






