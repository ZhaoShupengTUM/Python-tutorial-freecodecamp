key = input()
words = input()
password = ''

# get the no repeatable key, donot use set() because it will change the order
norepeat = ''
for i in key:
    if i not in norepeat:
        norepeat += i
        
check = 'a'
for i in range(26):
    if chr(ord('a') + i) not in norepeat:
        norepeat += chr(ord('a') + i)

#transform using a dictionary
encode = {}
ascii = 97
for i in norepeat:
    encode[chr(ascii)] = i
    ascii += 1

for i in words:
    password += encode[i]
    
print(password)
