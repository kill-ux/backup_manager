import subprocess
from utils.constants import *


def start():
    with open(MANAGERE_LOG, "a") as fd:
        subprocess.Popen(
            ["python3", "test.py"],
        )
        subprocess.run


def stop():
    pass
