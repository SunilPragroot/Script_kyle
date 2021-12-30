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
import re

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('start-maximized')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('disable-infobars')


driver=webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.get('https://www.lofty.ai/account/history')
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
driver.get('https://www.lofty.ai/account/history')
time.sleep(10)
res = driver.page_source
soup = BeautifulSoup(res,'html.parser')

a_tag = soup.find_all('a',{'class':'inline-flex items-center space-x-2 truncate text-sm hover:text-themeBlue-400'})
for anc in a_tag:
    urls = "https://www.lofty.ai"+str(anc.get('href'))
    driver.get(urls)
    time.sleep(10)
    res = driver.page_source
    soup = BeautifulSoup(res,'html.parser')

    # section_tag = soup.find('section',{'class':'flex flex-col mt-7.5 font-proxima'})
    # div_tag = section_tag.find('div',{'class':'mb-4 font-medium mr-0 lg:mr-6 lg:min-w-300-px'})
    # span_investment = div_tag.find('span',{'class':'flex items-center cursor-pointer'})
    # print(span_investment.text)

    total_investment_data = []
    total_investment=soup.find('span',{'class':'flex items-center cursor-pointer'})
    # print(total_investment.text)
    investment_d = re.sub("[A-Za-z:]","", total_investment.text)
    total_investment_data.append(investment_d)
    # print(total_investment_data)
    
    div=soup.find('div',{'class':'flex flex-col flex-wrap lg:flex-row justify-between'})
    all_ul=div.find_all('li')

    # all_ul_data = []
    # all_ul_data.append(all_ul.text)
    # print(all_ul[3].text)

    underlying_asset_price_data = []
    underlying_asset_price = all_ul[0].text
    underlying_ap = re.sub("[A-Za-z:]","", underlying_asset_price)
    underlying_asset_price_data.append(underlying_ap)
    # print(underlying_asset_price_data)

    closing_costs_data = []
    closing_costs = all_ul[1].text
    closing_c = re.sub("[A-Za-z:]","", closing_costs)
    closing_costs_data.append(closing_c)
    # print(closing_costs_data)

    city_transfer_tax_data = []
    ctt_data = all_ul[2].text
    ctt_list = ctt_data.split(':')
    # print(ctt_list[0])
    if (ctt_list[0]=='City Transfer Tax'):
        # print(ctt_list[1])
        city_transfer_tax_data.append(ctt_list[1])
        # print(city_transfer_tax_data)
        # print(all_ul[2].text)
        pass
    else:
        # print('N/A')
        pass

    Upfront_llc_administration_and_filing_fees_data = []
    upfront_llc_2 = all_ul[2].text
    upfront_llc_2_list = upfront_llc_2.split(':')
    # print(upfront_llc_2)

    upfront_llc_3 = all_ul[3].text
    upfront_llc_3_list = upfront_llc_3.split(':')
    # print(upfront_llc_3_list[0])

    if(upfront_llc_2_list[0]=='Upfront LLC administration and filing fees'):
        Upfront_llc_administration_and_filing_fees_data.append(upfront_llc_2_list[1])
        # print(Upfront_llc_administration_and_filing_fees_data)  
        pass 
    elif(upfront_llc_3_list[0]=='Upfront LLC administration and filing fees'):
        Upfront_llc_administration_and_filing_fees_data.append(upfront_llc_3_list[1])
        # print(Upfront_llc_administration_and_filing_fees_data)
        pass
    else:
        # print('N/A')
        pass

    Initial_maintenance_reserve_data = []
    initial_mr_3 = all_ul[3].text
    initial_mr_3_list = initial_mr_3.split(':')
    initial_mr_3_list_zi = initial_mr_3_list[0]
    initial_mr_3_list_text = initial_mr_3_list_zi.split('(')
    # print(initial_mr_3_list[1])

    initial_mr_4 = all_ul[4].text
    initial_mr_4_list = initial_mr_4.split(':')
    initial_mr_4_list_zi = initial_mr_4_list[0]
    initial_mr_4_list_text = initial_mr_4_list_zi.split('(')
    # print(initial_mr_4_list_text[0])

    # if(initial_mr_3_list_text[0]=='Initial maintenance reserve '):
    #     Initial_maintenance_reserve_data.append(initial_mr_3_list[1])
    #     print(Initial_maintenance_reserve_data)
    # elif(initial_mr_4_list_text[0]=='Initial maintenance reserve '):
    #     Initial_maintenance_reserve_data.append(initial_mr_4_list[1])
    #     print(Initial_maintenance_reserve_data)
    # else:
    #     print('N/A')


    Lofty_ai_listing_fee_data = []
    lofty_alf_4 = all_ul[4].text
    lofty_alf_4_list = lofty_alf_4.split(':')
    lofty_alf_4_list_zi = lofty_alf_4_list[0]
    lofty_alf_4_list_text = lofty_alf_4_list_zi.split('(')
    # print(lofty_alf_4_list_text[0])

    lofty_alf_5 = all_ul[5].text
    lofty_alf_5_list = lofty_alf_5.split(':')
    lofty_alf_5_list_zi = lofty_alf_5_list[0]
    lofty_alf_5_list_text = lofty_alf_5_list_zi.split('(')
    # print(lofty_alf_5_list_text[0])


    if lofty_alf_5_list_text[0]=='Lofty AI listing fee ':
        print('hello')
    else:
        print('N/A')

    # if lofty_alf_4_list_text[0]=='Lofty AI listing fee ':
    #     print(lofty_alf_4_list[1])
    # elif lofty_alf_5_list_text[0]=='Lofty AI listing fee ':
    #     print(lofty_alf_5_list[1])
    # else:
    #     print('N/A')


    city_transfer_tax = re.sub("[A-Za-z:]","", ctt_data)
    # print(ctt_data)

    for i in all_ul:
        # invest_list_data = []
        # data_list = re.sub("[A-Za-z:]","", i.text)
        # print(data_list.split())
        # invest_list_data.append(data_list)
        # print(invest_list_data)
        pass

    token_price_data = []
    div_prc = div.find_all('div',{'class':'mb-4 font-medium mr-0 lg:mr-6 lg:min-w-300-px'})[1].text
    token_price = re.sub("[A-Za-z:]","", div_prc)
    token_price_data.append(token_price)
    # print(token_price_data)

    total_token_data = []
    total_token = div.find_all('div',{'class':'mb-4 font-medium mr-0 lg:mr-6 lg:min-w-300-px'})[2].text
    # print(total_token)

    token_data=re.sub("[A-Za-z:]","", total_token)
    total_token_data.append(token_data)
    # print(total_token_data)

    # time.sleep(10)
