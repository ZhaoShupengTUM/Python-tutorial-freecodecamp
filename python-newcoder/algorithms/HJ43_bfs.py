'''1. 二维数组怎么建
2. DFS算法实现。 理解递归回溯'''

def dfs(i,j):
    dx = [0,0,-1,1]   #四种行进方式
    dy = [-1,1,0,0]
    if i == m-1 and j == n-1:  #find the goal
        for pos in route:
            print('('+str(pos[0])+','+str(pos[1])+')')
        return
    
    #递归部分
    for k in range(4):
        x = i+dx[k]
        y = j+dy[k]  
        if x>=0 and x<m and y>=0 and y<n and map1[x][y]==0:  #可以行进的条件
            map1[x][y]=1
            route.append((x,y))
            dfs(x,y)
    #回溯部分
            map1[x][y]=0
            route.pop()

    #如果进入了死胡同，会进行递归回溯到上一个分叉点，递归结束条件      
    else:
        return
            

while True:
    try:
        m,n = list(map(int,input().split()))
        map1=[]
        for i in range(m):
            s=list(map(int,input().split()))
            map1.append(s)  #建立地图 
# 		初始值是（0，0）将其标记为已经访问
        route = [(0,0)]
        map1[0][0]=1
        dfs(0, 0)
        
    except:
        break


'''1. BFS算法实现'''
def sol43():
    W = lambda x, y: (x - 1, y)
    S = lambda x, y: (x + 1, y)
    A = lambda x, y: (x, y - 1)
    D = lambda x, y: (x, y + 1)
    [N, M] = map(int, input().strip().split(' '))
    end = (N - 1, M - 1)

    def start2end(m, s, p):
        # find child
        child, v = [], list(p)
        for F in [W, A, S, D]:
            t = (F(s[0],s[1]))
            if not (0 <= t[0] < N and 0 <= t[1] < M):
                continue
            if not m[t[0]][t[1]] and (t not in v):
                if t == end:
                    p.append(end)
                    for pp in p:
                        print('(%d,%d)' %(pp[0],pp[1]))
                    return
                else:  # Enter the child node
                    child.append(t)
        if not child:
            # no child exit
            return
        for t in child:
            p_old = p.copy()
            p_old.append(t)
            start2end(m, t, p_old)

    maze = []
    for i in range(N):
        maze.append(list(map(int, input().strip().split(' '))))
    paths = [(0,0)]
    start2end(maze, (0,0), paths)
    return


if __name__ == '__main__':
    while True:
        try:
            sol43()
        except EOFError as e:
            # print(e)
            break
