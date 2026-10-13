def bin_search(C):
    l, r = 0, 10**5
    for _ in range(100):
        x = (l + r) / 2
        if C > (x**2 + x**0.5):
            l = x
        else:
            r = x
    return x

C = float(input())
print(bin_search(C))