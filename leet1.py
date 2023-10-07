x=121
i,j=x,0
while x>0:
    num=x%10
    j=j*10+num
    x//=10
    h=i==j
    print(h)
    
