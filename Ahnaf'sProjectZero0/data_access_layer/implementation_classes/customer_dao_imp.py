from Entities.Customers import Customer
from data_access_layer.abstract_classes.customer_dao import CustomerDAO

customer1 = Customer("Ahnaf", "Chowdhury", 27, 1,345)
customer2 = Customer("Mohammed", "Chowdhury", 59, 2,4567)


class CustomerDAOImp(CustomerDAO):
    customer_list = [customer1]
    customer_id_generator = 3
    

    def create_customer_entry(self, customer: Customer):
        customer.customer_id = CustomerDAOImp.customer_id_generator
        CustomerDAOImp.customer_id_generator += 1
        CustomerDAOImp.customer_list.append(customer)
        return customer

    def get_customer_information(self, customer_id):
        for customer in CustomerDAOImp.customer_list:
            if customer.customer_id == customer_id:
                return customer

    def update_customer_information(self, customer: Customer):
        for customer_in_list in CustomerDAOImp.customer_list:
            if customer_in_list.customer_id == customer.customer_id:
                index = CustomerDAOImp.customer_list.index(customer_in_list)
                CustomerDAOImp.customer_list[index] = customer
                return customer

    def delete_customer_information(self, customer_id):
        for customer_in_list in CustomerDAOImp.customer_list:
            if customer_in_list.customer_id == customer_id:
                index = CustomerDAOImp.customer_list.index(customer_in_list)
                del CustomerDAOImp.customer_list[index]
                return True

    def get_all_customers_information(self) -> list[Customer]:
        return CustomerDAOImp.customer_list

  