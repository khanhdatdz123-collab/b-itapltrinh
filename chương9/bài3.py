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
max_email = None
max_count = 0
for email, count in counts.items():
    if count > max_count:
        max_count = count
        max_email = email
print(max_email, max_count)
