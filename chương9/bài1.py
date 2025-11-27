fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
days = {}
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        if len(words) > 2:
            day = words[2]
            days[day] = days.get(day, 0) + 1
print(days)
