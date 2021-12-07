from custom_exceptions.duplicate_phone_number_exception import DuplicatePhoneNumberException
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from Entities.Customers import Customer
from service_layer.implementation_services.customer_postgres_service import CustomerPostgresSerivce

customer_dao=CustomerPostgresDAO()
customer_service=CustomerPostgresSerivce(customer_dao)

customer_with_duplicate_phone_number=Customer(0,"Duplicate","Customer",40,365)



def test_catch_duplicate_phone_number_for_create_method():
    try:
        customer_service.service_create_customer_entry(customer_with_duplicate_phone_number)
        assert False
    except DuplicatePhoneNumberException as e:
        assert str(e) == "Phone Number Is Already Taken. Please Enter A New One!"

def test_catch_duplicate_phone_number_for_update_method():
    try:
        customer_service.service_update_customer_information(customer_with_duplicate_phone_number)
        assert False
    except DuplicatePhoneNumberException as e:
        assert str(e) == "Phone Number Is Already Taken. Please Enter A New One!"

   
    

        
    