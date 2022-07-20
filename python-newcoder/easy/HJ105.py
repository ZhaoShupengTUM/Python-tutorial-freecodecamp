data=[]
sum_=0
while True:
    try:
        a=int(input())
        if a<0:
            sum_+=1
        if a>0:
            data.append(a)
    except:
        break
print(sum_)
if data==None:
    print('0.0')
else:
    print('%.1f'%(sum(data)/len(data)))