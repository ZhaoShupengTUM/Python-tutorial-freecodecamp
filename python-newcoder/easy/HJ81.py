while True:
    try:
        a,b=set(input()),set(input())
        print ("true" if a&b==a else "false")
    except:
        break