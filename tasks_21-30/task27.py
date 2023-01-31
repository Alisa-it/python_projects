from bs4 import BeautifulSoup
import requests

url = "https://www.yesasia.ru/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
i = 0
for data in soup.findAll('a', rel="bookmark"):
    if data.text != '' and not '...' in data.text:
        i += 1
        print(f'{i}) {data.text}', data.get('href'))