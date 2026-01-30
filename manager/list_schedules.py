from utils.constants import *
from .logger import log_message


def list_schedules():
    try:
        with open(SCHEDULES_FILE) as fd:
            for index, schedule in enumerate(fd):
                print(f"{index}: {schedule}", end="")
            log_message("TRACE: Show schedules list")
    except Exception as e:
        log_message(f"Error: Unexpected error while list a schedules: {e}")
