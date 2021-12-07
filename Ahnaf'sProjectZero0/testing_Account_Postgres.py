from Entities.Accounts import Account
from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO


ralph=Account(0,1222,300,11)
obj2=AccountPostgresDAO()
obj2.create_account_id(ralph)
#obj2.deposit_into_account(account1)

#obj2.get_all_accounts()


