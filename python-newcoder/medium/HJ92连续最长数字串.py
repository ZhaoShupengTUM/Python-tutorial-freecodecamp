#利用栈的思想

while True:
    try:
        line = input()

        stack = []
        res = []
        #数字入栈，字母不入栈，作为数字出栈的信号
        for i in line:
            if i.isdigit():
                stack.append(i)

            else:
                if len(stack):
                    res.append(''.join(stack))
                    stack.clear()
                else:
                    pass
        if len(stack):
            res.append(''.join(stack))
        
        #res中存储了所有的数字串
        if len(res):
            length = list(map(len, res))
            for i in res:
                if len(i) == max(length):
                    print(i, end='')
            print(',' + str(max(length)))
        else:
            print('')
            
    except:
        break