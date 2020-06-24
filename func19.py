from functools import reduce
fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],range(n - 2), [0, 1])
n=int(input('Enter number of terms: '))
print(fib(n))