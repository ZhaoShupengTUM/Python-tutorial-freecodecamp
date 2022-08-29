'''一个无序数组找出递增最长子串的长度'''

#暴力枚举递归算法
def violence(nums, i):  #return the length of longest increasing subsequence starting from i
    #递归终止条件
    if i ==len(nums) - 1:
        return 1 
    
    max_len = 1
    for j in range(i+1, len(nums)):
        if nums[j] > nums[i]:
            max_len = max(max_len, violence(nums,j)+1)
    return max_len

def length_result(nums):
    return max(violence(nums, i) for i in range(len(nums)))


#动态规划算法
def length_of_LIS(nums):
    n = len(nums)
    L = [1] * n   #存放从各位置开始的最长子串的长度

    for i in reversed(range(n)):
        for j in range(i+1, n):
            if nums[j] > nums[i]:
                L[i] = max(L[i], L[j] + 1)

    print(L)

    return max(L)

nums = [1, 5, 2, 4, 3]
print(length_of_LIS(nums)) 

# print(list(range(2,2)))
