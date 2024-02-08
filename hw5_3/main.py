
from collections import defaultdict

default_path = "hw5_3\\logfile.log"

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
        if item["level"] == level:
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
    print(column1 + column2)
    print("-" * len(column1) + "|" + "-" * len(column2))
    for key, value in counts.items():
        print({key} " "*(len(column1)-len(key)) + "|" + "{value}")


    pass

def main():
    log = load_logs(default_path)
    # print(log)
    # log_level = filter_logs_by_level(log, "ERROR")
    print(count_logs_by_level(log))
    counts = count_logs_by_level(log)
    display_log_counts(counts)


if __name__ == "__main__":
    main()