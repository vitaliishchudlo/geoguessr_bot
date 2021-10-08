import requests


def set_password(end_link):
    url = f'https://www.geoguessr.com/profile/set-password/{end_link}'


def send_confirmation_letter(email_address):
    url = 'https://www.geoguessr.com/api/v3/accounts/signup'
    data = {
        'email': email_address
    }
    request = requests.post(url=url, json=data)
    print('Confirmation email was sent', request.status_code)


def confirm_password(token, password):
    url = 'https://www.geoguessr.com/api/v3/profiles/setpassword'
    data = {
        'token': token,
        'password': password
    }
    response = requests.post(url=url, json=data)
    return response.text
