def total_kopecks(prices: list[int]) -> int:
    if any(price < 0 for price in prices):
        raise ValueError("Цена не может быть отрицательной")
    return sum(prices)
