s = 0
sl = 0
while True:
    value = input("Enter a number: ")
    if value == "done":
        break
    try:
        number = float(value)
    except:
        print("Invalid input")
        continue
    s += number
    sl += 1
if sl > 0:
    average = s / sl
    print(s, sl, average)
