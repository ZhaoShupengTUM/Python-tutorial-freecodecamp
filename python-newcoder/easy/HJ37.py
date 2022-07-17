# rabits spawn Fibonacci sequence

month = int(input())

rabbit = [1, 1]

if month == 1 or month == 2:
    print(1)
else:
    for i in range(2, month):
        rabbit.append(rabbit[i-1] + rabbit[i-2])
    print(rabbit[month - 1])