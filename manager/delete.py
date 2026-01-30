import os
from logger import log_message
def delete_line(line_num):
    log_message("deleting")
    with open("backup_schedules.txt", "r") as fr:
        lines = fr.readlines()
        
    lines.pop(line_num)
        
    with open("backup_schedules.txt", "w") as f:
            f.writelines(lines)


delete_line(2)  