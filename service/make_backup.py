from .format import format
import os
from utils.constants import *
import tarfile
import string


def make_backup(path: str, backup_name: str):
    try:
        if not backup_name.endswith(".tar"):
            backup_name = f"{backup_name}.tar"
            
        # destination = os.path.join(BACKUPS_DIR, full_filename)
        destination = BACKUPS_DIR + "/" + backup_name
        
        
        with tarfile.open(destination, "w") as tar:
            tar.add(path)  #  arcname=os.path.basename(path)
        

        print(format(f"Backup done for {path} in backups/{backup_name}"))
            
    except Exception as e:
        print(format(f"Error: Failed to create backup for {path}: {e}"))
