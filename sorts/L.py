distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

distances.sort()
prices.sort(reverse=True)

total_price = 0
for i in range(len(distances)):
    total_price += distances[i] * prices[i]

print(total_price)