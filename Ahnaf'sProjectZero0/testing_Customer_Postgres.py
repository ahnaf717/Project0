from Entities.Customers import Customer
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO

adam=Customer("adam","smith",34,2,345)
ahnaf=Customer("ahnaf","chowdhury",25,4,347)
ryan=Customer("ryan","rock",27,0,348)
tom=Customer("ryan","rock",27,6,348)
obj1=CustomerPostgresDAO()
#obj1.create_customer_entry(adam)
obj1.create_customer_entry(tom)
#obj1.get_customer_information(5)
#obj1.create_customer_entry(ryan)


