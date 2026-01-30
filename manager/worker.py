import subprocess
from signal import SIGTERM
from utils.constants import *
from manager.logger import log_message
import os

def start():
    try:
        is_running = subprocess.run(["pgrep", "-f", TARGET_SCRIPT], capture_output=True)
        if is_running.stdout:
            log_message("WARN: Backup is already running. Skipping..")
            return

        fd = open(SERVICE_LOG, "a")
        ps = subprocess.Popen(
            ["python3","-u", TARGET_SCRIPT], stdout=fd, stderr=fd, start_new_session=True
        )
        fd.close()
        log_message(f"TRACE: backup_service started at PID => {ps.pid}")
        return ps.pid
    except Exception as e:
        log_message(f"Error: Unexpected error while startin a backup manager: {e}")


def stop():
    try:
        result = subprocess.run(
            ["pgrep", "-f", TARGET_SCRIPT], capture_output=True, text=True
        )

        if not result.stdout:
            log_message("WARN: Stop requested but service was not running.")
            return

        pids = result.stdout.split()
        for pid_str in pids:
            pid = int(pid_str)
            os.kill(pid, SIGTERM)
            log_message(f"TRACE: backup_service (PID {pid}) stopped")

    except Exception as e:
        log_message(f"Error: Unexpected error while stopping: {e}")
