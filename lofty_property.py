from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import  Options
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.lofty.ai/account/offerings')
time.sleep(3)
res = driver.page_source
soup = BeautifulSoup(res,'html.parser')
time.sleep(5)
username = driver.find_element_by_id("email")
password = driver.find_element_by_id("password")

username.send_keys("kylevinson@gmail.com")
password.send_keys("LoftProp123")

driver.find_element_by_xpath("/html/body/div[1]/form/section/div/div[1]/div/div[4]/button").click()
time.sleep(10)
driver.get('https://www.lofty.ai/account/offerings')
time.sleep(10)
res = driver.page_source
soup = BeautifulSoup(res,'html.parser')

driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/main/div/div/div/nav/div/button[2]").click()
time.sleep(10)
res = driver.page_source
soup = BeautifulSoup(res,'html.parser')

url_list = []
div = soup.find_all('div',{'class':'relative rounded-xl bg-gray-100 dark:bg-gray-900'})
for anchor_tag in div:
    a_tag = anchor_tag.find('a')
    url = "https://www.lofty.ai"+str(a_tag.get('href'))
    # print(url)
    url_list.append(url)
    # category_type_name_list.append(category_type_name)

