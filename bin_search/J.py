def good(n, a, b, w, h, d):
    if (w // (a + 2*d)) * (h // (b + 2*d)) >= n or \
        (w // (b + 2*d)) * (h // (a + 2*d)) >= n:
        return True
    return False

def bin_search(n, a, b, w, h):
    l, r = 0, max(w, h)
    while(r - l > 1):
        m = (l + r) // 2
        if good(n, a, b, w, h, m):
            l = m
        else:
            r = m
    return l

n, a, b, w, h = map(int, input().split())
print(bin_search(n, a, b, w, h))