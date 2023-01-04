#バブルソート
def bubble_sort(x):
    y = x[:]
    for i in range(len(y) - 1):
        for j in range(len(y) - 1,i,-1):
            if y[j - 1] > y[j]:
                tmp = y[j - 1]; y[j - 1] = y[j]; y[j] = tmp
        print(y)
    return y
x = [4,8,6,10,30,7,1,4,2]
print(bubble_sort(x))