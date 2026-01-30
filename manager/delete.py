from .logger import log_message


def delete_schedule(index_str):

    try:
        index = int(index_str)
    except ValueError:
        log_message(f"Error: index '{index_str}' is not a valid number")
        return

    # with open("backup_schedules.txt", "r") as fr:
    #     lines = fr.readlines()

    # lines.pop(index)

    # with open("backup_schedules.txt", "w") as f:
    #     f.writelines(lines)

    # log_message(f"Schedule at index {index} deleted")
