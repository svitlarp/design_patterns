from abc import ABC, abstractmethod


# Abstract Products
class Account(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def get_balance(self):
        pass


class Card(ABC):
    @abstractmethod
    def get_card_info(self):
        pass


class Loan(ABC):
    def __init__(self, loan_amount):
        self.loan_amount = loan_amount

    @abstractmethod
    def get_loan_info(self):
        pass


# Concrete Products
# Account Products
class CurrentAcount(Account):
    def get_balance(self):
        print(f"Current Account Balance is {self.balance}")


class SavingAcount(Account):
    def get_balance(self):
        print(f"Saving Account Balance is {self.balance}")


class CreditAcount(Account):
    def get_balance(self):
        print(f"Credit Account Balance is {self.balance}")


# Cards Products
class DebitCard(Card):
    def get_card_info(self):
        print("[Card type] Debit")


class CreditCard(Card):
    def get_card_info(self):
        print("[Card type] Credit")


# Loan Products
class PersonalLoan(Loan):
    def get_loan_info(self):
        print(f"[Loan type] Personal. Loan Amount is {self.loan_amount}")


class MarginLoan(Loan):
    def get_loan_info(self):
        print(f"[Loan type] Margin. Loan Amount is {self.loan_amount}")


class EquipmentLoan(Loan):
    def get_loan_info(self):
        print(f"[Loan type] Equipment. Loan Amount is {self.loan_amount}")


# Abstract Factory
class BankFactory(ABC):
    @abstractmethod
    def create_account(self, balance):
        pass

    @abstractmethod
    def create_card(self):
        pass

    @abstractmethod
    def create_loan(self, loan_amount):
        pass


# Concrete Factories
class InvestmentBankFactory(BankFactory):
    def create_account(self, balance):
        return CreditAcount(balance)

    def create_card(self):
        return CreditCard()

    def create_loan(self, loan_amount):
        return MarginLoan(loan_amount)


class CommercialBankFactory(BankFactory):
    def create_account(self, balance):
        return CurrentAcount(balance)

    def create_card(self):
        return DebitCard()

    def create_loan(self, loan_amount):
        return EquipmentLoan(loan_amount)


class RetailBankFactory(BankFactory):
    def create_account(self, balance):
        return SavingAcount(balance)

    def create_card(self):
        return DebitCard()

    def create_loan(self, loan_amount):
        return PersonalLoan(loan_amount)


# Client Code
def main():

    print("Investment Bank Factory")
    investment_bank_factory = InvestmentBankFactory()
    investment_bank_account = investment_bank_factory.create_account(95800)
    investment_bank_card = investment_bank_factory.create_card()
    investment_bank_loan = investment_bank_factory.create_loan(30900)
    investment_bank_account.get_balance()
    investment_bank_card.get_card_info()
    investment_bank_loan.get_loan_info()

    print("Commercial Bank Factory")
    commercial_bank_factory = CommercialBankFactory()
    commercial_bank_account = commercial_bank_factory.create_account(10000000)
    commercial_bank_card = commercial_bank_factory.create_card()
    commercial_bank_loan = commercial_bank_factory.create_loan(3000000)
    commercial_bank_account.get_balance()
    commercial_bank_card.get_card_info()
    commercial_bank_loan.get_loan_info()

    print("Retail Bank Factory")
    retail_bank_factory = CommercialBankFactory()
    retail_bank_account = retail_bank_factory.create_account(4583.7)
    retail_bank_card = retail_bank_factory.create_card()
    retail_bank_loan = retail_bank_factory.create_loan(2381.4)
    retail_bank_account.get_balance()
    retail_bank_card.get_card_info()
    retail_bank_loan.get_loan_info()


if __name__ == "__main__":
    main()
