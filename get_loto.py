import random as rd
def pred_loto(ptn):
    rd.seed()
    if ptn == "l7":
        return get_loto(37,7)
    elif ptn == "l6":
        return get_loto(43,6)
    elif ptn == "ml":
        return get_loto(31,5)
    elif ptn == "n3":
        return get_num(3) 
    elif ptn == "n4":
        return get_num(4)
    elif ptn == "b5":
        return bingo5()
    elif ptn == "ks":
        return kisekae()

    else:
        return "引数がまちがっています。"
def get_loto(num,cnt):
    rd.seed()
    set_num = set()
    while True:
        s = rd.randint(1,num)
        set_num.add(s)
        if len(set_num) == cnt:
            list_loto = list(set_num)
            list_loto.sort(key=None,reverse=False)
            return list_loto
            break

def get_num(num):
    rd.seed()
    if num == 3:
        s = rd.randint(0,999)
        str_s = str(s)
        if len(str_s) == 1:
            return "00" + str_s
        elif len(str_s) == 2:
            return "0" + str_s
        elif len(str_s) == 3:
            return str_s
        else:
            return "引数エラー" 
    elif num == 4:
        s = rd.randint(0,9999)
        str_s = str(s)
        if len(str_s) == 1:
            return "000" + str_s
        elif len(str_s) == 2:
            return "00" + str_s
        elif len(str_s) == 3:
            return "0" + str_s
        elif len(str_s) == 4:
            return str_s
        else:
            return "引数エラー"
    else:
        "引数エラー"
def bingo5():
    result = []
    s = 1
    e = 5
    r = 0
    for _ in range(8):
        r = rd.randint(s,e)
        result.append(r)
        r = 0
        s += 5
        e += 5
    return result

def kisekae():
    sel_list = ["メロン","ぶどう","みかん","もも","りんご"]
    result = []
    for _ in range(4):
        result.append(sel_list[rd.randint(0,4)])
    return result

ptn = input("くじ入力。(ロト７:l7、ロト６:l6、ミニロト:ml、ナンバーズ３:n3、ナンバーズ４:n4、BINGO5:b5、きせかえ:ks)： ")
print(pred_loto(ptn))
    
