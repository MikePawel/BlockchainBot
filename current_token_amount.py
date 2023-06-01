import time
import os
from os import times
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import winsound
from datetime import datetime
import csv
import sys
from pancakeswap_interface import pancakeswap_init
from uniswap_interface import uniswap_init
from webdriver_manager.chrome import ChromeDriverManager
import re
from dotenv import load_dotenv
import os

load_dotenv()


def get_current_token_amount():
    # Chrome screen weg:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument("window-size=1920x1080")
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), chrome_options=chrome_options
    )  # insure for always newer versions

    partialStr = str(os.getenv("FROM_WALLET"))
    finStr = "https://bscscan.com/address/" + partialStr
    driver.get(finStr)
    driver.find_element_by_xpath('//*[@id="availableBalanceDropdown"]').click()
    x = driver.find_element_by_xpath(
        '//*[@id="mCSB_1_container"]/ul/li[2]/a/div[1]/span'
    ).get_attribute("innerHTML")
    x_copy = x
    # print(x)
    try:
        a = re.findall("\d+\,\d+", x)
        how_much_you_got = "".join([i for i in str(a[0]) if i.isdigit()])
    except:
        how_much_you_got = re.findall("\d+\.\d+", x_copy)
        how_much_you_got = float(how_much_you_got[0])
        how_much_you_got = int(how_much_you_got)
    driver.quit()

    return how_much_you_got


def get_current_token_name():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument("window-size=1920x1080")
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), chrome_options=chrome_options
    )  # insure for always newer versions

    driver.get("https://bscscan.com/address/0x18113D426BDCD08aA089c49CEc8DD5c1FFc7E1b1")
    driver.find_element_by_xpath('//*[@id="availableBalanceDropdown"]').click()
    x = driver.find_element_by_xpath(
        '//*[@id="mCSB_1_container"]/ul/li[2]/a/div[1]/span'
    ).get_attribute("innerHTML")
    name = "".join([i for i in str(x) if i.isalpha()])
    driver.quit()

    return name
