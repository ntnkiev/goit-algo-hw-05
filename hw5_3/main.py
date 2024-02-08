
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
        for value in item.values():
            level_dict???
            
    return dict(level_dict)

def main():
    log = load_logs(default_path)
    # print(log)
    # log_level = filter_logs_by_level(log, "ERROR")
    # for item in log_level:
    print(count_logs_by_level(log))


if __name__ == "__main__":
    main()