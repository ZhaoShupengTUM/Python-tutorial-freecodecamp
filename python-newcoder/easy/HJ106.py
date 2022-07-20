mystr = input()

res = []

for word in mystr:
    res.append(word[::-1])

res.reverse()
print(''.join(res))

#better solution
inputString=input()
print(inputString[::-1])


