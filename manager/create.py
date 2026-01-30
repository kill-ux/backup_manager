import re


def create(schedule):
    pattern = r"^[^;]+;([01][0-9]|2[0-3]):[0-5][0-9];[^;]+$"
    if re.match(pattern, schedule):
        index = lines_line()
        with open("backup_schedules.txt", "a+") as fd:
            fd.write(f"{index}: {schedule}\n")


def lines_line():
    with open("backup_schedules.txt") as fd_r:
        return sum(1 for line in fd_r)
