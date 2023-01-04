#ヒープソート
from heapq import heappush,heappop

def heap_sort(x):
    retary = []
    heap = []
    for i in x:
        heappush(heap,i)
    while len(heap) > 0:
        retary.append(heappop(heap))
    return retary
x = [1,8,3,2,4,9,12,28,16,20,21]
print(heap_sort(x))

