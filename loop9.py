# create a python program to reconstruct a banking applicaton,that a employee can add new customers which include their name, age, contact number, account number and initially balance must be zero.the bank employee can add balance, withdraw balance, program should exit only under user command.

customers=[]
account_num_counter=1000
while True:
    print("\n1. Add Customer\n2. View Customers\n3. Deposit\n4. Withdraw\n5. Exit")
    choice=input("Enter your choice:")
    if choice=='1':
        name=input("enter customer name:")
        age=int(input("enter customer age:"))
        contact_number=input("enter contact number:")
        account_number=str(account_num_counter)
        account_num_counter+=1
        
        new_customer={
            "name":name,
            "age":age,
            "contact_number":contact_number,
            "account_number":account_number,
            "balance":0
            }
        customers.append(new_customer)
        print("customer added successfully!")
    elif choice=='2':
        print("\ncustomers list")
        search_option=input("search by name (N) or account number (A):").upper()
        if search_option=='N':
            search_name=input("customer name:")
            found=False
            for customer in customers:
                if customer["name"]==search_name:
                   print("\nName: "+ customer['name']+"\nAge"+ str(customer['age'])+"\nContact:"+customer['contact_number']+"\nAccount Number:"+customer['account_number']+"\nBalance:"+str(customer['balance']))
                   found=True
                   if not found:
                    print("customer is not found")
        elif search_option=='A':
            search_account_number=input("customer account number:") 
            found=False
            for customer in customers:
                if customer["account_number"]==search_account_number:
                   print("\nName: "+ customer['name']+"\nAge"+ str(customer['age'])+"\nContact:"+customer['contact_number']+"\nAccount Number:"+customer['account_number']+"\nBalance:"+str(customer['balance']))
                   found=True
            if not found:
                print("customer is not found")
        else:
            print("invalid search option") 
    elif choice=='3':
        account_number=input("enter account number:")
        amount=float(input("enter deposit amount:"))
        for customer in customers:
            if customer["account_number"]==account_number:
                customer["balance"]+=amount
            print(f"Deposit {amount} Successful. New balance:{customer['balance']}")
            break
        else:
           print("Customer not found") 
    elif choice=='4':
        account_number=input("enter account number:")
        amount=float(input("enter withdrawal amount:"))
        for customer in customers:
            
           if amount>customer["balance"]:
            print("insufficent Fund")
           else:
            customer["balance"]-=amount
           print(f"Withdraw {amount} Successful. New balance:{customer['balance']}")
           break
        else:
         print("Customer not found") 
    elif choice=='5':
        print("exiting the program.")
        break
    else:
        print("invalid choice.Please enter a valid option.")
        
        
        
        
        