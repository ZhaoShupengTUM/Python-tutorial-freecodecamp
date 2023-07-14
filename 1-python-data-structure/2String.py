'''
\' = '
\n = enter
'''

#
print(r'C:\some\name') #raw strings

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")  #print multiple lines


#String concatenate
print(3 * 'un' + 'ium')

print('Py''thon')

text = ('Put several strings within parentheses '
         'to have them joined together.'
         'something')
print(text)


#String index and slices
'''
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
the start is always included, 
the end is always excluded,
the length is the difference of the indices
python strings are imutable
'''
word = "Python"
word[0:2]
word[2:]
word[:-2]


#String functions
len(word)


#String methods
phrase = "Giraffe Academy"
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper())
print(len(phrase))

print(phrase.index("G")) #find the specific character, retun index
print(phrase.index("Acad")) #return the index pf 'A'

print(phrase.replace("Giraffe", "Elephant"))  #replace the character

#find the char in a string, in可以找字符或者字符串是否出现在另一个字符串中
char = 'a'
mystr = 'freecampdpde'
if char in mystr:
    print("yes")

#compare two chars using their ASCII code value