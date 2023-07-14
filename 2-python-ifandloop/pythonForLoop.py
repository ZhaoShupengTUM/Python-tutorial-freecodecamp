#String
for letter in "Giraffe Academy":
    print(letter)


#Sequence 
friends = ["jim", "karen", "kevin"]
for name in friends:
    print(name)

#enumerate
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

#zip
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#range
for index in range(10):
    if index == 0:
        print("first interation")
    else:
        print("Not first interation")

for index in range(3, 10):
    print(index)

#reversed()
for i in reversed(range(1, 10, 2)):
    print(i)

#loop the dictionaries
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k,v, sep='')

