def format_total(kopecks: int) -> str:
    rubles, remainder = divmod(kopecks, 100)
    return f"Итого: {rubles}.{remainder:02d} руб."
