# create a python program to reconstruct a banking applicaton,that a employee can add new customers which include their name, age, contact number, account number and initially balance must be zero.the bank employee can add balance, withdraw balance, program should exit only under user command.


customers=[]
while True:
    print("\n1. Add Customer\n2. View Customers\n3. Deposit\n4. Withdraw\n5. Exit")
    choice=input("Enter your choice:")
    if choice=='1':
        name=input("enter customer name:")
        age=int(input("enter customer age:"))
        contact_number=input("enter contact number:")
        account_number=input("enter account number:")
        
        new_customer={
            "name":name,
            "age":age,
            "contact_number":contact_number,
            "account number":account_number,
            "balance":0
            }
        customers.append(new_customer)
        print("customer added successfully!")
    elif choice=='2':
        print("\ncustomers list")
        for customer in customers:
            print("\nName:{customer['Name']}\nAge: {customer['Age']}\ncontact:{customer['contact_number']}\n Account Number:{customer['account_number']}\nBalance:${customer['balance']}")
                
                    