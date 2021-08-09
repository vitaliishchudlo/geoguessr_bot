import requests


# def check_hash_calls(hash):
#     request = requests.get(f'https://post-shift.ru/api.php?action=balance&hash={hash}')
#     print(f'requests in post shift apapi folder: {request} ||| {request.text}')


def register_email(hash):
    request = requests.get(f'https://post-shift.ru/api.php?action=new&hash={hash}').json()
    return request


def get_confirmation_email(hash, key, letter_id=1):
    request = requests.get(f'https://post-shift.ru/api.php?action=getmail&hash={hash}&key={key}&id={letter_id}')

