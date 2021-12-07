from custom_exceptions.duplicate_account_number_exception import DuplicateAccountNumberException
from custom_exceptions.negative_Deposit_Amount_Exception import NegativeDepositAmountException
from custom_exceptions.withdrawl_exception import WithdrawlAccountException
from Entities.Accounts import Account
from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from service_layer.implementation_services.account_service_imp import AccountServiceImp

account_dao=AccountPostgresDAO()
account_service=AccountServiceImp(account_dao)

duplicate_account_number=Account(0,5239,200,21)



def test_catch_duplicate_account_number():
    try:
        account_service.service_create_account_id(duplicate_account_number)
        assert False
    except DuplicateAccountNumberException as e:
        assert str(e) == "Sorry,That Account Number is Already Taken!!! Please Choose A New Account Number"
    


def test_catch_negative_deposit():
    try:
        account_service.service_deposit_into_account(20,-20)
        assert False
    except NegativeDepositAmountException as e:
        assert str(e) == "Unsuccessful Deposit: No Negative deposit amounts allowed"
        

def test_catch_withdrawl_exceeds():
    try:
        account_service.service_withdraw_from_account(20,-500)
        assert False
    except WithdrawlAccountException as e:
        assert str(e) == "Unsuccessful Withdrawl: Please Make Sure You Enough Money In Your Account or You Entered A Positive Withdrawl Amount"
        
        
def test_catch_transfer_exceeds():
    try:
        account_service.service_transfer_between_accounts(6,23,200)
        assert False
    except WithdrawlAccountException as e:
        assert str(e) == "You Don't Have Enough Money For a Transfer!!"
    
        
        
        
