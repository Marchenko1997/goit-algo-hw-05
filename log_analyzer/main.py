import sys
from parser import load_logs
from utils import filter_logs_by_level, count_logs_by_level, display_log_counts

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_лог_файлу> [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        filtered = filter_logs_by_level(logs, level_filter)
        print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()
