while True:
    try:

        line=input()
        a=0
        b=0
        c=0
        d=0
        flag=True

        for i in line:
            if i.isdigit():
                a=1
            elif i.islower():
                b=1
            elif i.isupper():
                c=1
            else:
                d=1

        for j in range(len(line)-3):  #从第一个遍历到倒数第三个
            if line.count(line[j:j+3])>1:  #计算长度为3的重复字符串
                flag=False
                
        if len(line)>8 and (a+b+c+d)>=3 and flag:
            print("OK")
        else:
            print("NG")
    except:
        break
        

