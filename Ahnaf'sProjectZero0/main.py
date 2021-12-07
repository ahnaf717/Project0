from flask import Flask, request, jsonify
from custom_exceptions.duplicate_phone_number_exception import DuplicatePhoneNumberException
from custom_exceptions.duplicate_account_number_exception import DuplicateAccountNumberException
from custom_exceptions.negative_Deposit_Amount_Exception import NegativeDepositAmountException
from custom_exceptions.withdrawl_exception import WithdrawlAccountException
from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from Entities.Customers import Customer
from Entities.Accounts import Account
from service_layer.implementation_services.account_service_imp import AccountServiceImp
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from service_layer.implementation_services.customer_postgres_service import CustomerPostgresSerivce
import logging
logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)

customer_dao = CustomerPostgresDAO()
customer_service = CustomerPostgresSerivce(customer_dao)
account_dao=AccountPostgresDAO()
account_service=AccountServiceImp(account_dao)

# create a customer
@app.post("/customer")
def create_customer_entry():
    try:
        customer_data = request.get_json()
        new_customer = Customer(
            customer_data["customerID"],
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["customerAge"],
            customer_data["phoneNumber"]
          
        )
        customer_to_return = customer_service.service_create_customer_entry(new_customer)
        customer_as_dictionary = customer_to_return.make_customer_dictionary()
        customer_as_json = jsonify(customer_as_dictionary)
        return customer_as_json
    except DuplicatePhoneNumberException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


# get a customer's information
@app.get("/customer/<customer_id>")
def get_customer_information(customer_id: str):
    result = customer_service.service_get_customer_information(int(customer_id))
    result_as_dictionary = result.make_customer_dictionary()
    result_as_json = jsonify(result_as_dictionary)
    return result_as_json

# update customer information
@app.patch("/customer/<customer_id>")
def update_customer_information(customer_id: str):
    try:
        customer_data = request.get_json()
        new_customer = Customer(
            int(customer_id),
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["customerAge"],
            customer_data["phoneNumber"]
            
        )
        customer_service.service_update_customer_information(new_customer)
        return "Customer updated successfully,the player info is now" 
    except DuplicatePhoneNumberException as e:
        return str(e)
       


# delete customer information
@app.delete("/customer/<customer_id>")
def delete_customer_information(customer_id: str):
    result = customer_service.service_delete_customer_information(int(customer_id))
    if result:
        return "Sorry To See You Go ,Customer with id {} was deleted successfully".format(customer_id)
    else:
        return "Something went wrong: customer with id {} was not deleted".format(customer_id)
    
# get all customer information
@app.get("/customer")
def get_all_customers_information():
    customers_as_customers = customer_service.service_get_all_customers_information()
    customers_as_dictionary = []
    for customers in customers_as_customers:
        dictionary_customer = customers.make_customer_dictionary()
        customers_as_dictionary.append(dictionary_customer)
    return jsonify(customers_as_dictionary)
   
#create a customer account 
@app.post("/account")
def create_account():
    try:
        account_info = request.get_json()
        new_account = Account(
            account_info["accountID"],
            account_info["accountNumber"],
            account_info["accountBalance"],
            account_info["customerID"]
        )
        created_account = account_service.service_create_account_id(new_account)
        created_account_as_dictionary = created_account.create_account_dictionary()
        return jsonify(created_account_as_dictionary)
    except DuplicateAccountNumberException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
  

#get a customer account      
@app.get("/account/<account_ID>")
def view_account_balance(account_ID: str):
    account = account_service.service_view_account_balance(int(account_ID))
    account_as_dictionary = account.create_account_dictionary()
    return jsonify(account_as_dictionary), 200

#get all customer account information
@app.get("/account")
def get_all_accounts():
    accounts = account_service.service_get_all_accounts()
    accounts_as_dictionaries = []
    for account in accounts:
        dictionary_account = account.create_account_dictionary()
        accounts_as_dictionaries.append(dictionary_account)
    return jsonify(accounts_as_dictionaries), 200


#get all customer's account
@app.get("/gets/<customer_id>")
def get_all_customer_account_information(customer_id):
    customer_accounts = account_service.service_get_all_customer_accounts(customer_id)
    accounts_as_dictionaries= []
    for account in customer_accounts:
        dictionary_account = account.create_account_dictionary()
        accounts_as_dictionaries.append(dictionary_account)
    return jsonify(accounts_as_dictionaries), 200

#delete customer information
@app.delete("/account/<account_ID>")
def delete_account(account_ID: str):
    try:
        result = account_service.service_delete_account_ID(int(account_ID))
        if result:
            return "Account with id {} was deleted successfully".format(account_ID)
    except:
        return "Something went wrong: Account with id {} was not deleted".format(account_ID)
    
#deposit into customer account    
@app.post("/account/<account_ID>/<deposit_amount>")
def deposit_into_account(account_ID, deposit_amount):
    try:
        result=account_service.service_deposit_into_account(int(account_ID),int(deposit_amount))
        if result:
            return "Thanks for Your Deposit"
    except NegativeDepositAmountException as e:
        exception_dictionary={"message":str(e)}
        exceptions_json=jsonify(exception_dictionary)
        return exceptions_json
        return str(e)

#withdraw from customer account    
@app.post("/withdraw/<account_ID>/<withdraw_amount>")
def withdraw_from_account(account_ID, withdraw_amount):
    try:
        result = account_service.service_withdraw_from_account(int(account_ID), int(withdraw_amount))
        if result:
            return "You Withdrawed Successfully"
    except WithdrawlAccountException as e:
     exception_dictionary = {"message": str(e)}
     exceptions_json = jsonify(exception_dictionary)
     return exceptions_json
     return str(e)
  
    
#transfer between customer accounts    
@app.post("/transfer/<account_ID_1>/<account_ID_2>/<transfer_amount>")
def transfer_between_accounts(account_ID_1,account_ID_2,transfer_amount):
    try:
        result = account_service.service_transfer_between_accounts(int(account_ID_1), int(account_ID_2), int(transfer_amount))
        if result:
            return "You successfully Transferred Balances"
    except WithdrawlAccountException as e:
        exception_dictionary = {"message": str(e)}
        exceptions_json = jsonify(exception_dictionary)
        return exceptions_json
        return str(e)


app.run()
