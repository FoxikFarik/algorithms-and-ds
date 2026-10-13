def bin_search(el, arr):
    l, r = -1, len(arr)
    while(r - l > 1):
        mid = (l + r) // 2
        if arr[mid] == el:
            return 1
        if el > arr[mid]:
            l = mid
        else:
            r = mid
    return 0

N, K = map(int, input().split())
main_arr = list(map(int, input().split()))
search_list = list(map(int, input().split()))
for el in search_list:
    if bin_search(el, main_arr):
        print("YES")
    else:
        print("NO")