from current_token_amount import *
from error_notifier import buy_init_error
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from os import times
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import winsound

# from plyer import notification #asd
from datetime import datetime
import csv
import sys
from pancakeswap_interface import pancakeswap_init
from uniswap_interface import uniswap_init
from error_notifier import *
from dotenv import load_dotenv

load_dotenv()


def get_auto_buy_rbc(trade):
    with open("should_i_die.txt", "w") as suicide:
        suicide.write("NO")
    if trade == True:
        autotrade = "YES"
    elif trade == False:
        autotrade = "NO"
    else:
        buy_init_error()
        sys.exit()
    howMuchBRBC = int(get_current_token_amount())
    howMuchBUSD = int(get_current_token_amount())

    if autotrade == "NO":
        howMuchBRBC = float(2200)
        howMuchBUSD = float(2200)

    if howMuchBRBC <= 2240:
        toleranz = 94
    elif howMuchBRBC <= 2340:
        toleranz = 100
    elif howMuchBRBC <= 2440:
        toleranz = 106
    elif howMuchBRBC <= 2540:
        toleranz = 112
    else:
        toleranz = 118

    buy_toleranz = float(toleranz)
    howMuchBUSD = str(howMuchBUSD)
    howMuchBRBC = str(howMuchBRBC)

    schmoney_string = "BUSD RBC " + howMuchBUSD  # for the api later on

    # inititalize:
    with open("transaction_status.txt", "w") as mystatus:
        mystatus.write("NO")

    header = ["row", "time", "price"]
    with open("buy_rbc.csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

    row_lauf = 0
    open("buy_rbc_history.txt", "w").close()  # errase content

    # Chrome screen weg:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument("window-size=1920x1080")
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), chrome_options=chrome_options
    )

    try:
        pancakeswap_init(
            "0x8e3bcc334657560253b83f08331d85267316e08a", howMuchBUSD, driver, False
        )
    except:
        buy_init_error()
        pancake_init_error()
        sys.exit()

    # NEW WINDOW handling
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get("https://app.uniswap.org/#/swap")

    try:
        uniswap_init(
            "0xa4eed63db85311e22df4473f87ccfc3dadcfa3e3", howMuchBUSD, driver, False
        )
    except:
        buy_init_error()
        uniswap_init_error()
        sys.exit()

    # Difference anpassbar (Wie viel CoinUnterschied WICHTIG: NOTATION: >"zahl")
    def trigger(dex1, dex2, fin, priceChange, status):

        youget_BSC = dex1
        youget_RBC = dex2
        differenceSTR = fin
        pricePrint = priceChange

        email = "skastradingalert@gmail.com"
        pas = os.getenv("EMAIL_PAS")

        sms_gateway = "radlinski.mikolaj@gmail.com"
        smtp = "smtp.gmail.com"
        port = 587
        server = smtplib.SMTP(smtp, port)
        server.starttls()
        server.login(email, pas)

        # Now we use the MIME module to structure our message.
        msg = MIMEMultipart()
        msg["From"] = email
        msg["To"] = sms_gateway
        if status == "YES":
            msg["Subject"] = "I SWAPPED!!!\n"
        elif status == "NO":
            msg["Subject"] = "I DIDN'T SWAP!!!\n"
        elif status == "SLIPPAGE":
            msg["Subject"] = "SLIPPAGE KICKED IN :///\n"
        else:
            msg["Subject"] = "PRICE CHANGE!!!\n"

        body = (
            "For "
            + howMuchBUSD
            + "$ you get: \n"
            + str(youget_BSC)
            + " RBC on Pancakeswap\n"
            + str(youget_RBC)
            + " RBC on Uniswap \n"
            + "The Difference is: "
            + str(pricePrint)
            + "$ ("
            + str(differenceSTR)
            + "RBC)"
        )
        # and then attach that body furthermore you can also send html content.
        msg.attach(MIMEText(body, "plain"))

        sms = msg.as_string()

        server.sendmail(email, sms_gateway, sms)
        server.quit()

    def dead():

        email = "skastradingalert@gmail.com"
        pas = os.getenv("EMAIL_PAS")

        sms_gateway = "radlinski.mikolaj@gmail.com"
        smtp = "smtp.gmail.com"
        port = 587
        server = smtplib.SMTP(smtp, port)
        server.starttls()
        server.login(email, pas)

        # Now we use the MIME module to structure our message.
        msg = MIMEMultipart()
        msg["From"] = email
        msg["To"] = sms_gateway
        msg["Subject"] = "EYO I DIEAD :(\n"
        body = "I'm dead, please restart\n" + "I'm the RBC prgram btw..."
        # and then attach that body furthermore you can also send html content.
        msg.attach(MIMEText(body, "plain"))

        sms = msg.as_string()

        server.sendmail(email, sms_gateway, sms)
        server.quit()

    ##################################################################################################################

    try:
        while True:
            # Pancakeswap
            driver.switch_to.window(driver.window_handles[0])

            time.sleep(10)

            result1 = driver.find_element_by_xpath(
                '//*[@id="swap-currency-output"]/div[2]/div/div[1]/div/input'
            )  # new change
            youget_RBC1 = str(result1.get_attribute("value"))

            # current coin price
            coinP = driver.find_element_by_xpath(
                '//*[@id="swap-page"]/div[1]/div[4]/div[1]/div[2]'
            ).text
            coinPrice = float(coinP.split()[0])

            # Uniswap
            driver.switch_to.window(driver.window_handles[1])
            clicken = driver.find_element_by_xpath("//body").click()
            for i in range(4):
                clicken

            time.sleep(7)
            result2 = driver.find_element_by_xpath(
                '//*[@id="swap-currency-output"]/div/div[1]/input'
            )
            youget_RBC2 = str(result2.get_attribute("value"))

            print(" ")
            print(" ")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(current_time)
            # new print:
            print("For " + howMuchBUSD + "$ you get:")
            print(youget_RBC1 + " RBC on Pancakeswap")
            print(youget_RBC2 + " RBC on Uniswap")

            # Falls Pancakeswap mies Probleme macht:
            try:
                youget_BSCm = float(youget_RBC1)
            except:
                youget_BSCm = float(-1000000000)

            # Falls uniswap mies Probleme macht:
            try:
                youget_RBCm = float(youget_RBC2)
            except:
                youget_RBCm = float(1000000000)

            difference = float(youget_BSCm - youget_RBCm)
            diff = round(difference, 2)
            differenceSTR = str(diff)

            diff_in_dollaros1 = coinPrice * diff
            diff_in_dollaros = round(diff_in_dollaros1, 2)
            diffDstring = str(diff_in_dollaros)
            coinPriceS = str(coinPrice)

            print("The Difference is: " + diffDstring + "$ (" + differenceSTR + "RBC)")
            if autotrade == "YES":
                print("The trigger is at: " + str(buy_toleranz) + " (YES)")
            else:
                print("The trigger is at: " + str(buy_toleranz) + " (NO)")

            with open("buy_rbc_history.txt", "a") as myfile:
                myfile.write("\n")
                myfile.write("\n")
                myfile.write(current_time + "\n")
                myfile.write("For " + howMuchBUSD + "$ you get:\n")
                myfile.write(youget_RBC1 + " RBC on Pancakeswap\n")
                myfile.write(youget_RBC2 + " RBC on Uniswap\n")
                myfile.write(
                    "The Difference is: "
                    + diffDstring
                    + "$ ("
                    + differenceSTR
                    + "RBC)\n"
                )
                if autotrade == "YES":
                    myfile.write("The trigger is at: " + str(buy_toleranz) + " (YES)")
                else:
                    myfile.write("The trigger is at: " + str(buy_toleranz) + " (NO)")

            with open("should_i_die.txt", "r") as suicide:
                should_i = suicide.read()
            if should_i == "YES":
                died_intentionally()
                time.sleep(30)
                sys.exit()

            # csv management
            if diff_in_dollaros > -1000:
                with open("buy_rbc.csv", "a", encoding="UTF8", newline="") as f:

                    data = [[row_lauf, current_time, diff_in_dollaros]]
                    writer = csv.writer(f)

                    # write multiple rows
                    writer.writerows(data)

            schmoney_string_final = (
                schmoney_string + " " + str(youget_RBC1) + " " + str(buy_toleranz)
            )

            # Hier diff anpassen:
            if diff_in_dollaros > buy_toleranz:
                if autotrade == "YES":
                    with open("swap_schmoney.txt", "w") as myfile:
                        myfile.write(schmoney_string_final)
                    os.system('node "C:/Users/radli/code/api_schmoney_maker.js"')
                    with open("transaction_status.txt", "r") as mystatus:
                        status = mystatus.read()
                else:
                    status = "BliBlaBlub"

                trigger(
                    youget_RBC1, youget_RBC2, differenceSTR, diff_in_dollaros, status
                )

                if autotrade == "YES":
                    if status == "YES":
                        with open("should_i_die.txt", "w") as suicide:
                            suicide.write("YES")
                        driver.quit()
                        time.sleep(30)
                        sys.exit()

    except:
        print("sry Bro muss los")
        dead()
        driver.quit()
