from calendar import c
import requests
import json
from lxml import html
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.request import urlopen
from sqlalchemy import true



base_url = "https://www.zocdoc.com/"


proxies = {
   'http': 'http://uscurrency:Admin1234@us-dc.proxymesh.com:31280',
   'https': 'http://uscurrency:Admin1234@us-dc.proxymesh.com:31280',
}

payload={}
headers = {
  'authority': 'www.zocdoc.com',
  'cache-control': 'max-age=0',
  'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-fetch-site': 'none',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-user': '?1',
  'sec-fetch-dest': 'document',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'cookie': '_ga=GA1.2.1354560597.1644254293; _gcl_au=1.1.1731905607.1644254295; firstTimeVisitor=8eb45e3d-03ed-4a77-9268-04747bb881f1; ABG=704a49b2-5163-41c1-96e8-afa8021cd336; 1910D65B7BC74F23BC8FE7ACD9AEC709=set; abfp=1; originalReferrer=https://www.zocdoc.com/acupuncturists; ASP.NET_SessionId=4vms02tti130blocgwwbi5df; mostRecentReferrer=NONE; bsid=fd10cd84057d49ffa7af0910125482fb_2202161030; datadome=NSUEyvJm.X.4gPWgOf0u-WLBBypK4Jj~B1RS9U13XoMaooH1buogZ3nNKq6ykQVliLO~any4mhIunJN2ggU6w6j9ehZwuLbcD54.DtY6Uq4a~kq9BflaGtjRAZy5pmF; AWSALB=Pt51otdrr2a0xi9s67mpGVn8fL0d4x/nmzNstJe9fzCZ2zR1twtqlvfuCbwg7hAw6rubgjevS5JgXqsEmMahCavjZS3C/wHHEGP4zNb1LZBSXK86cEvtLmYUsUXK; AWSALBCORS=Pt51otdrr2a0xi9s67mpGVn8fL0d4x/nmzNstJe9fzCZ2zR1twtqlvfuCbwg7hAw6rubgjevS5JgXqsEmMahCavjZS3C/wHHEGP4zNb1LZBSXK86cEvtLmYUsUXK; bsid=a79bb59be3484cccba1c13f4028ed313_2202161843; datadome=.6a~o8z_g0I7hdsRqQyWXHXMVMC30VyCzKnQQ0XV78wsZBkKzqf13PGfH3nenzz~I4XnhW6G5C~JebU6hGwAyVTsC0~plRF~_cjwK~ngD-30swtjoUCOsp742vHLnATc; mostRecentReferrer=NONE'
}

response = requests.request("GET", base_url, headers=headers, data=payload, proxies=proxies)

home = html.fromstring(html=response.text)
physician_urls = home.xpath("//a[contains(@href,'/primary-care')]/@href")
dentist_urls = home.xpath("//a[contains(@href,'/dentists')]/@href")
obgyns_urls = home.xpath("//a[contains(@href,'/obgyns')]/@href")
psychologists_urls = home.xpath("//a[contains(@href,'/psychologists')]/@href")
psychiatrists_urls = home.xpath("//a[contains(@href,'/psychiatrists')]/@href")
therapist_urls =  home.xpath("//a[contains(@href,'/therapist')]/@href")
urgentcares_urls = home.xpath("//a[contains(@href,'/urgent')]/@href")

doc = []
for dentist in dentist_urls:
  url = "{}{}".format(base_url, dentist)
  response = requests.request("GET", url, headers=headers, data=payload, proxies=proxies)
  find_page = html.fromstring(html=response.text)
  
  doctors_page_url = "{}{}".format(base_url, find_page.xpath("//a[contains(@href, '/search?filters')]/@href")[0])

  doctors = "{}{}".format(base_url, find_page.xpath("//a[contains(@href, '/dentist/')]/@href"))
  doc.append(doctors)
  for d in doc:
    print(d)

  import pdb;pdb.set_trace()
  pass
# for obgyns in obgyns_urls:
#   url = "{}{}".format(base_url, obgyns)
#   response = requests.request("GET", url, headers=headers, data=payload, proxies=proxies)
#   find_page = html.fromstring(html=response.text)
  
#   doctors_page_url = "{}{}".format(base_url, find_page.xpath("//a[contains(@href, '/search?filters')]/@href")[0])
#   import pdb;pdb.set_trace()
#   pass
# for psychologists in psychologists_urls:
#   pass
# for psychiatrists in psychiatrists_urls:
#   pass
# for therapist in therapist_urls:
#   pass
# for urgentcares in urgentcares_urls:
#   pass
# for physician in physician_urls:
#   pass

  import pdb;pdb.set_trace()
  



# print(title.text)
  
