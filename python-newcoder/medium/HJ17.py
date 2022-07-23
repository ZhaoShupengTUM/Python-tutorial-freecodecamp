strlist = input().split(";")
x = 0
y = 0
# print(strlist)
strlistnew = []
for i in strlist:
    #check the correctness of the input
    if i != '' and i[0] in "ASWD" and i[1:].isdigit():
        strlistnew.append(i)

for i in strlistnew:
    if i[0] == 'A':
        x -= int(i[1:])
    elif i[0] == 'D':
        x += int(i[1:])
    elif i[0] == 'W':
        y += int(i[1:])
    elif i[0] == 'S':
        y -= int(i[1:])
        
print(str(x)+','+str(y))
# print(strlist)

