#create a tupel
mytupel = ('Max', 28, "Boston")

mytupel = ("Max")  #not a tuple but a string
# print(type(mytupel)) 
mytupel = ("Max",) #this will be recognized as tupel
# print(type(mytupel))

mytupel = tuple(['Max', 28, "Boston"])

#access element
item = mytupel[0]
item = mytupel[-1]

#no change of the tuple, imutable

#check existing
if "Max" in mytupel:
    print("yes")

#find and count
mytupel = ('a', 'p', 'p', 'l', 'e')
len(mytupel)
mytupel.count('a')
mytupel.index('p') #ValueError

mylist = list(mytupel)

#slice 
mytupel = (1,2,3,4,5,6,7,8,9)
b = mytupel[2:5]
b = mytupel[:5]
b = mytupel[2:]
b = mytupel[::2]
b = mytupel[::-1]

#unpacking
mytupel = "Max", 28, "Boston"  #the tuple defined by the , not the()
name, age, city = mytupel
mytupel = (1,2,3,4,5,6,7,8,9)
i1, *i2, i3 = mytupel  #the i2 will be list which is part of the tuple

#tuple can be more efficient
#tuple is smaller as list storing the same data
#also creating time
import timeit
print(timeit.timeit(stmt="[1,2,3,4]", number=1000000) )
print(timeit.timeit(stmt="(1,2,3,4)", number=1000000) )


















