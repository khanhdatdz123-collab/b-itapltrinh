fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
domains = {}
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        if len(words) > 1:
            email = words[1]
            domain = email.split('@')[-1]
            domains[domain] = domains.get(domain, 0) + 1
print(domains)
