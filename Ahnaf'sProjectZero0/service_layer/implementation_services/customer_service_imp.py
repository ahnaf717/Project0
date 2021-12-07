from Entities.Customers import Customer
from data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from service_layer.abstract_services.customer_service import CustomerService
from custom_exceptions.duplicate_phone_number_exception import DuplicatePhoneNumberException



class CustomerServiceImp(CustomerService):
    def __init__(self,customer_dao):
        self.customer_dao:CustomerDAOImp=customer_dao

    
    def service_create_customer_entry(self, customer: Customer):
        return self.customer_dao.create_customer_entry(customer)

    def service_get_customer_information(self, customer_id):
        return self.customer_dao.get_customer_information(customer_id)


    def service_update_customer_information(self, customer: Customer):
        return self.customer_dao.update_customer_information(customer)


    def service_delete_customer_information(self, customer_id):
        return self.customer_dao.delete_customer_information(customer_id)

    
    def service_get_all_customers_information(self) -> list[Customer]:
        return self.customer_dao.get_all_customers_information()
    
    