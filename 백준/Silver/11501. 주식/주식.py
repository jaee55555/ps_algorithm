import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    stocks = list(map(int, sys.stdin.readline().split()))

    max_price = 0
    profit = 0

    for price in reversed(stocks):
        if price > max_price:
            max_price = price
        else:
            profit += max_price - price

    print(profit)
