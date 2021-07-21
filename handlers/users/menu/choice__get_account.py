from utils.db_api import menu_get_account, get_hash


def get_account():
    account_data = menu_get_account()
    return account_data


def register_new_account():
    # 1. Get hash from DB, if false > say user

    hash_from_db = get_new_hash()
    if hash_from_db:
        print('True', hash_from_db)
    else:
        return False, 'No available hashs in database'

    # 2. Check hash for available requests >= 2-3, if false - set unactive in DB table, status 1

    # 3. Create email address
    pass


def get_new_hash():
    hash = get_hash()
    if hash:
        return hash