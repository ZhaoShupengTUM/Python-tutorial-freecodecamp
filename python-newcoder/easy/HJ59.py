#find the most nearing two sushu

def sushu(x):
    for j in range(2,x):
        if x%j==0:
            return False
    return True


while 1:
    try:
        n=int(input())
        m=n//2
        for i in range(m):
            a=n//2-i
            b=n//2+i
            if sushu(a) and sushu(b):
                print(a)
                print(b)
                break
    except:
        break