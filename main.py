from bank import Bank
from customer import Customer
from account import Account
from transaction import Transaction, TransactionType

def main():
    # Create a bank
    bank = Bank()

    # Create customers
    customer1 = Customer("John Doe")
    customer2 = Customer("Jane Smith")

    # Create accounts
    account1 = Account(1000)
    account2 = Account(500)

    # Add accounts to customers
    customer1.add_account(account1)
    customer2.add_account(account2)

    # Add customers to the bank
    bank.add_customer(customer1)
    bank.add_customer(customer2)

    # Create and process transactions
    transaction1 = Transaction(customer1, account1, TransactionType.WITHDRAWAL, 200)
    transaction2 = Transaction(customer2, account2, TransactionType.DEPOSIT, 300)

    bank.process_transaction(transaction1)
    bank.process_transaction(transaction2)

    # Display account balances
    print(f"Customer 1 Balance: ${account1.get_balance()}")
    print(f"Customer 2 Balance: ${account2.get_balance()}")

if __name__ == "__main__":
    main()
