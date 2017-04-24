import requests
import urllib.request
from bs4 import BeautifulSoup

# url = "http://h1bdata.info/index.php?em=&job=software&city=san+jose&year=All+Years"
url = "http://h1bdata.info/index.php?em=&job=software&city=chico&year=All+Years"

companies = set()

r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content, "html.parser")

for tr in soup.find_all('tr'):
    tds = tr.find_all('td')
    for td in tds:
        if td not in companies:
            companies.add(tds[0])
print(companies)

file = open("companies.txt", "w")
for cp in companies:
    # print(cp)
    file.write(str(cp) + '\n')




