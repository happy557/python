# i=0
# while i<9:
#     print(i)
#     i+=1


# create a python program,let to-do application using list.Implement the following methods add, delete, update, display?

choice='y'
list=["Market","movie","game"]
while choice=='y':
    print("\n1. Display Task\n2. Delete Task\n3. Add Task\n4 exit. ")
    option=input("Enter your choice(1-4):")
    if option=="1":
        print(list)
    elif option=="2":
        task=input("enter the task to delete:")
        list.remove(task)
    elif option=="3":
        task1=input("enter the task to add:")
        list.append(task1)
    elif option=="4":
        exit()
    else:
        print("invalid choice.Please enter a number between 1 and 5.")