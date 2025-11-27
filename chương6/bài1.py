str = 'X-DSPAM-Confidence:0.8475•'
pos = str.find(': ')
number_str = str[pos + 1:]
number = float (number_str)
print (number
