'''放砝码问题：
按照种类来放置砝码，
第一种砝码可以放0到n1个， 第二种可以放0到n2个，
进行组合之后去重
1. 两个for循环生成set'''

while True:
    try:
        n = int(input())  #n types 
        m = list(map(int, input().split()))  #n kinds of mass
        x = list(map(int, input().split()))  #each kind has x farmer
        
        res = [0]
        for i in range(n):  #
            tmp = [m[i] * j for j in range(x[i]+1)]
            res = list(set(a+b for a in tmp for b in res))  #单行双循环嵌套
        print(len(res))
    except:
        break