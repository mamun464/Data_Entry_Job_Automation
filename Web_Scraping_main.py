from pprint import pprint
from time import sleep

from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

form_link="https://forms.gle/z8Upjnbf48mkrHKr7"

Zillow_link="https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.85381150365383%2C%22east%22%3A-122.29840365771484%2C%22south%22%3A37.69668892292081%2C%22west%22%3A-122.56825534228516%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"

headers = { 'Accept-Language' : 'en-US',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }
response=requests.get(url=Zillow_link,headers=headers)
pprint(response)
soup=BeautifulSoup(response.text,"html.parser")
all_data=soup.select(".property-card-data")
print((all_data[0]))

link = all_data[0].find('a', {'class': 'property-card-link'}).get('href')
addrs = (all_data[0].find('address', {'data-test': 'property-card-addr'})).text.strip()

price = all_data[0].find('span', {'data-test': 'property-card-price'}).text.split()[0]

pprint((link))
pprint((addrs))
pprint((price))

Chrome_Dev_path = "E:\Python Udemy\Day 48\Chrome Dev Tools\chromedriver.exe"
driver = Service(Chrome_Dev_path)
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=driver, options=option)
for item in all_data:
    #print("start Instut")
    browser.get(form_link)
    #print("browser open")
    link = item.find('a', {'class': 'property-card-link'}).get('href')
    if "http" not in link:
        link="https://www.zillow.com"+link
    addrs = (item.find('address', {'data-test': 'property-card-addr'})).text.strip()
    price = item.find('span', {'data-test': 'property-card-price'}).text.split()[0]

    sleep(1)
    address_set=browser.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_set.send_keys(addrs)
    sleep(1)
    price_set = browser.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_set.send_keys(price)
    sleep(1)

    link_set = browser.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_set.send_keys(link)

    sleep(1)
    submit = browser.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

    sleep(2)
    #browser.quit()
    #print("end Instut")
    sleep(1)