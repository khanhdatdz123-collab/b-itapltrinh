numbers = []
while True:
    value = input("Enter a number: ")
    if value == "done":
        break
    try:
        number = float(value)
    except:
        print("Invalid input")
        continue
    numbers.append(number)
if len(numbers) > 0:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
else:
    print("No numbers were entered.")
