import time
from .get_schedules import get_schedules
from .extract_info import check_and_extract_info
from .make_backup import make_backup


def run():
    while True:
        for schedule in get_schedules():
            info = check_and_extract_info(schedule)
            if info is None:
                continue
            path, backup_name = info
            
            make_backup(path, backup_name)
            
            pass
        
        time.sleep(60)