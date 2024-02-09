import re
from typing import Callable
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

# def generator_numbers(text: str): #пошук натуральних чисел в рядку варіант 1
#     for item in text.split(" "):
#         try:
#             item = float(item) #привід елементу рядку до float
#             yield item #повернення числа
#         except ValueError: #якшо помилка: пропуск елементу
#             pass
def generator_numbers(text: str) -> float: #пошук натуральних чисел в рядку варіант 2
        mask = r"\s-?\d+\.?\d+?\s"  #шаблон для почуку натуральних чисел (в тому числі від'ємних)
        for item in re.findall(mask, text):
            yield float(item) #привід елементу рядку до float

def sum_profit(text: str, func: Callable) -> float: #сума всіх чисел в рядку
    return sum(func(text))


def main():
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}") #друк результату

if __name__ == "__main__":
    main()