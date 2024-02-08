from collections import defaultdict
import argparse

parser = argparse.ArgumentParser(description='Logfile parcer')
parser.add_argument("filename", help="Logfile path")
parser.add_argument("-info", required=False, default=False, help="Display INFO records", action="store_true")
parser.add_argument("-debug", required=False, default=False, help="Display DEBUG records", action="store_true")
parser.add_argument("-error", required=False, default=False, help="Display ERROR records", action="store_true")
parser.add_argument("-warning", required=False, default=False, help="Display WARNING records", action="store_true")

args = parser.parse_args()

# default_path = "hw5_3\\logfile.log"

def load_logs(file_path: str) -> list:

    def parse_log_line(line: str) -> dict:
        log_dict = {}
        line = line.split(" ", 3)
        struct = ("date", "time", "level", "description")
        return dict(zip(struct, line))
    
    list_logs = []   
    try:
        with open(file_path, "r") as file:
            while True:
                line = file.readline()
                if not line:
                    return list_logs
                list_logs.append(parse_log_line(line))
    except FileNotFoundError:
        print('File not found')
        exit()


def filter_logs_by_level(logs: list, level: str) -> list:
    level_list = []
    for item in logs:
        if item["level"].lower() == level:
            level_list.append(item)
    return level_list

def count_logs_by_level(logs: list) -> dict:
    level_dict = defaultdict(int)
    for item in logs:
        level_dict[item["level"]] +=1 
    return dict(level_dict)

def display_log_counts(counts: dict):
    column1 = "Рівень логування "
    column2 = "| Кількість"
    width_col1 = len(column1)
    width_col2 = len(column2)
    print("\n" + column1 + column2)
    print("-" * width_col1 + "|" + "-" * width_col2)
    for key, value in counts.items():
        print(f"{key:<{width_col1}}| {value:<{width_col2}}")
    print()
    
def main():
    def print_debug(list_logs):
        for rec in list_logs:
            print(rec["date"], end = " ")
            print(rec["time"], end = " - ")
            print(rec["description"], end = "")

    logs = load_logs(args.filename)
    print(logs)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)
    if args.info:
        print(f"Деталі логів для рівня INFO:")
        print_debug(filter_logs_by_level(logs, "info"))
    if args.debug:
        print(f"Деталі логів для рівня DEBUG:")
        print_debug(filter_logs_by_level(logs, "debug"))
    if args.error:
        print(f"Деталі логів для рівня ERROR:")
        print_debug(filter_logs_by_level(logs, "error"))
    if args.warning:
        print(f"Деталі логів для рівня WARNING:")
        print_debug(filter_logs_by_level(logs, "warning"))
    
    
if __name__ == "__main__":
    main()