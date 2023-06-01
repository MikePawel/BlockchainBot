from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from error_notifier import *
import os
import sys


def uniswap_init(address, howMuchMoney, driver, sell):

    try:
        driver.get("https://app.uniswap.org/#/swap")

        time.sleep(3)
        firstCoin = driver.find_element_by_xpath(
            '//*[@id="swap-currency-input"]/div/div[1]/button'
        ).click()

        getUSDT = driver.find_element_by_xpath(
            "/html/body/reach-portal[3]/div[3]/div/div/div/div/div[1]/div[3]/div/div[4]"
        ).click()
        time.sleep(3)
        secondCoin = driver.find_element_by_xpath(
            '//*[@id="swap-currency-output"]/div/div/button'
        ).click()

        if str(address) == "0xa4eed63db85311e22df4473f87ccfc3dadcfa3e3":
            tosend = "RBC"
            getRBC3 = driver.find_element_by_xpath(
                '//*[@id="token-search-input"]'
            ).send_keys(tosend)

            time.sleep(1)
            driver.find_element_by_xpath(
                "/html/body/reach-portal[3]/div[3]/div/div/div/div/div[3]/div[1]/div/div/div[1]"
            ).click()

            time.sleep(1)
        else:
            tosend = "XED"
            driver.find_element_by_xpath(
                "/html/body/reach-portal[3]/div[3]/div/div/div/div/div[4]/div/button"
            ).click()
            driver.find_element_by_xpath(
                "/html/body/reach-portal[3]/div[3]/div/div/div/div/div[3]/div/div[2]"
            ).click()
            driver.find_element_by_xpath('//*[@id="token-search-input"]').send_keys(
                str(address)
            )
            time.sleep(1)
            driver.find_element_by_xpath(
                "/html/body/reach-portal[3]/div[3]/div/div/div/div/div[4]/div[1]/div[1]/div[2]/div/button"
            ).click()
            driver.find_element_by_xpath(
                "/html/body/reach-portal[3]/div[3]/div/div/div/div/div[3]/button"
            ).click()

        if sell == True:
            uniChangeLocation = driver.find_element_by_xpath(
                '//*[@id="swap-page"]/div[2]/div[1]/div[2]'
            ).click()

        time.sleep(1)
        insertUSDT = driver.find_element_by_xpath(
            '//*[@id="swap-currency-input"]/div/div[1]/input'
        )
        insertUSDT.clear()
        insertUSDT.send_keys(howMuchMoney)

        time.sleep(8)

        result2 = driver.find_element_by_xpath(
            '//*[@id="swap-currency-output"]/div/div/input'
        )
        youget_RBC = str(result2.get_attribute("value"))
    except:
        uniswap_init_error()
        sys.exit()
