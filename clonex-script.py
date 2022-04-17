from cgitb import text
import json
from re import U
import time
from turtle import home, pd
from unicodedata import name
from click import option
# from xxlimited import Xxo
from sqlalchemy import true, types, create_engine
from  sqlalchemy.orm import scoped_session ,sessionmaker
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
# from mysql.connector import MySQLConnection
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chrome_path = 'chromedriver'

options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
# options.add_argument('--disable-gpu')
# options.add_argument('--headless')
# options.headless = True
chrome_driver_path = "chromedriver"

#  A system that checks the user-agent of the browser and they don't allow headless chrome
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(chrome_path, options=options)
engine = create_engine('mysql+pymysql://root@localhost/opensea_nfts')
db = scoped_session(sessionmaker(bind=engine))


nfts = [
    {
        "name": "Human",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=DNA&search[stringTraits][0][values][0]=Human&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "Robot",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=DNA&search[stringTraits][0][values][0]=Robot&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "Demon",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=DNA&search[stringTraits][0][values][0]=Demon&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "Angel",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=DNA&search[stringTraits][0][values][0]=Angel&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "Reptile",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=DNA&search[stringTraits][0][values][0]=Reptile&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "Undead",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=DNA&search[stringTraits][0][values][0]=Undead&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "Murakami",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=DNA&search[stringTraits][0][values][0]=Murakami&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "Alien",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=DNA&search[stringTraits][0][values][0]=Alien&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "MK1",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=MK1&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "MK-BLCK",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=MK-BLCK&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "MK2",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=MK2&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "Stoned",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=STONED&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "GLD Stoned",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=GLD%20STONED&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "Divine",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=Divine&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "ICE",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=ICE&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "DRK",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=DRK&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "ORNG",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=ORNG&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "TTN",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=TTN&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "Artist Edn",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=ARTIST%20EDITION&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "Split",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=SPLIT&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "M1 Human",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=MURAKAMI%20DRIP&search[stringTraits][1][name]=DNA&search[stringTraits][1][values][0]=Human&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "M2 Robot",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=MURAKAMI%20DRIP&search[stringTraits][1][name]=DNA&search[stringTraits][1][values][0]=Robot&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "M3 Demon",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=MURAKAMI%20DRIP&search[stringTraits][1][name]=DNA&search[stringTraits][1][values][0]=Demon&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "M4 Angel",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=MURAKAMI%20DRIP&search[stringTraits][1][name]=DNA&search[stringTraits][1][values][0]=Angel&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "M5 Reptile",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=MURAKAMI%20DRIP&search[stringTraits][1][name]=DNA&search[stringTraits][1][values][0]=Reptile&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "M6 Undead",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=MURAKAMI%20DRIP&search[stringTraits][1][name]=DNA&search[stringTraits][1][values][0]=Undead&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "M7 Alien",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=MURAKAMI%20DRIP&search[stringTraits][1][name]=DNA&search[stringTraits][1][values][0]=Alien&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "MT1 DOB Hat",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Hair&search[stringTraits][0][values][0]=DOB%20Hat&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "MT2 Blu Octopus",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Hair&search[stringTraits][0][values][0]=BLU%20OCTOPUS&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "MT3 PNK Octopus",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Hair&search[stringTraits][0][values][0]=PNK%20OCTOPUS&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "MT4 WHT Octopus",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Hair&search[stringTraits][0][values][0]=WHT%20OCTOPUS&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "MT5 Flower Hat",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Hair&search[stringTraits][0][values][0]=Flower%20Hat&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "MT6 Tan Tan Bo",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Mouth&search[stringTraits][0][values][0]=Tan%20Tan%20Bo&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "MT7 Org. M78.8",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Mouth&search[stringTraits][0][values][0]=Organism%20M78.8&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "MT8 Psychic Lazer",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Mouth&search[stringTraits][0][values][0]=PSYCHIC%20LAZER&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "MT9 Splash",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Back&search[stringTraits][0][values][0]=SPLASH&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "MT10 GRN U Wingz",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Back&search[stringTraits][0][values][0]=GRN%20UNDRWRLD%20WINGZ&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "MT11 GRY U Wingz",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Back&search[stringTraits][0][values][0]=GRY%20UNDRWRLD%20WINGZ&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "MT12 PNK U Wingz",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Back&search[stringTraits][0][values][0]=PNK%20UNDRWRLD%20WINGZ&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "MT13 BLK U Wingz",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Back&search[stringTraits][0][values][0]=BLCK%20UNDRWRLD%20WINGZ&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "R1 Helmet",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Helmet&search[stringTraits][0][values][0]=CATSUNE&search[stringTraits][0][values][1]=ANON&search[stringTraits][0][values][2]=BLU%20SAMURAI&search[stringTraits][0][values][3]=GLD%20MECH&search[stringTraits][0][values][4]=GLD%20SAMURAI&search[stringTraits][0][values][5]=GLD%20SPRTN&search[stringTraits][0][values][6]=GRN%20DRGN&search[stringTraits][0]"
    },
    {
        "name": "R2 Demonz",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Back&search[stringTraits][0][values][0]=DEMONZ&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "R3 Snake",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Clothing&search[stringTraits][0][values][0]=Snake&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "R4 VVS Crystl",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Eye%20Color&search[stringTraits][0][values][0]=VVS%20CRYSTL&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "R5 Blu Lazer",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Eyewear&search[stringTraits][0][values][0]=BLU%20LAZER&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "R6 Chrome Pipe",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Mouth&search[stringTraits][0][values][0]=Chrome%20Pipe&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "R7 Knife",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Mouth&search[stringTraits][0][values][0]=Knife&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "R8 Tongue Out",
        "url": "https://opensea.io/collection/clonex?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Mouth&search[stringTraits][0][values][0]=Tongue%20Out&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "RFT1 Mint Vial",
        "url": "https://opensea.io/collection/clonex-mintvial?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW"
    },
    {
        "name": "RFT2 MNLTH",
        "url": "https://opensea.io/collection/rtfkt-mnlth?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW"
    }
]

price=[]
for nft in nfts:
    url = nft["url"]
    name1 = nft["name"]
    driver.get(url)
    time.sleep(3)
    price = driver.find_elements(By.XPATH,"//div[@class='Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX Price--amount']")[0].text
    time.sleep(2)
    sql = "INSERT INTO `nfts` (`url`,`name`,`price`) VALUES ('{}','{}','{}')".format(url, name1, price)
    db.execute(sql)
    db.commit()
    print("inserted")
    time.sleep(2)


