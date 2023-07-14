'''
Immutable Sequence Types
hash()
'''
#create 
coordinates = (4, 5)
t = 12345, 54321, 'hello!'
v = ([1, 2, 3], [3, 2, 1])
v[0][0] = 2
empty = () #empty tupels
mytupel = ('Max', 28, "Boston")
mytupel = ("Max")  #not a tuple but a string
mytupel = ("Max",) #a tuple with one item is constructed by following a value with a comma
mytupel = tuple(['Max', 28, "Boston"])


#unpacking
mytupel = "Max", 28, "Boston"  #the tuple defined by the , not the()
name, age, city = mytupel
mytupel = (1,2,3,4,5,6,7,8,9)
i1, *i2, i3 = mytupel  #the i2 will be list which is part of the tuple


#check existing
if "Max" in mytupel:
    print("yes")


#transform
mylist = list(mytupel)

#tuple can be more efficient
#tuple is smaller as list storing the same data
#also creating time
import timeit
print(timeit.timeit(stmt="[1,2,3,4]", number=1000000) )
print(timeit.timeit(stmt="(1,2,3,4)", number=1000000) )


