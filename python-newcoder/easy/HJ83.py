while True:
    try:
        x, y = map(int, input().split())
        # 判断初始化是否成功，即行列表是否超出规格
        if x > 9 or y > 9:
            print(-1)
        else:
            print(0)
        x1, y1, x2, y2= map(int, input().split())
        # 判断交换单元格是否成功
        if x1 >= x or x2 >= x or y1 >= y or y2 >= y:
            print(-1)
        elif x1 == x2 and y1 == y2:
            print(-1)
        else:
            print(0)
        insertrow = int(input())
        # 判断插入行后是否超出范围
        if insertrow >= x or insertrow < 0 or x + 1 > 9:
            print(-1)
        else:
            print(0)
        insertcol = int(input())
        # 判断插入列后是否超出范围
        if insertcol >= y or insertcol < 0 or y + 1 > 9:
            print(-1)
        else:
            print(0)
        search = list(map(int, input().split()))
        # 判断查询的单元格是否存在
        if search[0] >= x or search[1] >= y:
            print(-1)
        else:
            print(0)
    except:
        break