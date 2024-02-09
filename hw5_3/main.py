from collections import defaultdict
import argparse

#ініціалізація парсера, додавання ключів
parser = argparse.ArgumentParser(description='Logfile parcer') 
parser.add_argument("filename", help="Logfile path")
parser.add_argument("-info", required=False, default=False, help="Display INFO records", action="store_true")
parser.add_argument("-debug", required=False, default=False, help="Display DEBUG records", action="store_true")
parser.add_argument("-error", required=False, default=False, help="Display ERROR records", action="store_true")
parser.add_argument("-warning", required=False, default=False, help="Display WARNING records", action="store_true")

args = parser.parse_args() #парсинг командної строки

# default_path = "hw5_3\\logfile.log"

def load_logs(file_path: str) -> list:

    def parse_log_line(line: str) -> dict:
        line = line.split(" ", 3) #розділення строки на дату, час, рівень та опис
        struct = ("date", "time", "level", "description") #створення ключів словнику
        return dict(zip(struct, line)) #створення словнику строки
    
    list_logs = [] #створення списку словників строк  
    try:
        with open(file_path, "r") as file: #відкриття файлу
            while True:
                line = file.readline() #зчитування строк поки не закінчаться
                if not line:
                    return list_logs #повернення списку словників
                list_logs.append(parse_log_line(line)) #парсинг та додавання строки до списку
    except FileNotFoundError: #обробка помилки filenot found
        print('File not found')
        exit()


def filter_logs_by_level(logs: list, level: str) -> list:
    level_list = [] #створення списку відфільтрованих строк
    for item in logs:
        if item["level"].lower() == level: 
            level_list.append(item) #додавання до списку строк з рівнем level
    return level_list

def count_logs_by_level(logs: list) -> dict:
    level_dict = defaultdict(int) #створення словнику рівнів
    for item in logs:
        level_dict[item["level"]] +=1 #підрахунок рівнів та додавання до словника
    return dict(level_dict) 

def display_log_counts(counts: dict):
    column1 = "Рівень логування " #шапка таблиці
    column2 = "| Кількість"
    width_col1 = len(column1) #ширина першї колонки
    width_col2 = len(column2) #ширина другої колонки
    print("\n" + column1 + column2) #друк шапки
    print("-" * width_col1 + "|" + "-" * width_col2) #друк роздільника
    for key, value in counts.items():
        print(f"{key:<{width_col1}}| {value:<{width_col2}}") #друк елементів таблиці
    print()
    
def main():
    def print_debug(list_logs):
        for rec in list_logs:
            print(rec["date"], end = " ") #друк дати
            print(rec["time"], end = " - ") #друк часу
            print(rec["description"], end = "") #друк опису

    logs = load_logs(args.filename) #читання файлу логів
    counts = count_logs_by_level(logs) #підрахунок рівнів помилок
    display_log_counts(counts) #друк таблиці рівнів логування
    if args.info:
        print(f"Деталі логів для рівня INFO:")
        print_debug(filter_logs_by_level(logs, "info")) #друк строк з рівнем "info"
    if args.debug:
        print(f"Деталі логів для рівня DEBUG:")
        print_debug(filter_logs_by_level(logs, "debug")) #друк строк з рівнем "debug"
    if args.error:
        print(f"Деталі логів для рівня ERROR:")
        print_debug(filter_logs_by_level(logs, "error")) #друк строк з рівнем "error"
    if args.warning:
        print(f"Деталі логів для рівня WARNING:")
        print_debug(filter_logs_by_level(logs, "warning")) #друк строк з рівнем "warning"
    
    
if __name__ == "__main__":
    main()