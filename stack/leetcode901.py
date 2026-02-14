def stockSpanner(price):
    n = len(price)
    stack = []
    result = [1] * n

    for i, num in enumerate(price):
        while stack and price[stack[-1]] <= num:
            stack.pop()

        if stack:
            result[i] = i - stack[-1]

        stack.append(i)

    return result

price = [100, 80, 60, 70, 60, 75, 85]

print(stockSpanner(price))




class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))
        return span
