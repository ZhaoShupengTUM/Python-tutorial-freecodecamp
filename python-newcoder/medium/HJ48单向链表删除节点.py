s=list(map(int,input().split()))
l=s[4:len(s)-1]
q=[s[3],s[2]]   #初始的两个节点
m=s[-1]

for i in range(len(l)//2):  #抛去最初两个节点之后的节点数/2
    n=q.index(l[2*i+1])+1  
    q.insert(n,l[2*i])
q.remove(m)
print(' '.join(map (str,q)))