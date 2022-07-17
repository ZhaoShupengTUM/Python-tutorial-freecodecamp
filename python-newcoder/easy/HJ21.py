#easy coder


while True:
    e=[]
    try:
        s = list(input())
        for i in s:
            if i>="A" and i <="Z":
                t=chr((ord(i)+33))
                if t>'z':
                    t='a'
                e.append(t)
            elif i>="a" and i <="c":
                 e.append('2')
            elif i>="d" and i <="f":
                 e.append('3')
            elif i>="g" and i <="i":
                 e.append('4')
            elif i>="j" and i <="l":
                 e.append('5')
            elif i>="m" and i <="o":
                 e.append('6')
            elif i>="p" and i <="s":
                 e.append('7')
            elif i>="t" and i <="v":
                 e.append('8')
            elif i>="w" and i <="z":
                 e.append('9')
            else :
                 e.append(i)
        print("".join(e))
    except:
        break

    # chr() 用一个整数作参数，返回一个对应的字符。
    # chr(i)
    # i -- 可以是 10 进制也可以是 16 进制的形式的数字，数字范围为 0 到 1,114,111 (16 进制为0x10FFFF)。
