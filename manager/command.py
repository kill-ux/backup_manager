from .create import create
from .delete import delete_schedule
from .logger import log_message

def run(args):
    match args:
        case ["start"]:
            print("Starting...")
        case ["stop"]:
            print("Stopping...")
        case ["create",schedule]:
            create(schedule)
        case ["delete",index]:
            delete_schedule(index)
        case _:
            log_message(f"Invalid argments\n")