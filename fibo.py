# 斐波那契(fibonacci)数列模块

# __all__ = ['fib','fib2','fib_attr']

fib_attr = 100
sum0 =111
def fib(n):  # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

def fib3(n):
    return n*2