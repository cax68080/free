def fact(n):
    s = 1
    e = n + 1
    result = 0
    for i in range(s,e):
        if i == 1:
            result = i
        else:
            result *= i
    return result

print(fact(15))
