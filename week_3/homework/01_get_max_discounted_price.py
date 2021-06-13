# 제일 할인을 많이 받으려면..?
shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    n = len(prices)
    for i in range(1, n):
        for j in range(i):
            if prices[i -j - 1] < prices[i - j]:
                prices[i - j - 1], prices[i - j] = prices[i - j], prices[i - j - 1]
    m = len(coupons)
    for i in range(1, m):
        for j in range(i):
            if coupons[i -j - 1] < coupons[i - j]:
                coupons[i - j - 1], coupons[i - j] = coupons[i - j], coupons[i - j - 1]
    total = 0
    if n > m:
        for i in range(m):
            total += prices[i] * ((100 - coupons[i])/100)
        for i in range(m,n):
            total += prices[i]
    else:
        for i in range(n):
            total += prices[i] * ((100 - coupons[i])/100)

    return total


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.