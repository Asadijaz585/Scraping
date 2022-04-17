from pyparsing import alphanums, alphas8bit
import requests
from bs4 import BeautifulSoup
import pandas as pd 
from pandas import ExcelWriter
from lxml import html

def get_headers():
    headers = {
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://www.filmzitate.info/startseite/abc_filme.php',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': '__utma=6314149.1766555589.1645691351.1645691351.1645691351.1; __utmc=6314149; __utmz=6314149.1645691351.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gads=ID=84b56af7f3d2974c-22051acd3ad000dc:T=1645691357:RT=1645691357:S=ALNI_MYv4LH-BdE39cUYxInbVGVqZsyHcQ; __utmb=6314149.4.10.1645691351'
    }
    return headers

proxies = {
   'http': 'http://uscurrency:Admin1234@us-dc.proxymesh.com:31280',
   'https': 'http://uscurrency:Admin1234@us-dc.proxymesh.com:31280',
}
url = "http://www.filmzitate.info/suche/suche-abc.php?suche_anfang={}"

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

payload={}

all_data = []
for alphabet in alphabets:
    response = requests.request("GET", url.format(alphabet), headers=get_headers(), data=payload, proxies=proxies)
    home = html.fromstring(html=response.text)
    print("status code: {} -- url: {}".format(response.status_code, response.url))
    for film in home.xpath("//a[contains(@href, 'film-zitate.php?film_id')]/@href"):
        film_url = "http://www.filmzitate.info/suche/{}".format(film)
        film_resposne = requests.request("GET", film_url, data=payload, proxies=proxies)
        film_page = html.fromstring(html=film_resposne.text)
        film_name = film_page.xpath("/html/body/h1/text()")
        quotes = [item[1:-1] for item in film_page.xpath("/html/body/li/text()")]
        df = pd.DataFrame([film_name[0], quotes])
        df.to_csv('table.csv', encoding='utf-8', index=False)
        # import pdb;pdb.set_trace()
