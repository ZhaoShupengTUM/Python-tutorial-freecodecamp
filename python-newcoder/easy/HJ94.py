while True:
    try:
        a = int(input())
        b = input().split()
        c = int(input())
        d = input().split()
        e = {}
        for i in d:
            if i not in b:
                e["Invalid"] = e.get("Invalid",0)+1
            else:
                e[i] = e.get(i,0)+1
        for i in b:
            print(i,":",e.get(i,0))
        print("Invalid",":",e.get("Invalid",0))
    except:
        break