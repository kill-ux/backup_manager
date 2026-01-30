import time
from .get_schedules import get_schedules
from .extract_info import check_and_extract_info
from .make_backup import make_backup
from datetime import datetime



def run():
    last_processed_minute = ""
    while True:
        now = datetime.now()
        current_time_str = now.strftime("%H:%M")
        if current_time_str != last_processed_minute: 
            for schedule in get_schedules():
                info = check_and_extract_info(schedule)
                if info is None:
                    continue
                path, backup_name = info
                make_backup(path, backup_name)
        last_processed_minute = current_time_str
            
        
        time.sleep(45)