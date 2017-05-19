while True:
    try:
        bsum = 0
        bproduct = 1
        ope = "*"
        svalue = ""

        print('計算式を入力してください（eで終了）')
        inp = input('>> ')
        if inp == 'e':
            break
        inp += "+"        

        for c in inp:
            if c == "*" or c == "/" or c == "+" or c == "-":
                value = float(svalue)
                svalue = ""
                if ope == "*":
                    bproduct *= value
                else:
                    bproduct /= value
                if c == "+" or c == "-":
                    bsum += bproduct
                    if c == "+":
                        bproduct = 1
                    else:
                        bproduct = -1
                    ope = "*"
                else:
                    ope = c                
            else:
                svalue += c        

        print(str(bsum).rstrip('.0'))        
    except:
        print('エラー')

print ('Good bye.')
