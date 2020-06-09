
def isNumeric(s):
    # write code here
    for i in s:
        if i.isdigit() or i == 'e' or i == 'E' or i == '+' or i == '-' or i == '.':
            pass
        else:
            return False

    if 'e' in s or 'E' in s:
        print('e in s')
        if s.count('e') > 1 or s.count('E') > 1:
            return False
        if 'e' in s:
            ss = s.split('e')
        else:
            ss = s.split('E')
        if s[0]!='E' and s[0]!='e' and s[-1] != 'E' and s[-1] != 'e':
            print(ss)
            num = ss[0]
            print(num)
            int_num = ss[1]
            print(int_num)
            if (num[0] == '+' or num[0] == '-') and num[0] != '0':
                if '+' not in num[1:] and '-' not in num[1:] and num[1] != '0':
                    f1 = True
            elif '+' not in num and '-' not in num and num[0] != '0':
                f1 = True
            else:
                f1 = False
            if (int_num[0] == '+' or int_num[0] == '-') and int_num[0] != '0' and '.' not in int_num:
                if '+' not in int_num[1:] and '-' not in int_num[1:]:
                    if len(int_num[1:]) == 1:
                        f2 = True
                    elif len(int_num[1:]) >= 1 and int_num[1] != '0':
                        f2 = True
                    else:
                        f2 = False
            elif '+' not in int_num and '-' not in int_num and '.' not in int_num:
                if len(int_num) == 1:
                    f2 = True
                elif len(int_num) >= 1 and int_num[0] != '0':
                    f2 = True
                else:
                    f2 = False
            else:
                f2 = False
            if f1 and f2:
                return True
            else:
                return False




        else:
            return False



    else:
        print("no e in s")
        try:
            a = float(s)
            if a:
                return True
        except:
            return False

print(isNumeric("-1E-16"))




