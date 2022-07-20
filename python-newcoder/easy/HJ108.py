a, b = map(int, input().split())

def gys(a, b):
    while (b != 0):
        c=a%b
        a=b
        b=c
    return a
print(int((a*b)/gys(a,b)))
