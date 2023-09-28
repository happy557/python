names=["arjun","aromal","edwin","lolan"]
passwords=["passwords1","passwords2","passwords3","passwords4"]
a=input("enter the name:")
b=input("enter the password:")
verified=False

for i in range(len(names)):
    if a==names[i] and b==passwords[i]:
        verified=True
        
if verified:
    print("authentication confirmed.",a)
else:
    print("authenthication Failed.")