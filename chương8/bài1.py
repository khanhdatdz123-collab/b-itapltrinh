fname = input("Enter file: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
words = []
for line in fhand:
    line = line.rstrip()
    pieces = line.split()
    for word in pieces:
        if word not in words:
            words.append(word)
words.sort()
print(words)
