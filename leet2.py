strs = ["flower","flow","flight"]
if not strs:
    prefix=""
else:
    strs.sort()
    x,y=strs[0],strs[-1]
    prefix=""
    for i in range(len(x)):
        if i<len(y) and x[i]==y[i]:
            prefix+=x[i]
        else:
            break
        print(prefix)