# output the least two

while True:
    try:
        m,n=map(int,input().split(" "))
        num=list(map(int,input().split()))
        num.sort()
        print(" ".join(map(str,num[:n])))
    except:
        break