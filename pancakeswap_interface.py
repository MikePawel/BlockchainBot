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


def pancakeswap_init(address, howMuchMoney, driver, sell):
    try:

        # driver = webdriver.Chrome(ChromeDriverManager().install()) #FOR TESTING

        # Start openning:
        driver.get("https://pancakeswap.finance/swap#/swap")

        # Darkmode:
        settings = driver.find_element_by_xpath(
            '//*[@id="open-settings-dialog-button-SWAP_LIQUIDITY"]'
        )
        settings.click()

        # Flippy sound ausmachen:
        flippy = driver.find_element_by_xpath(
            '//*[@id="__next"]/div[1]/div[2]/div[2]/div/div[5]/div[2]'
        ).click()

        exitLightmode = driver.find_element_by_xpath(
            '//*[@id="__next"]/div[1]/div[2]/div[1]/button'
        )
        exitLightmode.click()
        # Darkmode ende


        coinOne = driver.find_element_by_xpath(
            '//*[@id="swap-currency-input"]/div[1]/div/button'
        )  # new change
        coinOne.click()
        time.sleep(1)
        busd = driver.find_element_by_xpath(
            '//*[@id="__next"]/div[1]/div[2]/div[2]/div[2]/div/div/div[5]/div[1]'
        )  # new change
        busd.click()
        coinTwo = driver.find_element_by_xpath(
            '//*[@id="swap-currency-output"]/div[1]/div/button/div/img'
        )  # new change
        coinTwo.click()

        manageToken = driver.find_element_by_xpath(
            '//*[@id="__next"]/div[1]/div[2]/div[2]/div[3]/button'
        )
        manageToken.click()

        tokens = driver.find_element_by_xpath(
            '//*[@id="__next"]/div[1]/div[2]/div[2]/div/div[1]/button[2]'
        )
        tokens.click()

        newCoinAdress = driver.find_element_by_xpath('//*[@id="token-search-input"]')
        newCoinAdress.send_keys(address)

        # time.sleep(20) #guessing that it needs 7 seconds to load
        # better: wait the exact time needed
        try:
            addNewCoinAdress = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="__next"]/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/button',
                    )
                )
            )
            addNewCoinAdress.click()
        except:
            driver.quit()

        confirm = driver.find_element_by_xpath(
            '//*[@id="__next"]/div[1]/div[2]/div[2]/div/div[3]/div/input'
        )
        confirm.click()

        finalconfirm = driver.find_element_by_xpath(
            '//*[@id="__next"]/div[1]/div[2]/div[2]/div/div[3]/button'
        )
        finalconfirm.click()

        if sell == True:
            # Buy/ sell swap:
            changeLocation = driver.find_element_by_xpath(
                '//*[@id="swap-page"]/div[1]/div[2]/div/button'
            ).click()

        busdAmount = driver.find_element_by_xpath(
            '//*[@id="swap-currency-input"]/div[2]/label/div[1]/input'
        )  # new change
        busdAmount.clear()
        busdAmount.send_keys(howMuchMoney)  # Wie viel Dollar man angeben möchte

        time.sleep(4)

        result1 = driver.find_element_by_xpath(
            '//*[@id="swap-currency-output"]/div[2]/label/div[1]/input'
        )  

        youget_BSC = str(result1.get_attribute("value"))

    except:
        pancake_init_error()
        sys.exit()
