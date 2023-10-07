import requests
from bs4 import BeautifulSoup
url = "https://whatstat.ru/channel/UC2tsySbe9TNrI-xh2lximHA"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
def govno():
    weather_block = soup.find('table', class_="table")
    weather_info = weather_block.get_text().strip()
    pagodka =  'А4 это: ' + weather_info
    return pagodka