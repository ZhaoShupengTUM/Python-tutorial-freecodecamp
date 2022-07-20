# code strength level

while True:
    try:
        str_data = input().strip()
        num, up_char, low_char, other, score = 0, 0, 0, 0, 0

        #count the different type of chars
        for data in str_data:
            if data.isdigit():
                num += 1
            elif data.isalpha():
                if data.lower() == data:
                    low_char += 1
                else:
                    up_char += 1
            else:
                other += 1

        #the note for the length
        if len(str_data) < 5:
            score += 5
        elif len(str_data) < 8:
            score += 10
        else:
            score += 25

        # the note for the low or high char
        if up_char==0 and low_char==0:
            pass
        elif (up_char==0 and low_char!=0) or (up_char!=0 and low_char==0):
            score += 10
        else:
            score += 20

        #note for the number    
        if num == 0:
            pass
        elif num == 1:
            score += 10
        else:
            score += 20

        #note for the other chars   
        if other == 0:
            pass
        elif other == 1:
            score += 10
        else:
            score += 25

        #note for the char types    
        if num != 0 and (up_char+low_char) != 0 and other==0:
            score += 2
        elif num != 0 and up_char != 0 and low_char != 0 and other!=0:
            score += 5
        elif num != 0 and (up_char+low_char) != 0 and other!=0:
            score += 3

        #judge the code strength   
        if score >=90:
            print('VERY_SECURE')
        elif score >=80:
            print('SECURE')
        elif score >= 70:
            print('VERY_STRONG')
        elif score >= 60:
            print('STRONG')
        elif score >= 50:
            print('AVERAGE')
        elif  score>=25:
            print('WEAK')
        else:
            print('VERY_WEAK')

        #judge the code strength: the dictionary method
        criterium = ["VERY_SECURE", "SECURE","VERY_STRONG","STRONG","AVERAGE","WEAK", "VERY_WEAK"]
        score_list = [90, 80, 70, 60, 50, 25, 0]

        for i in range(len(criterium)):
            if score >= score_list[i]:
                print(criterium[i])
                break

    except:
        break
