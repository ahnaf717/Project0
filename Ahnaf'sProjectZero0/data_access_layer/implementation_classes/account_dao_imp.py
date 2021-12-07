from Entities.Accounts import Account
from data_access_layer.abstract_classes.account_dao import AccountDAO


class AccountDAOImp(AccountDAO):
    account_ID_generator = 5225
    account_list=[]
    def create_account_id(self, account: Account):
        account.account_ID=AccountDAOImp.account_ID_generator
        AccountDAOImp.account_ID_generator +=1
        AccountDAOImp.account_list.append(account)
        return account

    def view_account_balance(self, account_ID: int):
        for account in AccountDAOImp.account_list:
            if account.account_ID==account_ID:
                return account
                

    def delete_account_ID(self, account_ID):
        for account in AccountDAOImp.account_list:
            if account.account_ID==account_ID:
                index=AccountDAOImp.account_list.index(account)
                del AccountDAOImp.account_list[index]
                return True
                

    def get_all_accounts(self):
        return AccountDAOImp.account_list

    
    def deposit_into_account(self, account: Account):
        for current_account in AccountDAOImp.account_list:
            if current_account.account_ID==account.account_ID:
                index=AccountDAOImp.account_list.index(current_account)
                AccountDAOImp.account_list[index]=account
                return account

    
    def withdraw_from_account(self, account: Account):
        for current_account in AccountDAOImp.account_list:
            if current_account.account_ID==account.account_ID:
                index=AccountDAOImp.account_list.index(current_account)
                AccountDAOImp.account_list[index]=account
                return account

    def transfer_between_accounts(self, account_ID_1:Account,account_ID_2:Account):
        for current_account in AccountDAOImp.account_list:
            if current_account.account_ID == account_ID_1:
                index = AccountDAOImp.account_list.index(current_account)
                AccountDAOImp.account_list[index] = account_ID_1
    
        for current_account in AccountDAOImp.account_list:
            if current_account.account_ID == account_ID_2:
                index = AccountDAOImp.account_list.index(current_account)
                AccountDAOImp.account_list[index] = account_ID_2
                return True


            
            