#フィボナッチ数
def fib(n):
    return (fib(n - 1) + fib(n - 2) if n > 1 else 1)
    
print(fib(10))