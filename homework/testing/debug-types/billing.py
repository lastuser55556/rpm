from decimal import Decimal, ROUND_HALF_UP


def total(price: Decimal, quantity: int, discount_percent: int) -> Decimal:
    if price < 0 or quantity < 1 or not 0 <= discount_percent <= 100:
        raise ValueError("Проверьте цену, количество и скидку")
    rate = Decimal(100 - discount_percent) / 100
    return (price * quantity * rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
