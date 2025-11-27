fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
counts = {}
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        if len(words) > 1:
            email = words[1]
            counts[email] = counts.get(email, 0) + 1
print(counts)
