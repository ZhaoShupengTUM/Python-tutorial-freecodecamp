#perfect number

while True:
    try:
        a=int(input())
        print(len(list(filter(lambda x: x < a, [6, 28, 496, 8128]))))
    except:
        break
