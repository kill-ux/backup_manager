from utils.constants import *

def get_schedules() -> list[str]:
    try:
        with open(SCHEDULES_FILE) as fd:
            return fd.readlines()
    except Exception as e:
        return []