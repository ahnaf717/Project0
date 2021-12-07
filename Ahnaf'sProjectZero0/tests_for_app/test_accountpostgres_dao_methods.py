from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from Entities.Accounts import Account
account_dao=AccountPostgresDAO()

account1=Account(0,7977,1500,16)

account2=Account(1,5239,1500,10)
account2_after_deposit=Account(1,5239,2000,10)

account3=Account(20,5000,100,17)
account3_after_withdrawal=Account(20,5000,50,17)

account4=Account(3,7000,2000,15)
account4_after_transfer=Account(3,7000,2500,15)

account5=Account(43,4000,3000,15)
account5_after_transfer=Account(43,4000,3500,15)



def test_create_account_success():
    created_account=account_dao.create_account_id(account1)
    assert created_account.account_ID !=0
    
    
def test_get_accountID_success():
    retrieved_account=account_dao.view_account_balance(6)
    assert retrieved_account.account_balance==100
    
def test_get_all_accounts_success():
    get_all_accounts=account_dao.get_all_accounts()
    assert len(get_all_accounts) >=3
    
    
def test_delete_account_success():
    account_dao.delete_account_ID(40)
    assert True
    
    
def test_get_all_customer_accounts():
    accounts=account_dao.get_all_customer_accounts(39)
    assert len(accounts) >=1
    
    
def test_deposit_account_success():
    deposited_account=account_dao.deposit_into_account(account2)
    assert deposited_account.account_balance==account2.account_balance
    
    
def test_withdraw_account_success():
    withdrawed_account=account_dao.withdraw_from_account(account3)
    assert withdrawed_account.account_balance==account3.account_balance
    
    
def test_transfer_balance_success():
    result=account_dao.transfer_between_accounts(account4,account5)
    assert result==True
    
    
    

