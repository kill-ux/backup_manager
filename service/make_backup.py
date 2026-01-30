from .format import format
import os
from utils.constants import *
import tarfile

def make_backup(path, backup_name):
    try:
        if not backup_name.endswith('.tar'):
            full_filename = f"{backup_name}.tar"
        else:
            full_filename = backup_name
        # destination = os.path.join(BACKUPS_DIR, full_filename)
        destination = BACKUPS_DIR + "/" + full_filename
        
        with tarfile.open(destination, "w") as tar:
            tar.add(path)  #  arcname=os.path.basename(path)
        

        print(format(f"Backup done for {path} in backups/{full_filename}"))
            
    except Exception as e:
        print(format(f"Error: Failed to create backup for {path}: {e}"))
