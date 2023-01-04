def bin_sort(x):
    s = max(x)
    s_list = [0] * (s + 1)
    for i in x:
        #print(i)
        s_list[i] = i
    result = []
    for j in s_list:
         if j != 0:
             result.append(j)
    return result
x = [4,7,1,98,9,2,1000]
print(bin_sort(x))
