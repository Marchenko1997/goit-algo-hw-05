from typing import List, Dict
from collections import defaultdict

def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return list(filter(lambda log: log["level"] == level.upper(), logs))


def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return dict(counts)

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level in ["INFO", "DEBUG", "ERROR", "WARNING"]:
        print(f"{level:<17}| {counts.get(level, 0)}")
