
def dfs(nums):
    if not nums:
        return False
    if len(nums) == 1:
        return abs(nums[0] - 24) < 1e-6
    for i, a in enumerate(nums):                   # 获取第一个数字
        for j, b in enumerate(nums):               # 获取第二个数字
            if i != j:                             # 控制不重复
                newNums = list()
                for k, c in enumerate(nums):       # 获取第三个数字
                    if k != i and k != j:
                        newNums.append(c)
                for k in range(4):
                    if k < 2 and i > j:            # 对于+和*操作来说不需要考虑两者的顺序，因此舍去一种
                        continue
                    if k == 0:
                        newNums.append(a+b)
                    if k == 1:
                        newNums.append(a*b)
                    if k == 2:
                        newNums.append(a-b)
                    if k == 3:
                        if abs(b) < 1e-6:          # 排除除数为0的情况
                            continue
                        newNums.append(a/b)
                    if dfs(newNums):
                        return True
                    newNums.pop()
    return False

while True:
    try:
        lst = [int(x) for x in input().split()]
        if dfs(lst):
            print('true')
        else:
            print('false')
    except:
        break
