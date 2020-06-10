import requests
from bs4 import BeautifulSoup

URL = "https://play.google.com/store/search?q=%D1%81%D0%B1%D0%B5%D1%80%D0%B1%D0%B0%D0%BD%D0%BA&c=apps"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36', 'accept': '*/*'}
HOST = "https://play.google.com"
FILE = "apps.csv"
def get_html(url, params = None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='ImZGtf mpg5gc')
    apps = []
    for item in items:
        apps.append({
            'title': item.get_text(strip = True),
            'link': HOST + item.find('a', class_='JC71ub').get('href'),
            'Dev_link': HOST + item.find('a', class_='mnKHRc').get('href'),
            'Dev': HOST + item.find('div', class_='KoLSrc').get_text(strip = True),     
        })
    return apps         
def parse(): 
    html = get_html(URL)
    if html.status_code == 200:
        apps = []
        apps.extend(get_content(html.text))
        print(apps)
    else:
        print("Error!") 
parse()
