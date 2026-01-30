from .create import create
from .list_schedules import list_schedules
from .delete import delete_schedule
from .logger import log_message
from .list_backups import list_backups


def run(args):
    match args:
        case ["start"]:
            print("Starting...")
        case ["stop"]:
            print("Stopping...")
        case ["list"]:
            list_schedules()
        case ["create",schedule]:
            create(schedule)
        case ["delete",index]:
            delete_schedule(index)
        case ["backups"]:
            list_backups()
        case _:
            log_message(f"Error: Invalid argments")