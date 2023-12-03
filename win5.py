import random as rd
def get_horse_no(num):
    rd.seed()
    return(str(rd.randint(1,int(num))))
result_list = []
race_cnt = 1
for _ in range(5):
    tou = input(str(race_cnt) + "レース目の頭数を入力してください：")
    race_cnt += 1
    result_list.append(get_horse_no(tou))
print(result_list)