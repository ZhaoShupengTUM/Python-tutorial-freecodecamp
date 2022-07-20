a = int(input())

list1 = list(map(int, input().split()))

b = int(input())

list2 = list(map(int, input().split()))

list3 = set(list1 + list2)
             
list3 = sorted(list3)
             
print("".join(map(str, list3)))