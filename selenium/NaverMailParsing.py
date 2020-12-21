from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import random
import requests
import pyperclip


driver = webdriver.Chrome()
driver.get("https://www.naver.com")
elem = driver.find_element_by_class_name("link_login").click()
time.sleep(0.5)


def copy_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
    time.sleep(1)

id = 'hyp3252'
pw = 'gusdyd321!'

copy_input('//*[@id="id"]', id)
copy_input('//*[@id="pw"]', pw)

driver.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(0.5)


from bs4 import BeautifulSoup #웹 페이지의 소스코드를 파싱하기 위해 bs 라이브러리를 불러온다.

driver.get("https://mail.naver.com")
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

title_list = soup.find_all('strong','mail_title') #메일 제목을 하나씩 파싱한다.


for title in title_list:
    print(title.text) # 전체 메일을 순회하며 출력