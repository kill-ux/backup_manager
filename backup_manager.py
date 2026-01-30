import os, sys, re
from manager.create import create
from utils.create_dir import create_dir



def main():
    create_dir("logs")

    with open("./logs/backup_manager.log", "w") as fd:
        match sys.argv[1:]:
            case ["start"]:
                print("Starting...")
            case ["stop"]:
                print("Stopping...")
            case ["create",schedule]:
                create(schedule)
            case _:
                print("Invalid arguments")
                fd.write(f"Unknown command: {sys.argv[1:]}\n")



if __name__ == "__main__":
    main()

