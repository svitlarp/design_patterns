from abc import ABC, abstractmethod


# Abstract Product
class Account(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def get_balance(self):
        pass


# Concrete Products
class CurrentAcount(Account):
    def get_balance(self):
        print(f"Current Account Balance is {self.balance}")


class SavingAcount(Account):
    def get_balance(self):
        print(f"Saving Account Balance is {self.balance}")


class CreditAcount(Account):
    def get_balance(self):
        print(f"Credit Account Balance is {self.balance}")


# Abstract Factory
class AccountFactory(ABC):
    @abstractmethod
    def create_account(self, balance):
        pass


# Concrete Factories
class CurrentAccountFactory(AccountFactory):
    def create_account(self, balance):
        return CurrentAcount(balance)


class SavingAccountFactory(AccountFactory):
    def create_account(self, balance):
        return SavingAcount(balance)


class CreditAccountFactory(AccountFactory):
    def create_account(self, balance):
        return CreditAcount(balance)


# Client Code
def main():
    current_account_factory = CurrentAccountFactory()
    current_account = current_account_factory.create_account(100)
    current_account.get_balance()

    saving_account_factory = SavingAccountFactory()
    saving_account = saving_account_factory.create_account(12000)
    saving_account.get_balance()

    credit_account_factory = CreditAccountFactory()
    creadit_account = credit_account_factory.create_account(500)
    creadit_account.get_balance()


if __name__ == "__main__":
    main()
