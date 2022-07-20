num = bin(int(input()))

num = num[2:]
# print(num)

res = [0]
count = 1

# print(num[0] == "1")

for i in range(0, len(num)-1):
    if num[i] == "1" and num[i+1] == "1":
        count += 1
    elif num[i] == '1' and num[i+1] == '0':
        res.append(count)
        count = 1

res.append(count)
# print(res)
print(max(res))


# better solver
while True:
    try:
        a = int(input())
        b = str(bin(a)[2:])
        c = b.split('0')
        l = []
        for i in c:
            l.append(len(i))
        print(max(l))
    except:
        break
