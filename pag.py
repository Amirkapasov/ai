import requests
from bs4 import BeautifulSoup
url = "https://tengrinews.kz/weather/semey/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
def last_news():
    weather_block = soup.find('div', class_="temp")
    weather_info = weather_block.get_text().strip()
    pagodka =  'Погода в Семее: ' + weather_info
    return pagodka