line = input().split()
n_word = int(line[0])
words = line[1:1+n_word]
brother_words = []
original = line[-2]
k = int(line[-1])

#find the brother words
for i in words:
    if sorted(i) == sorted(original) and i!=original :
        brother_words.append(i)
        
#sort the words
brother_words.sort()

print(len(brother_words))
if len(brother_words) and k <= len(brother_words):
    print(brother_words[k-1])
    