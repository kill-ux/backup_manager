from datetime import datetime
import os
def log_message(message):
    timestamp = datetime.now().strftime("[%d/%m/%Y %H:%M]")
    formatted_message = f"{timestamp} {message}"
    
    
    try:
        with open("./logs/backup_manager.log", "a") as f:
            f.write(formatted_message + "\n")
    except Exception as e:
        print(f"Critical Error: Could not write to log file. {e}")