from customer import Customer
from transaction import Transaction

class Bank:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def process_transaction(self, transaction):
        # Add transaction processing logic here
        # For simplicity, this example does not include a full implementation
        pass
