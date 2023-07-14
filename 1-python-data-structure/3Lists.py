'''
Sequence Types: list, Tupel, range
x: an arbitrary object 
s,t: sequences of the same type
n,i,j,k: integers
The operations:
x in s
x not in s
s + t
slice: s[i], s[i,j], s[i:j:k]
len(s)
min(s), max(s)
s.index(x[, i[,j]])
s.count(x)

Mutable Sequence Types:
t: any iterable object
x: an arbitrary object
s[i] = x
s[i:j] = t, s[i:j:k] = t
del s[i:j], s[i:j] = []
s.append(x)
s.clear()
s.copy()
s.extend(t) or s+=t
s *= n
s.insert(i, x)
s.pop() or s.pop(i)
s.remove(x)
s.reverse()
'''

'''
The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.
'''

#create a list
mylist = ['banana', 'cherry', 'apple']
mylist2 = [5, True, "apple", "apple"]
mylist = [0] * 5 #create a list with multiplication with list
mylist = [1,2,3,4,5,6]
b = [i*i for i in mylist] #create a list from another with function
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]  #nested


#Indexed and sliced
squares = [1, 4, 9, 16, 25]
squares[-3:]  # slicing returns a new list
squares[:]  #return the copy
mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[1:5]
a = mylist[::5]
a = mylist[::-1]


#concatenation
squares + [36, 49, 64, 81, 100]


#List operation
#copy
mylist = ['banana', 'cherry', 'apple']
list_cpy = mylist  #both lists refer the same list in the memory
#these three methods can be used to real copy
list_cpy = mylist.copy()
list_cpy = list(mylist)
list_cpy = mylist[:]

#replace
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E'] #assignment to a list slice
letters[2:5] = [] #remove them
letters[:] = [] #clear

#append or extend
cubes.append(216)
friends = ['mike', 'bob', 'jack']
lucky_number = [1, 2, 3, 4, 5]
friends.extend(lucky_number)  

#insert
friends.insert(1, "Kelly")

#check the item exists in the list
if 'banane' in mylist:
    print('yes')
else:
    print('no')

#remove, clear, pop
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.remove("Jim")
friends.clear()
friends.pop()  #pop the last element

#find
friends.index("Kevin")

#count
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim"))

#sort
friends.sort()  #change the original list
sorted(friends)  #dont change the original list
friends.reverse()  #reverse dont return any values








