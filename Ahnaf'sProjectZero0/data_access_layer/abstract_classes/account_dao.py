from abc import ABC, abstractmethod

from Entities.Accounts import Account


class AccountDAO(ABC):

    # create account
    @abstractmethod
    def create_account_id(self, account: Account) :
        pass

    # get account information
    @abstractmethod
    def view_account_balance(self, account_ID: int):
        pass

        

    @abstractmethod
    def delete_account_ID(self, account_ID):
        pass


    # get all accounts
    @abstractmethod
    def get_all_accounts(self) :
        pass

    
    @abstractmethod
    def get_all_customer_accounts(self, customer_id):
        pass
    
    
    
    
    
    @abstractmethod
    def deposit_into_account(self,account:Account):
        pass

    @abstractmethod
    def withdraw_from_account(self,account:Account):
        pass
 
    @abstractmethod
    def transfer_between_accounts(self,account):
        pass
