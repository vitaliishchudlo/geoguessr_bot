import requests
from bs4 import BeautifulSoup


url = 'https://www.geoguessr.com/api/v3/accounts/signup'

headers = {
    'Host': 'www.geoguessr.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.geoguessr.com/signup',
    'Content-Type': 'application/json',
    'Origin': 'https://www.geoguessr.com',
    'Content-Length': '32',
    'Connection': 'keep-alive',
}


request = requests.post(url, headers=headers, json={'email':'prxocvqz40@post-shift.ru'})


print(request.status_code)
print(request.reason)
print(request.text)
