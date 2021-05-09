import requests




def check_hash(hash):
    request = requests.get(f'https://post-shift.ru/api.php?action=balance&hash={hash}').json()

    if request.get('error') == None:
        if request.get('limit') == '100':
            return 6000
        else:
            return 6001
    else:
        return (f'Error: 6002 | {request.get("error")}')
