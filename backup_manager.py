import os, sys, re
from manager import create


def main():
    folder = "logs"
    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(os.path.join(folder, "backup_manager.log"), "w") as fd:
        if len(sys.argv) < 2:
            fd.write("wrong argment")
            sys.exit(1)

        command = sys.argv[1:]

        match command:
            case ["start"]:
                print("Starting...")
            case ["stop"]:
                print("Stopping...")
            case [
                "create",
                schedule,
            ]:  # Matches 'create' followed by exactly one argument
                print(f"Creating with {schedule}")
                create.create(schedule)
            case _:
                print("Invalid arguments")
                fd.write(f"Unknown command: {command}\n")


if __name__ == "__main__":
    main()
