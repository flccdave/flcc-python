import requests
from bs4 import BeautifulSoup

geforce = requests.get('https://phishingdemo.org/python/scraping/4070ti.html', headers={"User-Agent": ""})
print(geforce) # 200 - OK

# print(geforce.text)
# print(geforce.content)

soup = BeautifulSoup(geforce.content, 'html.parser')
# print(soup)

quantity = soup.find(id="remaining").string
price = soup.find(id="price").string

print(f'There are {quantity} GeForce 4070ti cards left at {price}')
