class Customer:
    
    def __init__(self, customer_id:int, first_name:str, last_name:str,customer_age:int, phone_number:int
                 ):
        self.customer_id = customer_id
        self.first_name=first_name
        self.last_name=last_name
        self.customer_age=customer_age
        self.phone_number=phone_number
 
        
        
    def make_customer_dictionary(self):
        return {
            "customerID": self.customer_id,
            "firstName":self.first_name,
            "lastName": self.last_name,
            "customerAge":self.customer_age,
            "phoneNumber":self.phone_number
         
            
        }