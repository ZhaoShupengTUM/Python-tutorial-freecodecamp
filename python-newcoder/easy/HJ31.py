# reverse the word

while True:
    try:
        out_arr = [] 
        in_arr = input()
        
        for i in in_arr:
            if not i.isalpha():
                in_arr = in_arr.replace(i,' ')

        for j in in_arr.split():  
            out_arr.append(j)
        print(" ".join(out_arr[::-1]))
    except:
        break