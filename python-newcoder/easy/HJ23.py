# delete the least appearing char

while True:
    try:
        aaa = list(input())
        b = list(set(aaa))   #store all the type of the chars
        c=[]   #store the corresponding appearing count
        for i in b:
            c.append(aaa.count(i))
        for i in range(len(c)):
            if c[i] == min(c): 
                while b[i] in aaa:
                    aaa.remove(b[i])
        print("".join(aaa))  #join the list with space to a string
    except:
        break

# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。