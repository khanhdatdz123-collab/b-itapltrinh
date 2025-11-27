name = input ("Enter a file name: ")
try:
    fhand = open (name)
    for line in fhand:
        print(line. upper ().rstrip())
except:
    print("File cannot be opened:" , name)
