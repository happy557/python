l=[1,2,3]
m=1
for i in range(len(l)-1,-1,-1):
    l[i]+=m
    m=l[i]//10
    l[i]%=10
# if m:
#     l.insert(0,m)
#     print(l)