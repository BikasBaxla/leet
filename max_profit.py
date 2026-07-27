def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
                max_profit = profit

    return profit
prices = [14,9,5,11,3,8,16,10]
print(maxProfit(prices))