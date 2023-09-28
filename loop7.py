a=input("enter a password")
b=len(a)
c=a.split()
l,m,n,o,p=0,0,0,0,0
for i in range(b):
    if(a[i]==a.isalpha()):
        l=l+1
    elif(a[i]==a.islower()):
        m=m+1
    elif(a[i]==a.isupper()):
        n=n+1
    elif(a[i]!=a.isalnum()):
        o=o+1
    elif(a[i]==a.isnumeric()):
        p=p+1
if(l>0 and m>0 and n>0 and o>0 and p>0):
    print("password is strong")
else:
    print("password is not strong")
