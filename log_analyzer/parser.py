from typing import List

def parse_log_line(line: str) -> dict:
    try:
        date, time, level, *message = line.strip().split()
        return {
            "date": date,
            "time": time,
            "level": level.upper(),
            "message": " ".join(message)
        }
    except ValueError:
        return {}

def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            logs = [parsed for line in file if (parsed := parse_log_line(line))]
    except FileNotFoundError:
        print(f"[Error] file {file_path} not found")
        import sys
        sys.exit(1)
    return logs
