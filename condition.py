# amount=7500
# if amount>=10000:
#     discount_percentage=10
# else:
#     if 5000<=amount<10000:
#      discount_percentage=5
#     else:
#      discount_percentage=0
#     discount=amount*discount_percentage//100
#     final_amount=amount-discount
#     print(f"final after a {discount_percentage}% discount:{final_amount/100:2f}")

# year=int(input("enter a year:"))
# if(year%4==0 and year%100!=0)or(year%400==0):
#     print("Leap year")
# else:
#     print("not a leap year")

# num=42
# while True:
#     guess=int(input("guess the secret number between 1 and 100:"))
#     if guess==num:
#         print("correct answer")
#         break
#     elif guess<num:
#         print("Too low. Try again.")
#     else:
#         print("Too high. Try again.")
# temp=int(input("Enter the temp value:"))
# unit=input("enter the unit (F for Fahrenheit, C for Celsius):")
# if unit.upper()=='F':
#     converted=(temp-32)*5/9
#     print(f"{temp}F is {converted:.2f}C")
# elif unit.upper()=='C':
#     converted=(temp*9/5)+32
#     print(f"{temp}c is {converted:.2f}F")
# else:
#     print("invalid unit.")



#Q=1

# score=int(input("enter the numerical grade:"))
# if 90<=score<=100:
#     grade='A'
# elif 80<=score<=89:
#     grade="B"
# elif 70<=score<=79:
#     grade="C"
# elif 60<=score<=69:
#     grade="D"
# elif 0<=score<=59:
#     grade="F"
# else:
#     grade='invalid score'   
# print(f"the corressponding letter grade is:{grade}")


#Q=2

# num1=int(input("enter the first number:"))
# operator=input("enter the operator (+,-,*,/):")
# num2=int(input("enter the second number:"))
# result=None
# if operator=='+':
#     result=num1 + num2
#     print(result)
# elif operator=='-':
#     result=num1 - num2
#     print(result)
# elif operator=='*':
#     result=num1 * num2
#     print(result)
# elif operator=='/':
#     if num2 !=0:
#         result=num1 / num2
#         print(result)
#     else:
#         print("error: cannot divide by zero.")
# else:
#     print("error: invalid operator.")


#Q=3

# age=int(input("enter the person's age:"))
# if 0<=age<=2:
#     category='infant'
# elif 3<=age<=12:
#     category='child'
# elif 13<=age<=19:
#     category='teenager'
# elif 20<=age<=64:
#     category='adult'
# elif age<=65:
#     category='senior'
# else:
#     category='invalid age'
# print("category:",category)


#Q=4

# weight=int(input("enter weight in kilograms:"))
# height=int(input("enter height in meters:"))
# bmi=weight/(height**2)
# category=None
# if bmi<18.5:
#     category='u'
# elif 18.5<=bmi<=24.9:
#     category='n'
# elif 25<=bmi<=29.9:
#     category='o'
# elif bmi<=30:
#     category='ob'
# print("bmi is:",bmi)
# print("classified as:",category)

#Q=6

# num1=int(input("enter the first number:"))
# num2=int(input("enter the second number:"))
# num3=int(input("enter the third number:"))
# largest=max(num1,num2,num3)
# print("largest number:",largest)

#Q=7

# number=int(input("enter anumber(1-7):"))
# days={
#     1:'sunday',
#     2:'monday',
#     3:'tuesday',
#     4:'wednesday',
#     5:'thursday',
#     6:'friday',
#     7:'saturday'
# }
# if 1<=number<=7:
#     print("day is:",days[number] )
# else:
#     print("invalid input")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 