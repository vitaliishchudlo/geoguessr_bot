import requests


def register_email(hash):
    response = requests.get(f'https://post-shift.ru/api.php?action=new&hash={hash}').json()
    return response


def get_confirmation_email(hash, key, letter_id=1):
    response = requests.get(f'https://post-shift.ru/api.php?action=getmail&hash={hash}&key={key}&id={letter_id}')
    return response.text
