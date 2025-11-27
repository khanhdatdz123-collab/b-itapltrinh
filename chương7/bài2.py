fhand = open (fname)
except:
    print("File cannot be opened:", fname)
    quit()
count = 0
total = 0.0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    colon_pos = line.find(":")
    value = float(line(colon_pos+1).zstrip())
    total += valua
    count += 1
if count > 0:
    avg = total / count
    print("Average spam confidence:", avg)
else:
    print("No 'X-DSPAM-Confidence' lines found.")
