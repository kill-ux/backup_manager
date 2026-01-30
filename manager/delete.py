from .logger import log_message
import os
from utils.constants import *



def delete_schedule(index_str):

    try:
        index = int(index_str)
    except ValueError:
        log_message(f"Error: index '{index_str}' is not a valid number")
        return

    if not os.path.exists(SCHEDULES_FILE):
        log_message(f"Error: can't find backup_schedules.txt")
        return

    with open(SCHEDULES_FILE, "r") as fr:
        lines = fr.readlines()

    if index < 0 or index >= len(lines):
        log_message(f"Error: can't find schedule at index {index}")
        return

    lines.pop(index)

    with open(SCHEDULES_FILE, "w") as f:
        f.writelines(lines)

    log_message(f"Schedule at index {index} deleted")
