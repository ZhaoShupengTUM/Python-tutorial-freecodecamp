'''
Dictionaries are indexed by keys, 
which can be any immutable type.
It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary).

'''

#create
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
tel = {'jack': 4098, 'sape': 4139}
tel = dict(sape=4139, guido=4127, jack=4098)
empty_dic = {}
comprehensions_dict = {x: x**2 for x in (2, 4, 6)}
# print(comprehensions_dict)

#access the value through key
print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv", "Not a valid key"))

#add
tel['irv'] = 4127

#delete
del tel['sape']

#dict-list conversion
list(monthConversions) #the keys are converted to the dictionaries
print(sorted(monthConversions))



