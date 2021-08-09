import requests


def set_password(end_link):
    url = f'https://www.geoguessr.com/profile/set-password/{end_link}'



def send_confirmation_email(email_address):
    url = 'https://www.geoguessr.com/api/v3/accounts/signup'
    data = {'email': email_address}
    request = requests.post(url=url, json=data)
    print(request.status_code, request.reason)
    print(request.text)


def clear_slphesh():
    bad_link = 'https:\/\/www.geoguessr.com\/profile\/set-password\/FFR3k6M0Tsmnb9Js5sjJ9FgC8Ir1S0k5\\'
    new_link = bad_link.replace('\\', '')


