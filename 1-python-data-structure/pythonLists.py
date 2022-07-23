friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
lucky_number = [4, 8, 15, 16, 23, 42]

print(friends[0])
print(friends[-1])  #-1 is the last element
print(friends[1:])
print(friends[1:3])  #get the elements until the third element

friends[1] = "Mike"

#list functions
friends.extend(lucky_number)
friends.append("Creed")
friends.insert(1, "Kelly")

friends.remove("Jim")
friends.clear()
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()  #pop the last element

friends.index("Kevin")

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim"))

friends.sort()  #change the original list
sorted(friends)  #dont change the original list
friends.reverse()  #reverse dont return any values

friends2 = friends.copy()
print(friends2)