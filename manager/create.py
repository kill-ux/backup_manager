import re
from .logger import log_message
from utils.constants import *


def create(schedule):
    try:
        pattern = r"^[^;]+;([01][0-9]|2[0-3]):[0-5][0-9];[^;/]+$"
        if re.match(pattern, schedule):
            with open(SCHEDULES_FILE, "a+") as fd:
                fd.write(f"{schedule}\n")
                log_message(f"INFO: New schedule added => {schedule}")
        else:
            log_message(f"Error: malformed schedule: {schedule}")
    except Exception as e:
        log_message(f"Error: Unexpected error while adding a schedule: {e}")
