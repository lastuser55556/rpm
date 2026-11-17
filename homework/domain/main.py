import csv
from pathlib import Path


class InvalidSale(ValueError):
    pass


def total_sales(path: Path) -> int:
    with path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != ["sale_id", "amount_kopecks"]:
            raise InvalidSale("Неверный заголовок")
        total = 0
        seen = set()
        for row in reader:
            sale_id = row["sale_id"]
            if not sale_id or sale_id in seen:
                raise InvalidSale(f"Повторный или пустой ID, строка {reader.line_num}")
            try:
                amount = int(row["amount_kopecks"])
            except (TypeError, ValueError) as error:
                raise InvalidSale(f"Некорректная сумма, строка {reader.line_num}") from error
            if amount <= 0:
                raise InvalidSale(f"Сумма должна быть положительной, строка {reader.line_num}")
            seen.add(sale_id)
            total += amount
    return total
