def length_of_zhuang(zhuang):
    n = len(zhuang)
    L = [1] * n
    for i in reversed(range(n)):
        for j in range(i+1, n):
            if zhuang[j] > zhuang[i]:
                L[i] = max(L[i], L[j] + 1)
    return max(L)

n = int(input())
zhuang = list(map(int, input().split()))
print(length_of_zhuang(zhuang))