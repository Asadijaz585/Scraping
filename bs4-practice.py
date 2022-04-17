from unittest import result
from aiohttp import request
import requests
import time
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefing-room/")
print(result.status_code)

time.sleep(2)
# print(result.headers)
src = result.content
# print(src)
soup = BeautifulSoup(src,'lxml')

urls = []
for h2_tag in soup.find_all('h2'):
    try:
        a_tag = h2_tag.find('a')
        urls.append(a_tag.attrs['href'])
    except:
        continue

print(urls)    

# for link in links:
#     if 'About' in links:
#         print(link)
#         print(link.attrs['href'])
import pdb;pdb.set_trace()