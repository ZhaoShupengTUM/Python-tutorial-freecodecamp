# from numpy import *
n_num = int(input())
num_list = list(map(int, input().split()))

n_neg = 0
ins = 0
avg = []

for num in num_list:
    if num < 0:
        n_neg += 1
    elif num > 0:
        avg.append(num)
    
print( str(n_neg)+" 0.0" if not avg else str(n_neg)+" "+"{0:.1f}".format(sum(avg)/len(avg)) )        
                
# print(n_neg, " ", mean(avg))