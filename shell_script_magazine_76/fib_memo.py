#メモ化アルゴリズム
memo = [0] * 1000
memo[0] = memo[1] = 1
def fib(n):
    if memo[n - 1] == 0:
        memo[n - 1] = fib(n - 1)
    if memo[n - 2] == 0:
        memo[n - 2] = fib(n - 2)
    if memo[n] == 0:
        memo[n] = memo[n - 1] + memo[n - 2]
    #print(memo)
    return memo[n]
print(fib(100)) 