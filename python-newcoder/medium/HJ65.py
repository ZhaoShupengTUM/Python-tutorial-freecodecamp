shortstr = input()
longstr = input()

if len(shortstr) > len(longstr):
    shortstr, longstr = longstr, shortstr
    
res = []
for i in range(0, len(shortstr)):  #starting position
    for j in range(i, len(shortstr)):  #end position is from the end to front
        if shortstr[i:j+1] in longstr:
            res.append(shortstr[i:j+1])

# print(res)
count = list(map(len, res))
# print(count)
index = 0
for i in count:
    if i == max(count):
        index = count.index(i)
        break
# print(index)        
print(res[index])
    
# print(list(reversed(range(0,3))))