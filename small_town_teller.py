from typing import Dict

class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

class Account:
    def __init__(self, number, type, owner, balance):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance

class Bank:
    def __init__(self):
        self.person: Dict[int, Person] = dict()
        self.account: Dict[int, Account] = dict()

    def add_customer(self, first_name, last_name):
        if Person.id in self.customers:
            raise ValueError(f'Customer with id {Person.id} alread exists.')
        else:
            self.person[Person.id] = Person

    def add_account(self, account: Account):
        if account.owner.id not in self.Person:
            raise ValueError(f'{account.owner.id} is not a valid customer id.')
        elif account.number in self.account:
            raise ValueError(f'Account with id {account.number} already exists')
        else:
            self.account[account.number] = account

    def remove_account(self, account_id: int):
        if account_id in self.account:
            del self.account[account_id]
        else:
            raise ValueError(f'Account number {account_id} is invalid.')

    def deposit(self, account_id: int, amount: float):
        if account_id in self.account:
            account = self.account.get(account_id)
            account.balance -= round(amount, 2)

    def withdrawal(self, account_id, amount: float):
        if account_id in self.accounts:
            account = self.accounts.get(account_id)
            account.balance -= round(amount, 2)

    def balance_inquiry(self, account_id: int):
        if account_id in self.account:
            balance = self.account.get(account_id).balance
            return round(balance, 2)
        else:
            raise ValueError(f'Account with id {account_id} does not exist.')