'''百钱买鸡问题，列出方程之后循环找整数'''

while True:
    try:
        num = int(input())
        for x in range(100//7 + 1):
            if (100 - 7*x)%4 == 0:
                y = (100-7*x)/4
                print(int(x), int(y), int(100-x-y))
    except:
        break