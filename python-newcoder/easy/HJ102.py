while True:
    try:
        list1 = []
        arr = input()
        dic = {}
        for i in arr:
            if not (i.isalpha() or i.isdigit() or i.isspace()):
                continue
            else:
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
        # dic.items() return a special class of dict_items which contains key and value and are iterable
        dic = sorted(dic.items(), key=lambda x: x[0])  # 先按字符ASC排
        dic = sorted(dic, key=lambda x: x[1], reverse=True)  # 再按统计数目排，从大到小
        print(''.join(k for (k, v) in dic))
    except:
        break