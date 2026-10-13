def bin_search(el, arr):
    l, r = -1, len(arr)
    mid = (l + r) // 2
    while(r - l > 1):
        mid = (l + r) // 2
        if arr[mid] == el:
            return arr[mid]
        if el <= arr[mid]:
            r = mid
        else:
            l = mid
    
    if l == -1:
        return arr[r]
    if r == len(arr):
        return arr[l]
    
    if abs(arr[l] - el) <= abs(arr[r] - el):
        return arr[l]
    return arr[r]

N, K = map(int, input().split())
main_arr = list(map(int, input().split()))
search_list = list(map(int, input().split()))
for el in search_list:
    print(bin_search(el, main_arr))