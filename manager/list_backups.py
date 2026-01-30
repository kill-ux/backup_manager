
from .logger import log_message
import os
from utils.constants import *

def list_backups():
    try:
        if not os.path.exists(BACKUPS_DIR):
            log_message("Error: can't find backups directory")
            return
        
        files = os.listdir(BACKUPS_DIR)
        
        for file in files:
            print(file)
            
        log_message("Trace: Show backups list")
        
    except Exception as e:
        log_message(f"Error: Unexpected error while listing backups: {e}")