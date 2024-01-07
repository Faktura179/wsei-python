class BankAccount:
    def __init__(self, iban, currency, balance, owner):
        self.bank_name = "PB OKP"
        self.iban = iban
        self.currency = currency
        self.__balance = balance
        self.__owner = owner

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        self.__owner = owner

    def __str__(self):
        return f"Bank Account: {self.iban}, Currency: {self.currency}, Balance: {self.__balance}, Owner: {self.__owner}"

    def __len__(self):
        return self.__balance

    def __add__(self, other):
        if isinstance(other, BankAccount) and self.bank_name == other.bank_name and self.currency == other.currency and self.__owner == other.__owner:
            self.__balance += other.__balance
            other.__balance = 0
            return self
        else:
            raise ValueError("Nie można przelać pieniędzy pomiędzy tymi kontami")


account1 = BankAccount("1", "USD", 1000, "Jan Kowalski")
account2 = BankAccount("1", "USD", 2000, "Jan Kowalski")
account3 = BankAccount("2", "EUR", 1500, "Beata Nowak")

print(account1)
print(len(account1))

account1 += account2
print(account1)

print(account1.get_owner())
account1.set_owner("Jerzy Brzęczyszczykiewicz")
print(account1.get_owner())
