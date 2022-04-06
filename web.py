import time
from lib2to3.pgen2 import driver
from selenium import webdriver
from asd import generator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

driver.get('https://magyarorszag.hu/jszp_szuf')

time.sleep(10)


ugyfelkapu_btn = driver.find_element_by_xpath(
    '//*[@id="urn:eksz.gov.hu:1.0:azonositas:kau:1:uk:uidpwd"]/input[4]')

ugyfelkapu_btn.click()

time.sleep(10)
user = driver.find_element_by_xpath('//*[@id="fldUser"]')
passwd = driver.find_element_by_xpath('//*[@id="fldPass"]')
login_btn = driver.find_element_by_xpath(
    '//*[@id="frmAktivacio"]/div[3]/button')

print('ugyfelkapu gomb')

time.sleep(4)

user.send_keys('sascsani')
passwd.send_keys('VGV2ZWt1dHlhMDU=')
time.sleep(1)
login_btn.click()

try:
    rendszam = WebDriverWait(driver, 7).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#input-rendszam')))
    print('found the element')
except:
    print('took too much time for rendszam')
try:
    search_btn = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
        (By.ID, 'button-kereses')))
except:
    print('took too much time for the search button')
time.sleep(.5)
search_btn.click()
