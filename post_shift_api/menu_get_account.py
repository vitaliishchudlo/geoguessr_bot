import requests


def get_text_mail(date_mail, hash):
    url = 'https://post-shift.ru/api.php?action=getmail&hash=d6be5cce6245b61552cdc5201e0488b2&key=faf3f53538d0b5a52222ad7ef5040068&id=1'


def register_mail(hash):
    url = f'https://post-shift.ru/api.php?action=new&hash={hash}'
    request = requests.get(url=url)
    return request.json()


def check_remain_calls(hash):
    url = f'https://post-shift.ru/api.php?action=balance&hash={hash}'
    request = requests.get(url=url)
    try:
        num = int(request.json()['limit'])
        if num >= 2:
            print(f'Zaputiv zalushulosia - {num}')
            return True
        else:
            return False
    except Exception:
        return False
