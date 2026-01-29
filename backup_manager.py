import os, sys


def main():
    with open("./logs/backup_manager.log", "w") as fd:
        if len(sys.argv) < 2:
            fd.write("wrong argment")
            sys.exit(1)
        command = sys.argv[1].lower()
        match command:
            case "start":
                print("Service is starting...")

            case "stop":
                print("Service is stopping...")

            case "create":
                if len(sys.argv) != 3:
                    fd.write("wrong argument\n")
                    sys.exit(1)
                schedule = sys.argv[2].lower()
                print(f"Creating service with schedule: {schedule}")

            case _:  # This is the 'default' case (wildcard)
                fd.write(f"Unknown command: {command}\n")
                sys.exit(1)


if __name__ == "__main__":
    main()
