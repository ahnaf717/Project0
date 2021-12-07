from abc import ABC, abstractmethod

from Entities.Customers import Customer


class CustomerDAO(ABC):

    
    @abstractmethod
    def create_customer_entry(self, customer: Customer):
        pass
  
    @abstractmethod
    def get_customer_information(self, customer_id):
        pass
    

    
    @abstractmethod
    def update_customer_information(self, customer: Customer):
        pass

    @abstractmethod
    def delete_customer_information(self, customer_id):
        pass

    @abstractmethod
    def get_all_customers_information(self) -> list[Customer]:
        pass
    
    
    
   