import requests


def check_hash_availability(hash):
    request = requests.get(f'https://post-shift.ru/api.php?action=balance&hash={hash}').json()
    result = request.get('limit')
    return result

