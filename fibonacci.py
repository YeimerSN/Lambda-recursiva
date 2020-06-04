fibonacci = lambda x : 0 if x == 0 else 1 if 0 < x <= 2 else fibonacci(x - 1) + fibonacci(x - 2)
print(fibonacci(20))
