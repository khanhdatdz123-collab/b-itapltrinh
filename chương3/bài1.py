Hours = float(input("Enter Hours: "))
Rate = float(input("Enter Rate: "))
print("Enter Hours: ", Hours)
print("Enter Rate: ", Rate)
if Hours > 40:
    print("Pay: ", (Hours - 40) * 1.5 * Rate + 40 * Rate )
else:
    print("pay: ", Hours * Rate)
