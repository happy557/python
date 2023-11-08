def add_customer(customers, account_num_counter):
    name = input("Enter customer name: ")
    age = int(input("Enter customer age: "))
    contact_number = input("Enter contact number:")
    account_number = str(account_num_counter)
    account_num_counter += 1

    new_customer = {
        "name": name,
        "age": age,
        "contact_number": contact_number,
        "account_number": account_number,
        "balance": 0
    }
    customers.append(new_customer)
    print("Customer added successfully!")

def view_customers(customers):
    print("\nCustomers list")
    search_option = input("Search by name (N) or account number (A):").upper()
    if search_option == 'N':
        search_name = input("Customer name:")
        found = False
        for customer in customers:
            if customer["name"] == search_name:
                print_customer_details(customer)
                found = True
        if not found:
            print("Customer not found")
    elif search_option == 'A':
        search_account_number = input("Customer account number:")
        found = False
        for customer in customers:
            if customer["account_number"] == search_account_number:
                print_customer_details(customer)
                found = True
        if not found:
            print("Customer not found")
    else:
        print("Invalid search option")

def print_customer_details(customer):
    print("\nName: " + customer['name'])
    print("Age: " + str(customer['age']))
    print("Contact: " + customer['contact_number'])
    print("Account Number: " + customer['account_number'])
    print("Balance: " + str(customer['balance']))

def deposit(customers):
    account_number = input("Enter account number:")
    amount = float(input("Enter deposit amount:"))
    for customer in customers:
        if customer["account_number"] == account_number:
            customer["balance"] += amount
            print("Deposit {} Successful. New balance: {}".format(amount, customer['balance']))
            break
    else:
        print("Customer not found")

def withdraw(customers):
    account_number = input("Enter account number:")
    amount = float(input("Enter withdrawal amount:"))
    for customer in customers:
        if amount > customer["balance"]:
            print("Insufficient Fund")
        else:
            customer["balance"] -= amount
            print("Withdraw {} Successful. New balance: {}".format(amount, customer['balance']))
            break
    else:
        print("Customer not found")