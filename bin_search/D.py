def f(a, b, c, d, x):
    return a*x**3 + b*x**2 + c*x + d

def bin_search(a, b, c, d):
    l, r = -10**9, 10**9
    for _ in range(100):
        x = (l + r) / 2
        if f(a, b, c, d, l)*f(a, b, c, d, x) <= 0:
            r = x
        else:
            l = x
    return (l + r) / 2

a, b, c, d = map(int, input().split())
print(bin_search(a, b, c, d))