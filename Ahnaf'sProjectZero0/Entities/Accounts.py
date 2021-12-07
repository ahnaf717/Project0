class Account:
    
        def __init__(self, account_ID: int, account_number:int, account_balance:int,customer_id:int):
            self.account_ID = account_ID
            self.account_number=account_number
            self.account_balance=account_balance
            self.customer_id=customer_id

        def __str__(self):
            return "Account_ID: {}, Account_Balance: {}, Customer_ID: {}".format(self.account_ID, self.account_balance,self.customer_id)

        def create_account_dictionary(self):
            return {
                "customerID":self.customer_id,
                "accountID": self.account_ID,
                "accountBalance": self.account_balance,
                "accountNumber": self.account_number
                
            }
    