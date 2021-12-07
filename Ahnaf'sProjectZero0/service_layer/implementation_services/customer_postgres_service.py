from Entities.Customers import Customer
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from service_layer.abstract_services.customer_service import CustomerService
from custom_exceptions.duplicate_phone_number_exception import DuplicatePhoneNumberException

class CustomerPostgresSerivce(CustomerService):
    def __init__(self,customer_dao:CustomerPostgresDAO):
        self.customer_dao=customer_dao

    def service_create_customer_entry(self, customer: Customer):
      customers=self.customer_dao.get_all_customers_information()
      for current_customer in customers:
          if current_customer.phone_number==customer.phone_number:
              raise DuplicatePhoneNumberException("Phone Number Is Already Taken. Please Enter A New One!")
      created_customer=self.customer_dao.create_customer_entry(customer)
      return created_customer
       

    def service_get_customer_information(self, customer_id):
        return self.customer_dao.get_customer_information(customer_id)

    def service_update_customer_information(self, customer: Customer):
        customers=self.customer_dao.get_all_customers_information()
        for current_customer in customers:
            if current_customer.phone_number==customer.phone_number:
                raise DuplicatePhoneNumberException("Phone Number Is Already Taken. Please Enter A New One!")
        updated_customer=self.customer_dao.update_customer_information(customer)
        return updated_customer

    def service_delete_customer_information(self, customer_id):
        return self.customer_dao.delete_customer_information(customer_id)

    def service_get_all_customers_information(self) -> list[Customer]:
        return self.customer_dao.get_all_customers_information()
