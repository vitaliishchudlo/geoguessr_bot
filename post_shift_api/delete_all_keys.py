import requests


def delete_all_active_emails_by_ip():
    request = requests.get('https://post-shift.ru/api.php?action=deleteall')
    print(f'Deleting keys: {request.text}')
