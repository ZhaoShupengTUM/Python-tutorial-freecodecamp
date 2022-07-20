def func(x,y):
    if x < 0 or y < 0:
        return 0
    elif x == 0 or y == 0:
        return 1
    else:
        return func(x-1, y)+func(x, y-1)
 
while True:
    try:
        n, m = map(int, input().split())
        res = func(n, m)
        print(res)
    except:
        break


#besser solver
import math
    
while True:
    try:
        row, col = map(int, input().split())
        total_step = col + row
        res = math.factorial(total_step) / (math.factorial(col) * math.factorial(row))
        print(int(res))
    except:
        break
