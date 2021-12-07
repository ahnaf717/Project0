from abc import ABC, abstractmethod

from Entities.Customers import Customer


class CustomerService(ABC):

    @abstractmethod
    def service_create_customer_entry(self, customer: Customer):
        pass

    @abstractmethod
    def service_get_customer_information(self, customer_id):
        pass

    @abstractmethod
    def service_update_customer_information(self, customer: Customer):
        pass

    @abstractmethod
    def service_delete_customer_information(self, customer_id):
        pass

    @abstractmethod
    def service_get_all_customers_information(self) ->list[Customer]:
        pass

