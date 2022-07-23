phrase = "Giraffe Academy"
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper())
print(len(phrase))

#get individual character
print(phrase[0])
#find the specific character
print(phrase.index("G"))
print(phrase.index("Acad"))
#replace the character
print(phrase.replace("Giraffe", "Elephant"))

#find the char in a string, in可以找字符或者字符串是否出现在另一个字符串中
char = 'a'
mystr = 'freecampdpde'
if char in mystr:
    print("yes")

#compare two chars using their ASCII code value