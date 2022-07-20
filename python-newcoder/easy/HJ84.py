while True:
    try:
        a = 0
        s = input()
        for i in s:
            if i.isupper():
                a += 1
        print(a)
    except:
        break

                       