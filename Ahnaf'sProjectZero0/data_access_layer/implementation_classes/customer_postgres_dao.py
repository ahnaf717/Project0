from Entities.Customers import Customer
from data_access_layer.abstract_classes.customer_dao import CustomerDAO
from Utilities.database_connection import connection


class CustomerPostgresDAO(CustomerDAO):
    def create_customer_entry(self, customer: Customer):
        sql="insert into customer values (default,%s,%s,%s,%s) returning customer_id"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name,customer.last_name,customer.customer_age , customer.phone_number))
        connection.commit()
        generated_customer_id = cursor.fetchone()[0]
        customer.customer_id = generated_customer_id
        return customer

    def get_customer_information(self, customer_id):
        sql="select * from customer where customer_id =%s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        customer_record = cursor.fetchone()
        customer = Customer(*customer_record)
        return customer


    def update_customer_information(self, customer: Customer):
        sql = "update customer set first_name = %s, last_name = %s, customer_age = %s, phone_number = %s where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql,( customer.first_name, customer.last_name, customer.customer_age, customer.phone_number, customer.customer_id ))
        connection.commit()
        return customer

    def delete_customer_information(self, customer_id):
        sql = "delete from customer where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        return True

    def get_all_customers_information(self) -> list[Customer]:
        sql = "select * from customer"
        cursor = connection.cursor()
        cursor.execute(sql)
        customer_records = cursor.fetchall()
        customer_list = []
        for customer in customer_records:
            customer_list.append(Customer(*customer))
        return customer_list
