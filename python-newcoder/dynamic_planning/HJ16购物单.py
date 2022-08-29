money, things = map(int, input().split())
money = money // 10  # money都是10的整数，整除后，减小循环次数
# 三列分别表示主件，附件1，附件2
weight = [[0] * 3 for _ in range(0, things + 1)]  # 价格
# print(weight)
value = [[0] * 3 for _ in range(0, things + 1)]  # 价值=价格*重要度
result = [[0] * (money + 1) for _ in range(0, things + 1)]
for i in range(1, things + 1):
    prices, degree, depend = map(int, input().split())  # 分别为价格，重要性，主附件
    prices = prices // 10

    if depend == 0:  # 主件
        weight[i][0] = prices
        value[i][0] = prices * degree

    elif weight[depend][1] == 0:  # 附件
        weight[depend][1] = prices  # 第一个附件
        value[depend][1] = prices * degree

    else:
        weight[depend][2] = prices  # 第二个附件
        value[depend][2] = prices * degree
# 遍历计算
for i in range(1, things + 1):  # 每几件物品
    for j in range(money, -1, -1):
        if j >= weight[i][0]:  # 当前价格j可以容下第i个主件时,比较（上一个物品对应价格的价值）与（第i个物品的价值 + 余额价格对应上个物品价值）
            result[i][j] = max(result[i - 1][j], result[i - 1][j - weight[i][0]] + value[i][0])
            # 在确定主件可容纳，并做相应计算之后,判断附件的容纳情况，如果主件都没有办法容纳，则附件必定不可容纳
            if j >= (weight[i][0] + weight[i][1]):
                # 当可以容下第i个主件和此主件的第1个附件时，此时需要在比大小时加入当前最优，保证添加附件的结果不会反而更小
                # 比较（当前价格对应上一物品的价值）与（主键价值+附件1价值+上一物品在价格（j-主键价格-附件1价格）时对应的价值）
                result[i][j] = max(result[i][j], result[i - 1][j], result[i - 1][j - weight[i][0] - weight[i][1]] + value[i][0] + value[i][1])

            if j >= (weight[i][0] + weight[i][2]):
                # 可以容下第i个主件和此主件的第2个附件，此时也需要在比大小时加入当前最优，保证添加附件的结果不会反而更小
                # 比较（当前价格对应上一物品的价值）与（主键价值+附件2价值+上一物品在价格（j-主键价格-附件2价格）时对应的价值）,
                result[i][j] = max(result[i][j], result[i - 1][j], result[i - 1][j - weight[i][0] - weight[i][2]] + value[i][0] + value[i][2])
                # 根据3件物品价格之和必然大于等于2件物品的规则，只有在能容纳主件和附件2时，才有判断全部容纳可能性的必要
                if j >= (weight[i][0] + weight[i][1] + weight[i][2]):
                    # 当判断通过，则判断当前值与上物品计算当前价格价值与当前3物品情况价值中最大值，同时还要比较目前最优值
                    result[i][j] = max(result[i][j], result[i - 1][j], result[i - 1][j - weight[i][0] - weight[i][1] - weight[i][2]] + value[i][0] + value[i][1] + value[i][2])
        else:
            # 当前价格j不能容下第i个主件时,价值为上一个物品的对应价格的价值
            result[i][j] = result[i - 1][j]
print(result[things][money] * 10)