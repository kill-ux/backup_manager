from .create import create
from .logger import log_message

def run(args):
    match args:
        case ["start"]:
            print("Starting...")
        case ["stop"]:
            print("Stopping...")
        case ["create",schedule]:
            create(schedule)
        case _:
            log_message(f"Error: Invalid argments")