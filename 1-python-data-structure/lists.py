mylist = ['banana', 'cherry', 'apple']
# print(mylist)

mylist2 = [5, True, "apple", "apple"]
# print(mylist2)

#check the item exists in the list
if 'banane' in mylist:
    print('yes')
else:
    print('no')

#create a list with multiplication with list
mylist = [0] * 5

#create a list from another by function
mylist = [1,2,3,4,5,6]
b = [i*i for i in mylist]

#add the two lists
new_list = mylist + mylist2

#list slicing
mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[1:5]
a = mylist[::5]
a = mylist[::-1]

#copy list
mylist = ['banana', 'cherry', 'apple']
list_cpy = mylist  #both lists refer the same list in the memory
#these three methods can be used to real copy
list_cpy = mylist.copy()
list_cpy = list(mylist)
list_cpy = mylist[:]









