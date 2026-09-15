from functools import cmp_to_key


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def compare(point_a, point_b):
    dist_a = point_a.x ** 2 + point_a.y ** 2
    dist_b = point_b.x ** 2 + point_b.y ** 2
    if dist_a < dist_b:
        return -1
    elif dist_a == dist_b:
        return 0
    else:
        return 1


n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))
    
points.sort(key=cmp_to_key(compare))

for point in points:
    print(point.x, point.y)
