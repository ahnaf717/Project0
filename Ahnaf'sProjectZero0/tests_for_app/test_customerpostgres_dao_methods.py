from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from Entities.Customers import Customer
customer_dao=CustomerPostgresDAO()

customer1=Customer(0,"customer","one",45,347666)
customer2=Customer(23,"customer","two",21,347912)
updated_customer2=Customer(23,"Ahnaf","updated",21,347912)
deleted_customer=Customer(0,"delete","customer",90,642)

def test_create_customer_sucess():
    created_customer=customer_dao.create_customer_entry(customer1)
    assert created_customer.customer_id !=0
    
    
def test_get_customer_success():
    get_customer=customer_dao.get_customer_information(11)
    assert get_customer.first_name == "customer" and get_customer.last_name == "six"
    
    
def test_get_all_customers_success():
    get_all_customers=customer_dao.get_all_customers_information()
    assert len(get_all_customers) >4
    
    
def test_update_customer_information_success():
    updated_customer=customer_dao.update_customer_information(updated_customer2)
    assert updated_customer2.last_name=="updated"
    
    
    
def test_delete_customer_information_success():
    customer_to_delete=customer_dao.create_customer_entry(deleted_customer)
    result=customer_dao.delete_customer_information(customer_to_delete.customer_id)
    assert result
    
    

    
