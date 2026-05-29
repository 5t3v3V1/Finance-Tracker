from datetime import date, timedelta, datetime
import json

class Transaction:
    def __init__ (self, name, value, date, type):
        self.name = name
        self.value = value
        self.date = date
        self.type = type

    def to_dict(self):
        transaction_json = {
            "name": self.name,
            "value": self.value,
            "date": self.date,
            "type": self.type
        }
        return transaction_json


class System:
    def __init__ (self):
        self.transactions = []

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

        new_transaction = Transaction(transaction_name, transaction_value, transaction_date, transaction_type)
        self.transactions.append(new_transaction)
        return self.transactions
    
    def delete_transaction(self, index):
        self.transactions.pop(index)
        return self.transactions
    
    def rename_transaction(self, index, rename):
        transaction = self.transactions[index]
        transaction.name = rename
        return self.transactions
    
    def save_transactions(self):
        jsontransactions = {}
        i = 0

        for transactions in self.transactions:
            jsontransactions[i] = transactions.to_dict()
            i += 1

        with open("finances.json", "w", encoding="utf-8") as file:
            json.dump(jsontransactions, file, indent = 4)

    def load_transactions(self):
        self.transactions = []

        try:
            with open("finances.json", "r", encoding="utf-8") as file:
                loaded_transactions = json.load(file)

            for transaction_data in loaded_transactions.values():
                loaded_transaction = Transaction(transaction_data["name"], transaction_data["value"], transaction_data["date"], transaction_data["type"])

                self.transactions.append(loaded_transaction)      
    
        except FileNotFoundError:
            pass

        return self.transactions

    def calculate(self, info):
        if info == "gross_profit":
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
        
        elif info == "net_profit":
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
            for index, transaction in enumerate(self.transactions):
                if transaction.type == "Income":
                    incomes[index] = transaction
                else:
                    continue

            return incomes

        elif type == "s":
            subscriptions = {}
            for index, transaction in enumerate(self.transactions):
                if transaction.type == "Subscription":
                    subscriptions[index] = transaction
                else:
                    continue

            return subscriptions

        elif type == "e":
            expenses = {}
            for index, transaction in enumerate(self.transactions):
                if transaction.type == "Expense":
                    expenses[index] = transaction
                else:
                    continue

            return expenses






