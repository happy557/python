nums=[3,2,2,3]
val=3
k=0
for i in range(len(nums)):
    if nums[i]!=val:
        nums[k]=nums[i]
        k+=1
        nums[:k]=sorted(nums[:k])
        print(f"output:{k}, nums={nums[:k]}")
        