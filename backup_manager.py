import os
from datetime import datetime

def delete_line(line_num):
    log_message("deleting")
    with open("backup_schedules.txt", "r") as fr:
        lines = fr.readlines()
        
    lines.pop(line_num)
        
    with open("backup_schedules.txt", "w") as f:
            f.writelines(lines)
            
def log_message(message):
    timestamp = datetime.now().strftime("[%d/%m/%Y %H:%M]")
    formatted_message = f"{timestamp} {message}"
    
    
    try:
        os.makedirs(os.path.dirname("./logs/backup_manager.log"), exist_ok=True)
        with open("./logs/backup_manager.log", "a") as f:
            f.write(formatted_message + "\n")
    except Exception as e:
        print(f"Critical Error: Could not write to log file. {e}")


delete_line(2)  
