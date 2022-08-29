'''1. 利用栈的思想'''

s=str(input())
stack=[] #栈 存储当前字符串
l=[] #列表 存储全部字符串
counter=0 #字符串计数器
for i in s: 
    if i=='"' and '"' in stack: #引号分割的参数
        l.append(''.join(stack[1::]))  #取出从第一个引号开始的参数
        stack=[]
        counter+=1
    elif i==' ' and '"' not in stack: #空格分隔的参数
        if len(stack)!=0:  #防止连续空格情况
            l.append(''.join(stack[0::]))
            stack=[]
            counter+=1
    else: #加入参数
        stack.append(i)
if len(stack)!=0: #最后再看下栈中是否还有字符串
    l.append(''.join(stack[0::]))
    counter+=1
print(counter)
for j in l:
    print(j)