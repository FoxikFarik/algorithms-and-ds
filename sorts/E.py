def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    larr = merge_sort(arr[:mid])
    rarr = merge_sort(arr[mid:])
    
    return merge(larr, rarr)

def merge(larr, rarr):
    arr = []
    
    i = 0
    j = 0
    while i < len(larr) and j < len(rarr):
        if larr[i] < rarr[j]:
            arr.append(larr[i])
            i += 1
        else:
            arr.append(rarr[j])
            j += 1
    
    arr.extend(larr[i:])
    arr.extend(rarr[j:])
    return arr


N = int(input())
arr = list(map(int, input().split()))
arr = merge_sort(arr)
print(*arr)