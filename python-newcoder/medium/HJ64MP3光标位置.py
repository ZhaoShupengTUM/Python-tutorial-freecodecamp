nsongs = int(input())
command = input()

songlist = list(range(1, nsongs+1))

#down and up will always change the pointer
pointer = 1
page = songlist[:4]

for i in command:
    if i == 'U':
        if pointer == 1:  #特殊翻页
            pointer = nsongs
            page = songlist[-4:]
        else:
            if pointer == page[0]:  #一般翻页
                page = list(range(pointer-1, pointer+3))
            else:  #不翻页
                pass
            pointer -= 1        
    elif i == 'D':
        if pointer == nsongs:  #特殊翻页
            pointer = 1
            page = songlist[:4]
        else:
            if pointer == page[-1]:  #一般翻页
                page = list(range(pointer-2, pointer+2))
            else:  #不翻页
                pass
            pointer += 1
            
print(' '.join(map(str, page)))
print(pointer)