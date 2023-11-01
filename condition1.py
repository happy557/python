letter={
        2:"abc",
        3:"def",
        4:"ghi",
        5:"jkl",
        6:"mno",
        7:"pqrs",
        8:"tuv",
        9:"wxyz"
    }
c=int(input("Enter the number:"))
d=c//10
c=c%10
b=letter[d]
a=letter[c]
for j in a:
    for i in b:
        print(i,j)
