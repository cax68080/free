# 線形探索と二分木探索を比較する。
# 線形探索
def liner_search(data,key):
    position = 0
    end = len(data)
    steps = 1
    while position <= end:
        if data[position] == key:
            return steps,position
        steps += 1
        position += 1
    return steps,-1

# 二分木探索
def binary_search(data,key):
    start = 0
    end = len(data) - 1
    steps = 1
    while start <= end:
        middle = (start + end) // 2
        if data[middle] == key:
            return steps,middle
        elif data[middle] < key:
            start = middle + 1
        else:
            end = middle - 1
        steps += 1
    return steps,-1

# 探索の実行と最大ステップ数を求める処理
def search(title,data,func):
    print(title)
    max_steps = 1
    keys = [1,50,100,500,900]
    for key in keys:
        steps,pos = func(data,key)
        if max_steps < steps:
            max_steps = steps
        print("key:{} position:{} steps:{}".format(key,pos,steps))
    print("最大ステップ数:{}\n".format(max_steps))
    return

if __name__ == "__main__":
    #data = [1,3,7,17,21,74]
    data = list(range(1000))    # 0から999までのリストを作成
    length = len(data)
    print("探索データ:{}\n長さ:{}\n".format(data,length))
    search("線形探索",data,liner_search)
    search("二分木探索",data,binary_search)