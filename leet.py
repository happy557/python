nums=[2,7,11,15]
target=9
number={}
for i in range(len(nums)):
    num=nums[i]
    j=target-num
    if j in number:
        h=[number[j], i]
        print(h)
        break
    number[num]=i