str1 = input()
str2 = input()

flag = 0

for i in str1:
    if i in str2:
        pass
    else:
        print('false')
        flag = 1
        break

if flag == 0:
    print('true')

#better solutions using set and &
while True:
    try:
        a,b=set(input()),set(input())
        print ("true" if a&b==a else "false")
    except:
        break