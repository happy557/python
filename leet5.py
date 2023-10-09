x=8
i,j=0,x
while i<=j:
    k=i+(j-i)//2
    l=k*k
    if l==x:
        m=k
        break
    elif l<x:
        i=k+1
    else:
        j=k-1
        m=j
    print(m)