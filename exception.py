# Exception handling
try:
  x = 10
  print(x)
except Exception as ex:
  print(ex)
  print("Print failed")
finally:
  print("Final stament")

x = 10
y = "0"

if type(y) is not int:
  raise TypeError("Number must be an integer")
  # raise Exception("zero not allowed")
else:
  print(x/y)