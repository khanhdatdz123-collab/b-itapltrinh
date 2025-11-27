fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
count = 0
for line in fhand :
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        print(words[1])
        count += 1
print("There were", count, "lines in the file with From as the first word")
