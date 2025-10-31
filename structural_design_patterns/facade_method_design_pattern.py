
from abc import ABC, abstractmethod


class Bank(ABC):
    @abstractmethod
    def transfer_money(self):
        pass


class SecurityService():
    def verify_user(self, user_id, password):
        print(f'Verifying user {user_id} ...')
        if password == '1234':
            print('Verification successful')
            return True
        print('Verification failed')    
        return False


class AccountService():
    def __init__(self):
        self.accounts = {"A123":9000, "B456": 3500}

    def has_sufficient_balance(self, account_id, amount):
        balance = self.accounts.get(account_id, 0)
        print(f'Checking balance for {account_id}: ${balance}')
        return balance >= amount 
    
    def debit(self, account_id, amount):
        self.accounts[account_id] -= amount
        print(f'Debited {amount} from {account_id}. New balance is: {self.accounts[account_id]}')

    def credit(self, account_id, amount):
        self.accounts[account_id] += amount
        print(f'Credited {amount} from {account_id}. New balance is: {self.accounts[account_id]}')    
    

class TransactionService():
    def execute_transfer(self, from_acc, to_acc, amount):
        print(f'Transferring {amount} from {from_acc} to {to_acc}...')
    
class NotificationService():
    def send(self, user_id, message):
        print(f'Message for {user_id}: {message} ')


class BankFacade():
    def __init__(self):
        self.security = SecurityService()
        self.account = AccountService()
        self.transaction = TransactionService()
        self.notification = NotificationService()

    def transfer_money(self, user_id, passw, from_acc, to_acc, amount):
        # Security check
        if not self.security.verify_user(user_id, passw):
            print('[BankFacade] Transfer failed: invalid credentials. \n')
            return 
        
        # Balance check
        if not self.account.has_sufficient_balance(from_acc, amount):
            print('[BankFacade] Transfer failed: amoun is greater than current balance. \n')
            return
        
        self.transaction.execute_transfer(from_acc, to_acc, amount)
        self.account.debit(from_acc, amount)
        self.account.credit(to_acc, amount)
        self.notification.send(user_id, f'Transfer of ${amount} from {from_acc} to {to_acc} is completed successfully.')

if __name__ == "__main__":
    bank = BankFacade()

    bank.transfer_money(
        user_id='userTest',
        passw='1234',
        from_acc='A123', 
        to_acc='B456', 
        amount=1000
    )

        


