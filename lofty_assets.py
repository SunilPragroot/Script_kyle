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
driver.get('https://www.lofty.ai/account')
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
res = driver.page_source

soup = BeautifulSoup(res,'html.parser')
# time.sleep(5)
# assets_data = []


div_tag = soup.find_all('div', {'class':'px-6 sm:pl-6 sm:pr-0 w-full'})


for p_data in div_tag:

    address_data = []
    div_addres = p_data.find('div',{'class':'mb-0 mt-2 sm:mt-0 text-center sm:text-left flex flex-col sm:flex-row'})
    address_text = div_addres.text
    address_data.append(address_text)
    print(address_data)

    token_div = p_data.find('div',{'class':'sm:mr-8 flex flex-row sm:flex-col items-center sm:items-start min-w-140-px'})
    token_p = token_div.find('p',{'class':'flex-1 sm:flex-none text-right font-semibold ml-3 sm:ml-0'})
    tokens = token_p.text
    token_data = []
    token_data.append(tokens)
    print(token_data)

    cash_payment_data = []
    div_cash = p_data.find('div',{'class':'mr-8 hidden sm:flex flex-col'})
    cash_p = div_cash.find('p',{'class':'font-semibold'})
    cash_payment = cash_p.text
    cash_payment_data.append(cash_payment)
    print(cash_payment_data)

    # div_princi = p_data.find('div',{'class':'sm:mr-8 flex flex-row sm:flex-col items-center sm:items-start'})
    princi_value_data = []
    div_p_value = p_data.find('div',{'class':'flex-1 sm:flex-none flex justify-end font-semibold ml-3 sm:ml-0'})
    princi_val = div_p_value.text
    princi_value_data.append(princi_val)
    principal_value = princi_value_data[0][1:7]
    print([principal_value])
    
    
    div_rate = p_data.find('div',{'class':'hidden sm:flex'})
    div_p_cb = div_rate.find_all('p',{'class':'font-semibold'})

    current_balance_list = []
    current_bal = div_p_cb[0].text
    current_balance_list.append(current_bal)
    # print(current_bal,"current balance")
    print(current_balance_list)

    rental_income_list = []
    rental_inc = div_p_cb[1].text
    rental_income_list.append(rental_inc)
    # print(rental_inc,"rental income")
    print(rental_income_list)

        