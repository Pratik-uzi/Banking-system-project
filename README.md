Synopsis:(my first project)

This Python code implements a simple banking application with features such as creating accounts, depositing money, withdrawing money, checking individual account details, and checking master account details.

The program begins with a menu-driven interface (selection()) where users can choose from various options like creating an account, depositing money, withdrawing money, checking individual account details, or checking master account details.

Create Account (create_acc()): Allows users to create a new bank account by entering personal details like name, father's name,
date of birth, address, gender, phone number, and initial balance. It generates a random account number and inserts the details into a MySQL database table named acc_details.

Deposit (deposit()): Enables users to deposit money into their account. It prompts users to enter their account number and the 
amount they wish to deposit. It updates the balance in the database accordingly and logs the transaction in the transaction_details table.

Withdraw (withdraw()): Allows users to withdraw money from their account. Users are prompted to enter their account number and 
the amount they want to withdraw. It checks if the withdrawal amount is valid (ensuring the balance doesn't 
fall below a minimum threshold) and updates the balance and transaction records accordingly.

Check Individual Account Details (check_individual()): Allows users to check their individual account details. Users provide their
account number and can choose to either check their current balance or view their transaction history.

Check Master Account Details (check_master()): Provides a summary of all account details stored in the database. It fetches all
records from the acc_details table and displays them in a tabular format.

The program continuously prompts the user if they want to perform another operation after each transaction until the user decides
to exit.




