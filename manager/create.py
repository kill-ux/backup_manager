import re
from .logger import log_message


def create(schedule):
    pattern = r"^[^;]+;([01][0-9]|2[0-3]):[0-5][0-9];[^;]+$"
    if re.match(pattern, schedule):
        index = lines_line()
        with open("backup_schedules.txt", "a+") as fd:
            fd.write(f"{"\n" if index else ""}{index}: {schedule}")
            log_message(f"INFO: New schedule added => {schedule}")
    else:
        log_message(f"Error: malformed schedule: {schedule}")


def lines_line():
    try:
        with open("backup_schedules.txt") as fd_r:
            return sum(1 for line in fd_r)
    except:
        return 0