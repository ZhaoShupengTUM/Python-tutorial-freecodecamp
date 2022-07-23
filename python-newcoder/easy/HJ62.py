while True:
    try:
        num = bin(int(input()))
        res = 0
        for i in num:
            if i == '1':
                res += 1
        print(res)
    except:
        break