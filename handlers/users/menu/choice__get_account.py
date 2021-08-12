import time

from geoguessr_api import send_confirmation_email
from post_shift_api import check_hash_availability, register_email, delete_all_active_emails_by_ip, \
    get_confirmation_email
from utils.db_api import get_hash, set_hash_status_deactive


def register_new_account():
    # 1. Get hash from DB, if false > say user
    hash_from_database = get_hash()  # hash from db --> 2868985227b081ea418f29533e3eaafa
    if not hash_from_database:
        return False, 'No available hash for registering account in database.\nPlease, connect with admin - ' \
                      '@vitalii_shchudlo'
    # 2. Check hash for available requests >= 2-3, if false - set unactive in DB table, status 1
    info_calls = check_hash_availability(hash_from_database)
    if not info_calls or int(info_calls) <= 3:
        # Set unactive status in DB for this hash
        set_hash_status_deactive(hash_from_database)
        # Call function register_new_account again
        register_new_account()

    # 3. Register email
    email_data = register_email(hash_from_database)
    email_address = email_data.get('email')
    email_key = email_data.get('key')
    print('\n\n')
    print(email_data)
    print('\n\n')

    # 4. 1\2 First step of registration geoguessr account. Send post.
    send_confirmation_email(email_address)

    # 5. Get a link from a letter that came in an email.

    email_text = get_confirmation_email(hash_from_database, email_key)
    print(email_text)
    time.sleep(5)
    email_text = get_confirmation_email(hash_from_database, email_key)
    print(email_text)

    # 6.  2\2 First step of registration geoguessr account. Confirmation. Setting password

    # 7. Saving all data. Setting all statuses. Deleting active emails. Returning info for user.

    delete_all_active_emails_by_ip()
    return 'login', 'password'

    # account_data = register_new_account()
    # if not account_data[0]:
    #     await message.answer(f'[Error]: {account_data[1]}')
    # else:
    #     await message.answer(f'Account data: {account_data[0], account_data[1]}')
