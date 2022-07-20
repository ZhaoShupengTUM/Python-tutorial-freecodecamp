"""
注意string.replace()返回一个新的字符串，对原字符串并无修改
"""
while True:
    try:
        string = input()
        out = ''
        for i in string:
            if i.isdigit():
                out += "*"+i+"*"
            else:
                out += i
        out = out.replace("**", "")
        print(out)
    except:
        break