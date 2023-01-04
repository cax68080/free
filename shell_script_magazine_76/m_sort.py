def merge_sort(x):
    retary = []
    if len(x) <= 1:
        retary.extend(x)
    else:
        m = len(x) // 2
        first = merge_sort(x[:m])
        second = merge_sort(x[m:])
        while len(first) > 0 and len(second) > 0:
            retary.append(first.pop(0) \
                if first[0] < second[0] else second.pop(0))
        retary.extend(first if len(first) > 0 else second)
    return retary
x = [9,7,27,83,6,40,172,67,39,27,11,28,29,76]
print(merge_sort(x))