key = input()
words = input()
password = ''

# get the no repeatable key
norepeat = ''
for i in key:
    if i not in norepeat:
        norepeat += i
        
check = 'a'
for i in range(26):
    if chr(ord('a') + i) not in norepeat:
        norepeat += chr(ord('a') + i)

#transform
encode = {}
count = 97
for i in norepeat:
    encode[chr(count)] = i
    count += 1

for i in words:
    password += encode[i]
    
print(password)
