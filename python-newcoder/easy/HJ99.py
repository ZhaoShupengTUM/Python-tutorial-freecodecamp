while True:
    try:
        a=int(input())
        b=0
        for i in range(a+1):
            if str(i*i).endswith(str(i)):
                b+=1
        
        print(b)
    except:
        break
