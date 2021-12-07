from Utilities.database_connection import connection
from data_access_layer.abstract_classes.account_dao import AccountDAO
from Entities.Accounts import Account

class AccountPostgresDAO(AccountDAO):


    def create_account_id(self, account: Account):
        sql = "insert into account values(default,%s,%s,%s) returning account_ID"
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_number, account.account_balance, account.customer_id))
        connection.commit()
        generated_account_ID = cursor.fetchone()[0]
        account.account_ID = generated_account_ID
        return account

    def view_account_balance(self, account_ID: int):
        sql = "select * from account where account_ID =%s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_ID])
        account_record = cursor.fetchone()
        account = Account(*account_record)
        return account
        

    def delete_account_ID(self, account_ID):
        sql = "delete from account where account_ID = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_ID])
        connection.commit()
        return True

    def get_all_accounts(self):
        sql = "select * from account"
        cursor = connection.cursor()
        cursor.execute(sql)
        account_records = cursor.fetchall()
        accounts = []
        for account in account_records:
            accounts.append(Account(*account))
        return accounts

    def deposit_into_account(self, account: Account):
        sql="update account set account_balance =%s where account_ID=%s"
        cursor=connection.cursor()
        cursor.execute(sql, (account.account_balance,account.account_ID))
        connection.commit()
        return account

    def withdraw_from_account(self, account: Account):
        sql = "update account set account_balance =%s where account_ID=%s"
        cursor = connection.cursor()
        cursor.execute(sql,(account.account_balance,account.account_ID))
        connection.commit()
        return account

    def transfer_between_accounts(self, account:Account,account1:Account):
        sql = "update account set account_balance =%s where account_ID in (%s,%s)"
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_balance, account.account_ID, account1.account_ID))
        connection.commit()
        return True
        