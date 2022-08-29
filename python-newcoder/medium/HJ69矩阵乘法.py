x = int(input())
y = int(input())
z = int(input())

#first matrix
A = []
for i in range(x):
    A.append(list(map(int, input().split())))

#second matrix
B = []
for i in range(y):
    B.append(list(map(int, input().split())))

#mul
# C = [[0] * z] * x  notice: bug
C=[[0 for k in range(z)] for i in range(x)]

for i in range(x):
    for k in range(z):
        for j in range(y): #计算每个输出单元格的数据，A行与B列的乘积，长度为y
            C[i][k] += A[i][j] * B[j][k]

for i in range(x):
    print(' '.join(map(str, C[i])))
