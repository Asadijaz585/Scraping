from pip import main
import requests, time, csv
from lxml import html
PROXY = {
'http': 'http://youparcel:Proxy2022!@de.proxymesh.com:31280',
'https': 'http://youparcel:Proxy2022!@de.proxymesh.com:31280',
}

def first_20_computers_printers():
    base_url = requests.get("https://www.snapdeal.com/products/computers-printers-scanners?sort=plrty", proxies=PROXY)
    home = html.fromstring(html=base_url.content)
    for url_product in home.xpath("//div[@class='product-desc-rating ']/a/@href"):
        product_page = requests.get(url_product, proxies=PROXY)
        product_home = html.fromstring(html=product_page.content)
        product_urls = dict({
            "title": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
            "price": product_home.xpath("//span[@class='payBlkBig']/text()")[0].strip(),
            "image": product_home.xpath("//img[@class='cloudzoom']/@src")[0].strip(),
            "Left-Images": product_home.xpath("//div[@id='bx-pager-left-image-panel']/a/img/@src"),
            "description": product_home.xpath("//div[@itemprop='description']/text()"),
            "model": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
        }) 
        with open('computers&printers.csv', 'a', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([product_urls['title'], product_urls['price'], product_urls['image'], product_urls['Left-Images'], product_urls['description'], product_urls['model']])

def all_computers_printers():
    start_page = 20

    url = "https://www.snapdeal.com/acors/json/product/get/search/58/{}/20?q=&brandPageUrl=&keyword=&searchState=k3=true|k5=0|k6=0|k7=FwAwAAAQGAAAEsARkegAshwCAAAAAAAAAAAAAAAAAAAAAAACAAAACIAAAAAAACAAABAAAAAAAAAAIIAAAAAgAAAAQAI=|k8=0&pincode=&vc=&webpageName=categoryPage&campaignId=&brandName=&isMC=false&clickSrc=&showAds=true&cartId=&page=cp"

    payload={}
    headers = {
    'Cookie': 'SCOUTER=z6j084hegm0kjf; SCOUTER=x2iedd2e47apt8; alps=akm; sd.zone=NO_ZONE; u=164871552119873032; versn=v1; xc=eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImNiIjoiQiIsInVybCI6IloxIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn19; xg=eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImNiIjoiQiIsInVybCI6IloxIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn0sInVpZCI6eyJndWlkIjoiMGU2OTYxZjYtNjNjNy00ZjUxLWIzZTMtMzU2YTQwODI4OTIxIn19fHwxNjQ5MjQxNjgxODg5; JSESSIONID=17AE36468089E9395C1E43CBA8A31F2D; Megatron=!b3zmxFrbzL81u5/+ZidaGBcQKxXOrLaSvQE/JAcW9a3UMLZKWGYuvyjPmG69TBeVqEibis6gscdHwA=='
    }


    while True:
        response = requests.request("GET", url.format(start_page), headers=headers, data=payload, proxies=PROXY)
        home = html.fromstring(html=response.content)
        print("{} -- {}".format(home.xpath("//span[@id='pagination-lower-count']/text()")[0], home.xpath("//span[@id='pagination-upper-count']/text()")[0]))
        start_page += 20
        time.sleep(2)
        for url_product in home.xpath("//div[@class='product-desc-rating ']/a/@href"):                
            product_page = requests.get(url_product, proxies=PROXY)
            product_home = html.fromstring(html=product_page.content)
            product_urls = dict({
                "title": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
                "price": product_home.xpath("//span[@class='payBlkBig']/text()")[0].strip(),
                "image": product_home.xpath("//img[@class='cloudzoom']/@src")[0].strip(),
                "Left-Images": product_home.xpath("//div[@id='bx-pager-left-image-panel']/a/img/@src"),
                "description": product_home.xpath("//div[@itemprop='description']/text()"),
                "model": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
            }) 
            with open('computers&printers.csv', 'a', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([product_urls['title'], product_urls['price'], product_urls['image'], product_urls['Left-Images'], product_urls['description'], product_urls['model']])

def first_20_storage_devices():
    storage_devices_url = requests.get("https://www.snapdeal.com/products/storage-devices?sort=plrty", proxies=PROXY)
    home = html.fromstring(html=storage_devices_url.content)
    for url_product in home.xpath("//div[@class='product-desc-rating ']/a/@href"):
        product_page = requests.get(url_product, proxies=PROXY)
        product_home = html.fromstring(html=product_page.content)
        try:
            product_urls = dict({
                "title": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
                "price": product_home.xpath("//span[@class='payBlkBig']/text()")[0].strip(),
                "image": product_home.xpath("//img[@class='cloudzoom']/@src")[0].strip(),
                "Left-Images": product_home.xpath("//div[@id='bx-pager-left-image-panel']/a/img/@src"),
                "description": product_home.xpath("//div[@itemprop='description']/text()"),
                "model": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
            })
        except:
            pass 
        with open('storage_devices.csv', 'a', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([product_urls['title'], product_urls['price'], product_urls['image'], product_urls['Left-Images'], product_urls['description'], product_urls['model']])




def all_storage_devices():
    start_page = 20

    url = "https://www.snapdeal.com/acors/json/product/get/search/3032/{}/20?q=&sort=plrty&brandPageUrl=&keyword=&searchState=k3=true|k5=0|k6=0|k7=+kICyQ2ASycAAAAACAAAAAAACAAAARATIAAAAEAAEAAAgAAACAABAAAAAAAAABAE|k8=0&pincode=&vc=&webpageName=categoryPage&campaignId=&brandName=&isMC=false&clickSrc=&showAds=true&cartId=&page=cp"

    payload={}
    headers = {
    'Cookie': 'SCOUTER=x6j8r9ilpr0l6q; alps=akm; sd.zone=NO_ZONE; u=164871552119873032; versn=v1; xc=eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImNiIjoiQiIsInVybCI6IloxIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn19; xg=eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImNiIjoiQiIsInVybCI6IloxIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn0sInVpZCI6eyJndWlkIjoiMGU2OTYxZjYtNjNjNy00ZjUxLWIzZTMtMzU2YTQwODI4OTIxIn19fHwxNjQ5MjM0MDc4NDIw; JSESSIONID=4642140858E096C488D1200B540E20BD; Megatron=!Q/BjLNdJQlSss5j+ZidaGBcQKxXOrH5qwbGZsU8m3/Bez02RhDKpH2T6PdU1hoqKEgoA9NKQ95iEpN0='
    }
    while True:
        response = requests.request("GET", url.format(start_page), headers=headers, data=payload, proxies=PROXY)
        home = html.fromstring(html=response.content)
        print("{} -- {}".format(home.xpath("//span[@id='pagination-lower-count']/text()")[0], home.xpath("//span[@id='pagination-upper-count']/text()")[0]))
        start_page += 20
        time.sleep(2)
        for url_product in home.xpath("//div[@class='product-desc-rating ']/a/@href"):
            product_page = requests.get(url_product, proxies=PROXY)
            product_home = html.fromstring(html=product_page.content)
            try:
                product_urls = dict({
                    "title": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
                    "price": product_home.xpath("//span[@class='payBlkBig']/text()")[0].strip(),
                    "image": product_home.xpath("//img[@class='cloudzoom']/@src")[0].strip(),
                    "Left-Images": product_home.xpath("//div[@id='bx-pager-left-image-panel']/a/img/@src"),
                    "description": product_home.xpath("//div[@itemprop='description']/text()"),
                    "model": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
                })
            except:
                pass
            with open('storage_devices.csv', 'a', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([product_urls['title'], product_urls['price'], product_urls['image'], product_urls['Left-Images'], product_urls['description'], product_urls['model']])

def first_20_computer_accessories():
    storage_devices_url = requests.get("https://www.snapdeal.com/products/computers-computer-accessories?sort=plrty", proxies=PROXY)
    home = html.fromstring(html=storage_devices_url.content)
    for url_product in home.xpath("//div[@class='product-desc-rating ']/a/@href"):
        product_page = requests.get(url_product, proxies=PROXY)
        product_home = html.fromstring(html=product_page.content)
        try:
            product_urls = dict({
                "title": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
                "price": product_home.xpath("//span[@class='payBlkBig']/text()")[0].strip(),
                "image": product_home.xpath("//img[@class='cloudzoom']/@src")[0].strip(),
                "Left-Images": product_home.xpath("//div[@id='bx-pager-left-image-panel']/a/img/@src"),
                "description": product_home.xpath("//div[@itemprop='description']/text()"),
                "model": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
            })
        except:
            pass 
        with open('computer_accessories.csv', 'a', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([product_urls['title'], product_urls['price'], product_urls['image'], product_urls['Left-Images'], product_urls['description'], product_urls['model']])

def all_computer_accessories():
    start_page = 20

    url = "https://www.snapdeal.com/acors/json/product/get/search/150/{}/20?q=&sort=plrty&brandPageUrl=&keyword=&searchState=k3=true|k5=0|k6=0|k7=AYBAAEEQjTECEAAIAIABEGGJhAAAAAABAAAkAAFAAAAAAAAAAAAAAAAQAABAAAAAAAAAAAAQAIAAIAQQAEA=|k8=0&pincode=&vc=&webpageName=categoryPage&campaignId=&brandName=&isMC=false&clickSrc=unknown&showAds=true&cartId=&page=cp"

    payload={}
    headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'Accept': 'text/html, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.snapdeal.com/products/computers?sort=plrty',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'SCOUTER=x3eags2601lq53; versn=v1; u=164870822175895719; sd.zone=NO_ZONE; alps=akm; _gcl_au=1.1.1072627701.1648708226; isWebP=true; st=utm_source%3DDIRECT%7Cutm_content%3Dnull%7Cutm_medium%3Dnull%7Cutm_campaign%3Dnull%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C; lt=utm_source%3DDIRECT%7Cutm_content%3Dnull%7Cutm_medium%3Dnull%7Cutm_campaign%3Dnull%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C; hpcl=21; _fbp=fb.1.1648708228546.548567908; __gads=ID=b0d68e116620f978:T=1648708230:S=ALNI_MYz6W164tiBBHsvG-8SbLZmMhU02w; _clck=tom5y7|1|f08|0; SCOUTER=x4qa37ekk7g6ki; f5_cspm=1234; JSESSIONID=F00998DEA3A3051164142B7892AB7984; xg=eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImNiIjoiQiIsInVybCI6IloxIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn0sInVpZCI6eyJndWlkIjoiMGQzODRlY2EtNGFjZS00Y2M5LThmY2MtZmMxNzA1ZjI0MjU3In19fHwxNjQ4NzIyODEyMTI0; xc=eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImNiIjoiQiIsInVybCI6IloxIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn19; _sdDPPageId=1648721015431_6026_164870822175895719; vt=utm_source%3DDIRECT%7Cutm_content%3Dnull%7Cutm_medium%3Dnull%7Cutm_campaign%3Dnull%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C; _uetsid=131f1ac0b0bc11ecbd52d73b5ad3c2b2; _uetvid=131f68d0b0bc11ec880e57704750516a; _clsk=1ff3i8u|1648721020849|1|1|l.clarity.ms/collect; s_pers=%20s_vnum%3D1651300227499%2526vn%253D2%7C1651300227499%3B%20gpv_pn%3DallProducts%253Ahttps%253A%252F%252Fwww.snapdeal.com%252Fproduct%252Fosel-silver-karizma-metallic-16gb%252F678648619511%7C1648722824742%3B%20s_invisit%3Dtrue%7C1648722824744%3B; Megatron=!1gaHkTpIYBb+wyL+ZidaGBcQKxXOrDGsp1RIPOJAouecIOyYvxzBDkzy5Pl9+zKF1d1kX15SixrQoJo=; cto_bundle=jKYvlV9QbGtrYlhCanFqSkQxVzJQbzdIS1ZOZ0dxa2pjUThDVU9EaTFOMGJaYjlQRWhadFR5c3A1N1h2M2d0Y045UXM4SjZRVTJSVW5wNE9GaW00QXg4UnpqeDNjNUZJMmtncDYlMkJSS3JHZHA5WVpMQnc3OHpvQUFMTWhqOElwbUolMkJYQXY2N2pIR2NSYTd6TXNXUG5paUdpSlB3JTNEJTNE; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3D%3B%20s_ppv%3D61%3B; alps=akm; sd.zone=NO_ZONE; u=164871552119873032; versn=v1; xc=eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImNiIjoiQiIsInVybCI6IloxIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn19; xg=eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImNiIjoiQiIsInVybCI6IloxIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn0sInVpZCI6eyJndWlkIjoiN2RjMmVmY2ItNzdlNS00ZmIwLWExYTMtMzBmODA3MGJmYzc5In19fHwxNjQ5MTM0Mjc4MTIx; JSESSIONID=7937BC92B7F6611AD2C982347094CCA8; Megatron=!vXoIu9f50xW6idH+ZidaGBcQKxXOrCApEunSyqEXwP99f9DktQ6dwXe2Wvbc1kDUlDeh6bVmsjZd0ds='
    }
    while True:
        response = requests.request("GET", url.format(start_page), headers=headers, data=payload, proxies=PROXY)
        home = html.fromstring(html=response.content)
        print("{} -- {}".format(home.xpath("//span[@id='pagination-lower-count']/text()")[0], home.xpath("//span[@id='pagination-upper-count']/text()")[0]))
        start_page += 20
        time.sleep(2)
        for url_product in home.xpath("//div[@class='product-desc-rating ']/a/@href"):
            product_page = requests.get(url_product, proxies=PROXY)
            product_home = html.fromstring(html=product_page.content)
            try:
                product_urls = dict({
                    "title": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
                    "price": product_home.xpath("//span[@class='payBlkBig']/text()")[0].strip(),
                    "image": product_home.xpath("//img[@class='cloudzoom']/@src")[0].strip(),
                    "Left-Images": product_home.xpath("//div[@id='bx-pager-left-image-panel']/a/img/@src"),
                    "description": product_home.xpath("//div[@itemprop='description']/text()"),
                    "model": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
                })
            except:
                pass
            with open('computer_accessories.csv', 'a', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([product_urls['title'], product_urls['price'], product_urls['image'], product_urls['Left-Images'], product_urls['description'], product_urls['model']])

def first_20_software():
    storage_devices_url = requests.get("https://www.snapdeal.com/products/computers-software-cd-roms?sort=plrty", proxies=PROXY)
    home = html.fromstring(html=storage_devices_url.content)
    for url_product in home.xpath("//div[@class='product-desc-rating ']/a/@href"):
        product_page = requests.get(url_product, proxies=PROXY)
        product_home = html.fromstring(html=product_page.content)
        try:
            product_urls = dict({
                "title": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
                "price": product_home.xpath("//span[@class='payBlkBig']/text()")[0].strip(),
                "image": product_home.xpath("//img[@class='cloudzoom']/@src")[0].strip(),
                "Left-Images": product_home.xpath("//div[@id='bx-pager-left-image-panel']/a/img/@src"),
                "description": product_home.xpath("//div[@itemprop='description']/text()"),
                "model": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
            })
        except:
            pass 
        with open('software.csv', 'a', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([product_urls['title'], product_urls['price'], product_urls['image'], product_urls['Left-Images'], product_urls['description'], product_urls['model']])

def all_software():
    start_page = 20

    url = "https://www.snapdeal.com/acors/json/product/get/search/59/{}/20?q=&sort=plrty&brandPageUrl=&keyword=&searchState=k3=true|k5=0|k6=0|k7=RgOAAAACABEAIAQFAEAAAAAAQAAAAAwAAAAGBAAAABINAACACAiAAAAsAAAoAhABBMA=|k8=0&pincode=&vc=&webpageName=categoryPage&campaignId=&brandName=&isMC=false&clickSrc=unknown&showAds=true&cartId=&page=cp"

    payload={}
    headers = {
    'Cookie': 'SCOUTER=z3a2j7e16vl5bk; alps=akm; sd.zone=NO_ZONE; u=164871552119873032; versn=v1; xc=eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImNiIjoiQiIsInVybCI6IloxIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn19; xg=eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImNiIjoiQiIsInVybCI6IloxIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn0sInVpZCI6eyJndWlkIjoiMGU2OTYxZjYtNjNjNy00ZjUxLWIzZTMtMzU2YTQwODI4OTIxIn19fHwxNjQ5MjM3NTEwOTUz; JSESSIONID=4642140858E096C488D1200B540E20BD; Megatron=!JsXzkqa1uE+Qt8j+ZidaGBcQKxXOrFVr9X89rknpOv/psLUKQaA1zKIaaTzvHkbKA/JD5wi6CIRohJI='
    }

    while True:
        response = requests.request("GET", url.format(start_page), headers=headers, data=payload, proxies=PROXY)
        home = html.fromstring(html=response.content)
        print("{} -- {}".format(home.xpath("//span[@id='pagination-lower-count']/text()")[0], home.xpath("//span[@id='pagination-upper-count']/text()")[0]))
        start_page += 20
        time.sleep(2)
        for url_product in home.xpath("//div[@class='product-desc-rating ']/a/@href"):
            product_page = requests.get(url_product, proxies=PROXY)
            product_home = html.fromstring(html=product_page.content)
            try:
                product_urls = dict({
                    "title": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
                    "price": product_home.xpath("//span[@class='payBlkBig']/text()")[0].strip(),
                    "image": product_home.xpath("//img[@class='cloudzoom']/@src")[0].strip(),
                    "Left-Images": product_home.xpath("//div[@id='bx-pager-left-image-panel']/a/img/@src"),
                    "description": product_home.xpath("//div[@itemprop='description']/text()"),
                    "model": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
                })
            except:
                pass
            with open('software.csv', 'a', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([product_urls['title'], product_urls['price'], product_urls['image'], product_urls['Left-Images'], product_urls['description'], product_urls['model']])

def first_20_computers_components():
    storage_devices_url = requests.get("https://www.snapdeal.com/products/computers-components?sort=plrty", proxies=PROXY)
    home = html.fromstring(html=storage_devices_url.content)
    for url_product in home.xpath("//div[@class='product-desc-rating ']/a/@href"):
        product_page = requests.get(url_product, proxies=PROXY)
        product_home = html.fromstring(html=product_page.content)
        try:
            product_urls = dict({
                "title": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
                "price": product_home.xpath("//span[@class='payBlkBig']/text()")[0].strip(),
                "image": product_home.xpath("//img[@class='cloudzoom']/@src")[0].strip(),
                "Left-Images": product_home.xpath("//div[@id='bx-pager-left-image-panel']/a/img/@src"),
                "description": product_home.xpath("//div[@itemprop='description']/text()"),
                "model": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
            })
        except:
            pass 
        with open('computers_components.csv', 'a', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([product_urls['title'], product_urls['price'], product_urls['image'], product_urls['Left-Images'], product_urls['description'], product_urls['model']])

def all_computers_components():
    start_page = 20

    url = "https://www.snapdeal.com/acors/json/product/get/search/56/{}/20?q=&sort=plrty&brandPageUrl=&keyword=&searchState=k3=true|k5=0|k6=0|k7=/WbvAw==|k8=0&pincode=&vc=&webpageName=categoryPage&campaignId=&brandName=&isMC=false&clickSrc=unknown&showAds=true&cartId=&page=cp"

    payload={}
    headers = {
    'Cookie': 'SCOUTER=x53mrv7711d66l; alps=akm; sd.zone=NO_ZONE; u=164871552119873032; versn=v1; xc=eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImNiIjoiQiIsInVybCI6IloxIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn19; xg=eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImNiIjoiQiIsInVybCI6IloxIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn0sInVpZCI6eyJndWlkIjoiN2RjMmVmY2ItNzdlNS00ZmIwLWExYTMtMzBmODA3MGJmYzc5In19fHwxNjQ5MTM0Mjc4MTIx; JSESSIONID=7937BC92B7F6611AD2C982347094CCA8; Megatron=!d/cpZ3YQX1067/L+ZidaGBcQKxXOrIj4npWjdl03cgjCLajPHEwiAhtzkxR+rGEDclA6TItsM/cteH8='
    }

    while True:
        response = requests.request("GET", url.format(start_page), headers=headers, data=payload, proxies=PROXY)
        home = html.fromstring(html=response.content)
        print("{} -- {}".format(home.xpath("//span[@id='pagination-lower-count']/text()")[0], home.xpath("//span[@id='pagination-upper-count']/text()")[0]))
        start_page += 20
        time.sleep(2)
        for url_product in home.xpath("//div[@class='product-desc-rating ']/a/@href"):
            product_page = requests.get(url_product, proxies=PROXY)
            product_home = html.fromstring(html=product_page.content)
            try:
                product_urls = dict({
                    "title": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
                    "price": product_home.xpath("//span[@class='payBlkBig']/text()")[0].strip(),
                    "image": product_home.xpath("//img[@class='cloudzoom']/@src")[0].strip(),
                    "Left-Images": product_home.xpath("//div[@id='bx-pager-left-image-panel']/a/img/@src"),
                    "description": product_home.xpath("//div[@itemprop='description']/text()"),
                    "model": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
                })
            except:
                pass
            with open('computers_components.csv', 'a', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([product_urls['title'], product_urls['price'], product_urls['image'], product_urls['Left-Images'], product_urls['description'], product_urls['model']])

def first_20_networking_connected_devices():
    storage_devices_url = requests.get("https://www.snapdeal.com/products/networking-connected-devices?sort=plrty", proxies=PROXY)
    home = html.fromstring(html=storage_devices_url.content)
    for url_product in home.xpath("//div[@class='product-desc-rating ']/a/@href"):
        product_page = requests.get(url_product, proxies=PROXY)
        product_home = html.fromstring(html=product_page.content)
        try:
            product_urls = dict({
                "title": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
                "price": product_home.xpath("//span[@class='payBlkBig']/text()")[0].strip(),
                "image": product_home.xpath("//img[@class='cloudzoom']/@src")[0].strip(),
                "Left-Images": product_home.xpath("//div[@id='bx-pager-left-image-panel']/a/img/@src"),
                "description": product_home.xpath("//div[@itemprop='description']/text()"),
                "model": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
            })
        except:
            pass 
        with open('networking_connected_devices.csv', 'a', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([product_urls['title'], product_urls['price'], product_urls['image'], product_urls['Left-Images'], product_urls['description'], product_urls['model']])

def all_networking_connected_devices():
    start_page = 20

    url = "https://www.snapdeal.com/acors/json/product/get/search/46138967/{}/20?q=&sort=plrty&brandPageUrl=&keyword=&searchState=k3=true|k5=0|k6=0|k8=0&pincode=&vc=&webpageName=categoryPage&campaignId=&brandName=&isMC=false&clickSrc=unknown&showAds=true&cartId=&page=cp"

    payload={}
    headers = {
    'Cookie': 'SCOUTER=z39362davqu95e; alps=akm; sd.zone=NO_ZONE; u=164871552119873032; versn=v1; xc=eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImNiIjoiQiIsInVybCI6IloxIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn19; xg=eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImNiIjoiQiIsInVybCI6IloxIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn0sInVpZCI6eyJndWlkIjoiN2RjMmVmY2ItNzdlNS00ZmIwLWExYTMtMzBmODA3MGJmYzc5In19fHwxNjQ5MTM0Mjc4MTIx; JSESSIONID=7937BC92B7F6611AD2C982347094CCA8; Megatron=!S+UzrlddDr+7FrL+ZidaGBcQKxXOrJM8HaPrEbFSMuIoH02Y1WTgZw9wFfU0tPrAWwexXiEYlJymwms='
    }

    while True:
        response = requests.request("GET", url.format(start_page), headers=headers, data=payload, proxies=PROXY)
        home = html.fromstring(html=response.content)
        print("{} -- {}".format(home.xpath("//span[@id='pagination-lower-count']/text()")[0], home.xpath("//span[@id='pagination-upper-count']/text()")[0]))
        start_page += 20
        time.sleep(2)
        for url_product in home.xpath("//div[@class='product-desc-rating ']/a/@href"):
            product_page = requests.get(url_product, proxies=PROXY)
            product_home = html.fromstring(html=product_page.content)
            try:
                product_urls = dict({
                    "title": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
                    "price": product_home.xpath("//span[@class='payBlkBig']/text()")[0].strip(),
                    "image": product_home.xpath("//img[@class='cloudzoom']/@src")[0].strip(),
                    "Left-Images": product_home.xpath("//div[@id='bx-pager-left-image-panel']/a/img/@src"),
                    "description": product_home.xpath("//div[@itemprop='description']/text()"),
                    "model": product_home.xpath("//h1[@class='pdp-e-i-head']/text()")[0].strip(),
                })
            except:
                pass
            with open('networking_connected_devices.csv', 'a', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([product_urls['title'], product_urls['price'], product_urls['image'], product_urls['Left-Images'], product_urls['description'], product_urls['model']])




if __name__ == "__main__":
    first_20_computers_printers()
    all_computers_printers()
    # first_20_storage_devices()
    # all_storage_devices()
    # first_20_computer_accessories()
    # all_computer_accessories()
    # first_20_software()
    # all_software()
    # first_20_computers_components()
    # all_computers_components()
    # first_20_networking_connected_devices()
    # all_networking_connected_devices()


