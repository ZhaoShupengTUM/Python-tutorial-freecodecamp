while 1:
    try:
        y, m, d = map(int,input().split())
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        tol_days = sum(month[:m - 1]) + d
        if m > 2 and (y%4==0 and y%100!=0 or y%400==0):
            tol_days += 1
        print(tol_days)
    except:
        break