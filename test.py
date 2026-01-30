import time
from manager.logger import log_message


if __name__ == "__main__":
    while True:
        time.sleep(3)
        log_message("Hello python")
        
