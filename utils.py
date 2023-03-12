import calendar
import random


def get_random_date(month: int, year: int) -> str:
    days = calendar.monthrange(year, month)[1]
    return f"{year}-{month}-{random.randint(1, days)}"
