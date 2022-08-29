'''1. 对于字母串不分大小写进行排序
    2. 字母排序之后只插入到原来字母存在的位置'''

while True:
    try:
        string=input()
        temp=list(string)
        alphastring=[]  #所有字母的列表
        for i in string:
            if i.isalpha():
                alphastring.append(i)
        alphastring.sort(key=str.upper)     #将所有字母不论大小写排序，相同时保证之前输入的顺序不变
        j=0

        for i in range(len(temp)):
            if temp[i].isalpha():#对字母进行排序
                temp[i]=alphastring[j]
                j+=1

        print(''.join(temp))
    except:
        break