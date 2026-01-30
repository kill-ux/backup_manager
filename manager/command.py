from manager.create import create

def run(args, fd):
    match args:
        case ["start"]:
            print("Starting...")
        case ["stop"]:
            print("Stopping...")
        case ["create",schedule]:
            create(schedule)
        case _:
            print("Invalid arguments")
            fd.write(f"Unknown command: {args}\n")