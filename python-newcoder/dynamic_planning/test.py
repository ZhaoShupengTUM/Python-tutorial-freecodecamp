# # dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
# # print(type(dishes.items()))

# msk = '255.255..10'
# msk = [int(x) for x in filter(None, msk.split('.'))]   #this can remove the empty elements in a list
# val = (msk[0] << 24) + (msk[1] << 16) + (msk[2] << 8) + msk[3]
# print(msk)

# print(2 << 3)  #change the number to binary, move bits, then return an int

#the right method to buid a 2d list
# list2d = [ [i for i in range(5)] for k in range(5) ]
# print(list2d)
# list2d = [ [0]*5 for i in range(5) ]
# print(list2d)

#use lambda with filter to pick up the certain elements from a list
# cmd_set = ['reset', 'reset board', 'board add', 'board delete', 
#               'reboot backplane', 'backplane abort', 'he he']
# startwithr = list(filter(lambda x:x.startswith('r'), cmd_set))
# print(startwithr)

#ascii code: A-65, a-97

# #the use of stack
# line = list('(A(BCDE))')
# print(line)
# stack = []
# for i in line:
#     if i == ')':
#         while stack[-1] != '(':
#             stack.pop()
#         stack.pop()
#     else:
#         stack.append(i)
#     print(stack)

