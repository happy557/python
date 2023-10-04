elif choice=='2':
        account_number=input("enter account number:")
        amount=float(input("enter deposit amount:"))
        for customer in customers:
            if customer[account_number]==account_number:
                customer["balance"]+=amount
#             break
    #         else:
    #             print("customer not found!")
                
    # elif choice=='3':
    #     account_number=input("enter account number:")
    #     amount=float(input("enter withdrawal amount:"))
    #     for customer in customers:
    #         if customer.account_number==account_number:
    #             customer.withdraw(amount)
    #             break
    #         else:
    #             print("customer not found!")
    # elif choice=='4':
    #     print("exiting the program.")
    #     break
    # else:
    #     print("invalid choice.Please enter a valid option.")