'''1. 二维数组怎么建
2. DFS算法实现。 理解递归回溯'''


def dfs(i,j):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    if i == m-1 and j == n-1:  #find the goal
        for pos in route:
            print('('+str(pos[0])+','+str(pos[1])+')')
        return
    
    for k in range(4):
        x = i+dx[k]
        y = j+dy[k]  #four next points
        if x>=0 and x<m and y>=0 and y<n and map1[x][y]==0:
            map1[x][y]=1
            route.append((x,y))
            dfs(x,y)
            map1[x][y]=0
            route.pop()
#如果进入了死胡同，会进行递归回溯到上一个分叉点        
    else:
        return
            

while True:
    try:
        m,n = list(map(int,input().split()))
        map1=[]
        for i in range(m):
            s=list(map(int,input().split()))
            map1.append(s)
# 		初始值是（0，0）将其标记为已经访问
        route = [(0,0)]
        map1[0][0]=1
        dfs(0, 0)
        
    except:
        break
