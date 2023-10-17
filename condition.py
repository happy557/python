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
temp=int(input("Enter the temp value:"))
unit=input("enter the unit (F for Fahrenheit, C for Celsius):")
if unit.upper()=='F':
    converted=(temp-32)*5/9
    print(f"{temp}F is {converted:.2f}C")
elif unit.upper()=='C':
    converted=(temp*9/5)+32
    print(f"{temp}c is {converted:.2f}F")
else:
    print("invalid unit.")