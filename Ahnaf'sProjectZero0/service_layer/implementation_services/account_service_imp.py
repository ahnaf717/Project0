from Entities.Accounts import Account
from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from service_layer.abstract_services.account_service import AccountService
from custom_exceptions.duplicate_account_number_exception import DuplicateAccountNumberException
from custom_exceptions.negative_Deposit_Amount_Exception import NegativeDepositAmountException
from custom_exceptions.withdrawl_exception import WithdrawlAccountException

class AccountServiceImp(AccountService):
    
    def __init__(self,account_dao):
        self.account_dao:AccountPostgresDAO=account_dao
        
        
    def service_create_account_id(self, account: Account):
        accounts=self.account_dao.get_all_accounts()
        for current_account in accounts:
            if current_account.account_number==account.account_number: 
                raise DuplicateAccountNumberException("Sorry,That Account Number is Already Taken!!! Please Choose A New Account Number")
        created_account=self.account_dao.create_account_id(account)    
        return created_account

    def service_view_account_balance(self, account_ID: int):
        return self.account_dao.view_account_balance(account_ID)

    def service_delete_account_ID(self, account_ID):
        return self.account_dao.delete_account_ID(account_ID)

    def service_get_all_accounts(self):
        return self.account_dao.get_all_accounts()
    
    
    def service_deposit_into_account(self,account_ID,deposit_amount:int):
        #make sure that deposit amount is greater than zero
        accounts=self.account_dao.get_all_accounts()
        for account in accounts:
            if account.account_ID==account_ID:
                if deposit_amount >= 0:
                    account.account_balance+=deposit_amount
                    return self.account_dao.deposit_into_account(account)
        else:
                raise NegativeDepositAmountException("Unsuccessful Deposit: No Negative deposit amounts allowed")

    def service_withdraw_from_account(self,account_ID,withdraw_amount:int):
        #make sure withdraw amount is less than account_balance 
        accounts=self.account_dao.get_all_accounts()
        for account in accounts:
            if account.account_ID == account_ID:
                if withdraw_amount <account.account_balance and withdraw_amount>=0:
                    account.account_balance -= withdraw_amount
                    return self.account_dao.withdraw_from_account(account)
        else:
             raise WithdrawlAccountException("Unsuccessful Withdrawl: Please Make Sure You Enough Money In Your Account or You Entered A Positive Withdrawl Amount")
    
    def service_transfer_between_accounts(self, account_ID_1, account_ID_2, transfer_amount:int):
       for account_1 in self.account_dao.get_all_accounts():
            for account_2 in self.account_dao.get_all_accounts():
                if account_1.account_ID == account_ID_1:
                    if account_2.account_ID==account_ID_2:
                        if transfer_amount<account_1.account_balance:
                            account_1.account_balance-=transfer_amount
                            self.account_dao.withdraw_from_account(account_1)
                            account_2.account_balance += transfer_amount
                            self.account_dao.deposit_into_account(account_2)
                            return True
    
                        else:
                            raise WithdrawlAccountException("You Don't Have Enough Money For a Transfer!!")
                            
        
          
                            
                          
                            
                            
                         
        
                   
                