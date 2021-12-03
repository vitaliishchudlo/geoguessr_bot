import random
import string


def generate_password():
    # get random password pf length 8 with letters&digits
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(12))
    return password
