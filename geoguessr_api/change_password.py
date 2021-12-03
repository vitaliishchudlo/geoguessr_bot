import requests
from requests import Session

def change_password_geoAPI(email, old_password, new_password):
    data_auth = {
        "email": email,
        "password": old_password
    }
    data_change_password = {
        "newPassword": new_password,
        "oldPassword": old_password
    }
    url_auth = 'https://www.geoguessr.com/api/v3/accounts/signin'
    url_cp = 'https://www.geoguessr.com/api/v3/profiles/'

    s = Session()
    res_auth = s.post(url_auth, json=data_auth)
    res_cp = s.put(url_cp, json=data_change_password)
    if res_cp.status_code != 200:
        return False
    return True
