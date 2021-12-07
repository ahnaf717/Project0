from abc import ABC, abstractmethod

from Entities.Accounts import Account


class AccountService(ABC):

    # create account
    @abstractmethod
    def service_create_account_id(self, account: Account):
        pass

    # get account information
    @abstractmethod
    def service_view_account_balance(self, account_ID: int):
        pass

    @abstractmethod
    def service_delete_account_ID(self, account_ID):
        pass

    # get all accounts
    @abstractmethod
    def service_get_all_accounts(self):
        pass
    
      @abstractmethod
    def service_get_all_customer_accounts(self,customer_id):
        pass

    @abstractmethod
    def service_deposit_into_account(self,account:Account):
        pass

    @abstractmethod
    def service_withdraw_from_account(self,account:Account):
        pass
    
    @abstractmethod
    def service_transfer_between_accounts(self,account:Account):
        pass
