nline = int(input())

for i in range(nline):
    mystr = input()
    norepeat = list(set(mystr))
    count = {}
    for i in norepeat:
        count[i] = mystr.count(i)
    count = sorted(count.items(), key = lambda x:x[1], reverse=True)
    countlist = [i for (i,j) in count]
    
    beauty = {}
    value = 26
    for i in countlist:
        beauty[i] = value
        value -= 1
    
    res = 0
    for word,n in count:
        res += beauty[word]*n
        
    print(res)