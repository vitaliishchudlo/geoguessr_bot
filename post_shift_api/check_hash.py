import requests


def check_hash_availability(hash):
    response = requests.get(f'https://post-shift.ru/api.php?action=balance&hash={hash}').json()
    result = response.get('limit')
    return result
