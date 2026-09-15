def CountCompare(s1, s2):
    if len(s1) != len(s2):
        return 0
    
    symbols = set(s1)
    if set(s2) != symbols:
        return 0
    
    counts1 = dict()
    counts1 = counts1.fromkeys(symbols, 0)
    counts2 = counts1.copy()
    
    for i in range(len(s1)):
        counts1[s1[i]] += 1
        counts2[s2[i]] += 1
    
    return counts1 == counts2

s1 = input()
s2 = input()

if CountCompare(s1, s2):
    print("YES")
else:
    print("NO")
    