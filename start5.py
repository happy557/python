t=(1,2,3.5 ,"abc",3.5)
t2=(8,9,10)
t3=t+t2
print(t3)
l=list(t)
l.append(100)
tup=tuple(l)
print(tup)

tup=("cat","dog","goat")
print(len(tup))
t2=("apple","orange")
t3=tup+t2
print(t3)
l=list(tup)
l.append("xyz")
tup=tuple(l)
print(tup)
l=list(tup)
l.clear()
print(l)
del l
print(l)