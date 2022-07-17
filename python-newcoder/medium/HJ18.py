import sys
 
res = [0,0,0,0,0,0,0]  #store the result
 
def puip(ip):
    if 1 <= ip[0] <= 126:             # A类地址判断条件
        res[0] += 1
    elif 128 <= ip[0] <= 191:         # B类地址判断条件
        res[1] += 1
    elif 192 <= ip[0] <= 223:         # C类地址判断条件
        res[2] += 1
    elif 224 <= ip[0] <= 239:         # D类地址判断条件
        res[3] += 1
    elif 240 <= ip[0] <= 255:         # E类地址判断条件
        res[4] += 1
    return
 
def prip(ip):           # 私有IP地址判断条件
    if (ip[0] == 10) or (ip[0] == 172 and 16 <= ip[1] <= 32) or (ip[0] == 192 and ip[1] == 168):
        res[6] += 1
    return
 
def ym(msk):
    val = (msk[0] << 24) + (msk[1] << 16) + (msk[2] << 8) + msk[3]    # 获取32位的掩码表示
    s = bin(val)[2:]                                                  # 去除“0b”字符，并转换成字符串, bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
    pos0 = s.find('0')                                                # 从左往右找到0第一次出现的位置
    pos1 = s.rfind('1')                                               # 从右往左找到1第一次出现的位置
    if pos0 != -1 and pos1 != -1 and pos0 - pos1 == 1:                # 判断两个位置是否相差1，且是否找不到
        return True
    return False
     
 
def judge(line):
    ip, msk = line.strip().split('~')
    ips = [int(x) for x in filter(None, ip.split('.'))]             # 获得表示IP的列表，理论上应该包含四个元素
    #filter(None, ip.split('.')) removes the all empty strings from a list of strings 
    msks = [int(x) for x in filter(None, msk.split('.'))]           # 获得表示掩码的列表，理论上应该包含四个元素
    if ips[0] == 0 or ips[0] == 127:                                # 排除非法IP不计数
        return
    if len(ips) < 4 or len(msks) < 4:                               # 判断错误掩码或错误IP
        res[5] += 1
        return
    if ym(msks) == True:                                            # 通过掩码判断的可以进行IP判断
        puip(ips)
        prip(ips)
    else:
        res[5] += 1
    return
 
for line in sys.stdin:
    judge(line)
# judge("192.168.0.2~255.255.255.0")
 
res = [str(x) for x in res]
print(" ".join(res))

# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
# filter(function, iterable)