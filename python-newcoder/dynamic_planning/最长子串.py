def length_of_LIS(nums):
    n = len(nums)
    L = [1] * n   #存放从各位置开始的最长子串的长度

    for i in reversed(range(n)):
        for j in range(i+1, n):
            if nums[j] > nums[i]:
                L[i] = max(L[i], L[j] + 1)

    return max(L)

nums = [1, 5, 2, 4, 3]
print(length_of_LIS(nums)) 

# print(list(range(2,2)))
