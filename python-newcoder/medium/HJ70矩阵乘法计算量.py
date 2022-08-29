'''1. use stack to deal with the parentheses'''

while True:
    try:
        n = int(input())
        arr = []
        order = []
        res = 0
        for i in range(n):
            arr.append(list(map(int, input().split())))    #  用二维矩阵处理输入的矩阵行列数据
        f = input()

        for i in f:
            if i.isalpha():   
                order.append(arr[ord(i)-65])               # 将字母转换成第几个矩阵的处理信息
            elif i == ')' and len(order) >= 2:             # 读到右括号就处理最近的两个矩阵相乘的结果
                b = order.pop()
                a = order.pop()
                res += a[1]*b[1]*a[0]                      # 累计到res中
                order.append([a[0], b[1]])     #放入运算结果之后得到的矩阵
        print(res)
    except:
        break

