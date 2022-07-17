#count the different type of chars

while True:
    try:
        sentence = input()
        word, space, digit, other = 0, 0, 0, 0
        for i in sentence:
            if i.isalpha():
                word += 1
            elif i == ' ':
                space += 1
            elif i.isdigit():
                digit += 1
            else:
                other += 1
        print(word)
        print(space)
        print(digit)
        print(other)
    except:
        break