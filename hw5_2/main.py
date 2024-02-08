import re
from typing import Callable
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

# def generator_numbers(text: str):
#     for item in text.split(" "):
#         try:
#             item = float(item)
#             yield item
#         except ValueError:
#             pass
def generator_numbers(text: str) -> float:
        mask = r"\s-?\d+\.?\d+?\s" 
        for item in re.findall(mask, text):
            yield float(item)

def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))


def main():
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

if __name__ == "__main__":
    main()