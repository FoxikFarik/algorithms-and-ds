import sys
from functools import cmp_to_key


def compare(A, B):
    if A + B > B + A:
        return -1
    elif A + B == B + A:
        return 0
    else:
        return 1

nums = list(map(str, sys.stdin.read().split()))
nums.sort(key=cmp_to_key(compare))
print(''.join(nums))
