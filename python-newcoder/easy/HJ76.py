num = int(input())

num_quad = num**2

odd_list = []

first_num = num_quad - (num - 1)
for i in range(num):
    odd_list.append(first_num + 2*i)

print("+".join(map(str,odd_list)))

        