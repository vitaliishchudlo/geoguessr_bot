import requests

def register_mail(hash):
    url = f'https://post-shift.ru/api.php?action=new&hash={hash}'
    request = requests.get(url=url)
    print(request.text)

def check_remain_calls(hash):
    url = f'https://post-shift.ru/api.php?action=balance&hash={hash}'
    request = requests.get(url=url)
    if int(request.json()['limit']) >= 2:
        return True
    else:
        return False
