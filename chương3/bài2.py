try:
 Hours = float(input("Enter Hours: "))
 Rate = float(input("Enter Rate: "))
except:
 print("Error, please enter numeric input")
if Hours > 40:
   pay = 40 * Rate + ( Hours - 40 ) * Rate * 1.5
else:
   pay = Hours * Rate
print("Enter Hours: ", Hours)
print("Enter Rate: ", Rate)
print("pay: ", pay)
