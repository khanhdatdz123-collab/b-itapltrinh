def computepay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        pay = 40 * rate + overtime * rate * 1.5
    else:
        pay = hours * rate
    return pay
h = float(input("Enter Hours: "))
r = float(input("Enter Rate: "))
p = computepay(h, r)
print("Pay:", p)
