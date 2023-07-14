'''
 A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
'''

#create
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)    

a = set('abracadabra')
b = set('alacazam') # unique letters in a
a - b # letters in a but not in b
a | b # letters in a or b or both
a & b # letters in both a and b
a ^ b # letters in a or b but not both

