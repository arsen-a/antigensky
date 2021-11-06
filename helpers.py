import random, string

import os
from constants import REQUIRED_DIRS


def generate_protocol_number():
    return "".join(
        [random.choice(string.ascii_uppercase) for _ in range(3)]
        + [str(random.randint(0, 9)) for _ in range(4)]
    )


def init_dirs():
    for dir in REQUIRED_DIRS:
        if not os.path.isdir(dir):
            os.mkdir(dir)
