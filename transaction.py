class Transaction:
    def __init__(self, customer, account, transaction_type, amount):
        self.customer = customer
        self.account = account
        self.transaction_type = transaction_type
        self.amount = amount
