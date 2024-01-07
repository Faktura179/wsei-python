class BankAccount:
    def __init__(self, iban, currency, balance, owner):
        self.bank_name = "PB OKP"
        self.iban = iban
        self.currency = currency
        self.__balance = balance
        self.__owner = owner

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    def __str__(self):
        return f"Bank Account: {self.iban}, Currency: {self.currency}, Balance: {self.balance}, Owner: {self.owner}"

    def __len__(self):
        return self.__balance

    def __add__(self, other):
        if isinstance(other, BankAccount) and self.bank_name == other.bank_name and self.currency == other.currency and self.__owner == other.__owner:
            self.balance += other.__balance
            other.balance = 0
            return self
        else:
            raise ValueError("Nie można przelać pieniędzy pomiędzy tymi kontami")
        
    @staticmethod
    def convert_currency(amount, exchange_rate):
        return amount * exchange_rate
        
account1 = BankAccount("1", "USD", 1000, "Jan Kowalski")
account2 = BankAccount("1", "USD", 2000, "Jan Kowalski")
account3 = BankAccount("2", "EUR", 1500, "Beata Nowak")

print(account1)
print(len(account1))

account1 += account2
print(account1)
print(len(account2))

print(account1.owner)
account1.owner = "Jerzy Brzęczyszczykiewicz"
print(account1.owner)

print(BankAccount.convert_currency(1000, 3.8))