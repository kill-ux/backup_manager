import re
from datetime import datetime
from utils.constants import *

def check_and_extract_info(schedule):
    m = re.match(SCHEDULES_PATTERN, schedule)
    if m is None:
        return None

    path,  time_string, _, backup_name = m.groups()
    backup_time = datetime.strptime(time_string, "%H:%M").strftime("%H:%M")
    current_time = datetime.now().strftime("%H:%M")
    
    if backup_time != current_time:
        return None
    
    return path, backup_name