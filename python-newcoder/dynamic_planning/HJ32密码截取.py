#动态递归
s = input()
n = len(s)

maxlen = 1
dp = [ [False for k in range(n)] for i in range(n) ]

for i in range(n):
    for j in range(i+1):
        if i == j:
            dp[j][i] = True
        elif i-j == 1:
            dp[j][i] = (s[i] == s[j])
        else:
            dp[j][i] = (s[i] == s[j] and dp[j + 1][i - 1])
            
        if dp[j][i] and i - j + 1 > maxlen: 
            maxlen = i - j + 1

print(maxlen) 



# # #violent solution
# mycode = input()
# length = 1

# for i in range(len(mycode)):
#     for j in range(i+1, len(mycode)+1):
#         sonstr = mycode[i:j]
#         sonstrre = list(mycode[i:j])
#         sonstrre.reverse()
#         sonstrre = ''.join(sonstrre)
#         if sonstr == sonstrre and len(sonstr) > length:
#             length = len(mycode[i:j])
            
# print(length)

#fenleitaolun
s = input()
# 从右到左，对每个字符进行遍历处理，并且每个字符要处理两次，因为回文子串有两种情况：
# ABA型：只需要从当前字符向两边扩散，比较左右字符是否相等，找出以当前字符为中心的最长回文子串长度
# ABBA型：只需要从当前字符和下一个字符向两边扩散，比较左右字符是否相等，找出以当前字符和下一个字符为中心的最长回文子串长度
# 最后比对两种类型的长度，取自较长的长度
out = 0

for i in range(0, len(s)):  # 双指针
    k = i - 1
    j = i + 1
    len_ABA = 1
    while k >= 0 and j < len(s):
        if s[k] == s[j]:
            k -= 1
            j += 1
            len_ABA += 2
        else:
            break
    
    k = i
    j = i + 1
    len_ABBA = 0
    while k >= 0 and j < len(s):
        if s[k] == s[j]:
            k -= 1
            j += 1
            len_ABBA += 2
        else:
            break
     
    now_len = max(len_ABA, len_ABBA)
    if out < now_len:
        out = now_len
print(out)

# include<iostream>
# include<string>
# include<algorithm>
# include<vector>
# using namespace std;

# int main(){
#     string s;
#     while(cin >> s){
#         int n = s.length();
#         vector<vector<bool> > dp(n, vector<bool>(n, false)); //dp[j][i]=1表示从j到i是回文子串
#         int maxlen = 1; //初始为1
#         for(int i = 0; i < n; i++){
#             for(int j = 0; j <= i; j++){
#                 if(i == j) //奇数长度子串
#                     dp[j][i] = true;
#                 else if(i - j == 1) //偶数长度子串
#                     dp[j][i] = (s[i] == s[j]);
#                 else
#                     dp[j][i] = (s[i] == s[j] && dp[j + 1][i - 1]); //这两个字符相等，同时中间缩也要相等
#                 if(dp[j][i] && i - j + 1 > maxlen) //取最大
#                     maxlen = i - j + 1;
#             }
#         }
#         cout << maxlen << endl;
#     }
#     return 0;
# }

            
