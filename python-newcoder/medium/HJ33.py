'''1. 二进制不需要0b标识符就可以被int()转化为整数'''
# ip to int
ip = list(map(int, input().split('.')))
toint = []
for num in ip:
    num_bin = bin(num)[2:].rjust(8,'0')
    toint.append(num_bin)
res = '0b' + ''.join(toint)
print(int(res, 2))

#int to ip
num = int(input())
b = bin(num)[2:].rjust(32, '0')
print(str(int(b[0:8],2))+'.'+str(int(b[8:16],2))+'.'+str(int(b[16:24],2))+'.'+str(int(b[24:32],2)))



