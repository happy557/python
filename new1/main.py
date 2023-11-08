
import master

customers = []
account_num_counter = 1000

while True:
    print("\n1. Add Customer\n2. View Customers\n3. Deposit\n4. Withdraw\n5. Exit")
    choice = input("Enter your choice:")

    if choice == '1':
        master.add_customer(customers, account_num_counter)
    elif choice == '2':
        master.view_customers(customers)
    elif choice == '3':
        master.deposit(customers)
    elif choice == '4':
        master.withdraw(customers)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")