import time
import os
import sys
from os import error, times
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

# from plyer import notification
from datetime import datetime
import csv
import sys
from pancakeswap_interface import *
from uniswap_interface import *
from webdriver_manager.chrome import ChromeDriverManager
from current_token_amount import get_current_token_amount

# from sold import just_sold
from error_notifier import *
from dotenv import load_dotenv

load_dotenv()


def just_bought(coin_name, toleranz):
    with open("should_i_die.txt", "w") as suicide:
        suicide.write("NO")

    def trigger(howMuchBRBCA, youget_BSCA, youget_RBCA, diffo, status, tokenname):

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
        # Make sure you also add new lines to your body
        if tokenname == "XED":
            body = (
                "For "
                + howMuchBRBCA
                + "XED you get: \n"
                + str(youget_BSCA)
                + " $ on Pancakeswap \n"
                + str(youget_RBCA)
                + " $ on Uniswap \n"
                + "The Difference is: "
                + str(diffo)
                + "$"
            )
        elif tokenname == "RBC":
            body = (
                "For "
                + howMuchBRBCA
                + "RBC you get: \n"
                + str(youget_BSCA)
                + " $ on Pancakeswap \n"
                + str(youget_RBCA)
                + " $ on Uniswap \n"
                + "The Difference is: "
                + str(diffo)
                + "$"
            )
        else:
            body = (
                "Eyo i ran into a string parsing error, but "
                + str(msg["Subject"])
                + " anyway :)"
            )
        # and then attach that body furthermore you can also send html content.
        msg.attach(MIMEText(body, "plain"))

        sms = msg.as_string()

        server.sendmail(email, sms_gateway, sms)

        # lastly quit the server
        server.quit()

    def dead(tokenname):

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
        if tokenname == "XED":
            body = "I'm dead, please restart\n" + "I'm the XED prgram btw..."
        elif tokenname == "RBC":
            body = "I'm dead, please restart\n" + "I'm the RBC prgram btw..."
        else:
            body = "I ran into some parsing error, but i died either way :)"
        # and then attach that body furthermore you can also send html content.
        msg.attach(MIMEText(body, "plain"))

        sms = msg.as_string()

        server.sendmail(email, sms_gateway, sms)

        # lastly quit the server
        server.quit()

    autotrade = "YES"
    howMuchBRBC = int(get_current_token_amount())
    howMuchBUSD = int(get_current_token_amount())
    howMuchBRBC = str(howMuchBRBC)
    howMuchBUSD = str(howMuchBUSD)

    if str(coin_name) == "XED":

        # inititalize:
        with open("transaction_status.txt", "w") as mystatus:
            mystatus.write("NO")

        header = ["row", "time", "price"]
        with open("sell_xed.csv", "w", encoding="UTF8", newline="") as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

        row_lauf = 0
        schmoney_string = "XED BUSD " + howMuchBRBC
        sell_toleranz = int(toleranz) - 60
        open("sell_xed_history.txt", "w").close()  # errase content

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
                "0x5621b5a3f4a8008c4ccdd1b942b121c8b1944f1f", howMuchBRBC, driver, True
            )
        except:
            sell_init_error()
            pancake_init_error()
            sys.exit()

        ##################################################################################################################

        # NEW WINDOW handling
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])

        try:
            uniswap_init(
                "0xee573a945b01b788b9287ce062a0cfc15be9fd86", howMuchBRBC, driver, True
            )
        except:
            sell_init_error()
            uniswap_init_error()
            sys.exit()

        try:
            while True:

                driver.switch_to.window(driver.window_handles[0])
                # Pancakeswap
                time.sleep(10)

                result1 = driver.find_element_by_xpath(
                    '//*[@id="swap-currency-output"]/div[2]/div/div[1]/div/input'
                )
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
                time.sleep(5)
                result2 = driver.find_element_by_xpath(
                    '//*[@id="swap-currency-output"]/div/div[1]/input'
                )
                youget_RBC2 = str(result2.get_attribute("value"))

                print(" ")
                print(" ")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(current_time)
                print("For " + howMuchBRBC + "XED you get:")
                print(youget_RBC1 + " $ on Pancakeswap")
                print(youget_RBC2 + " $ on Uniswap")

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

                # Statt:
                # youget_BSCm = float(youget_RBC1)
                # youget_RBCm = float(youget_RBC2)

                difference = float(youget_BSCm - youget_RBCm)
                diff = round(difference, 2)
                differenceSTR = str(diff)

                print("The Difference is: " + differenceSTR)
                if autotrade == "YES":
                    print("The trigger is at: " + str(sell_toleranz) + " (YES)")
                else:
                    print("The trigger is at: " + str(sell_toleranz) + " (NO)")
                # Pancakeswap
                driver.switch_to.window(driver.window_handles[0])

                with open("sell_xed_history.txt", "a") as myfile:
                    myfile.write("\n")
                    myfile.write("\n")
                    myfile.write(current_time + "\n")
                    myfile.write("For " + howMuchBRBC + "XED you get:\n")
                    myfile.write(youget_RBC1 + " $ on Pancakeswap\n")
                    myfile.write(youget_RBC2 + " $ on Uniswap\n")
                    myfile.write("The Difference is: " + differenceSTR + "\n")
                    if autotrade == "YES":
                        myfile.write(
                            "The trigger is at: " + str(sell_toleranz) + " (YES)"
                        )
                    else:
                        myfile.write(
                            "The trigger is at: " + str(sell_toleranz) + " (NO)"
                        )

                with open("should_i_die.txt", "r") as suicide:
                    should_i = suicide.read()
                if should_i == "YES":
                    died_intentionally()
                    time.sleep(30)
                    sys.exit()

                # csv management
                if difference > -1000:
                    with open("sell_xed.csv", "a", encoding="UTF8", newline="") as f:

                        data = [[row_lauf, current_time, difference]]
                        writer = csv.writer(f)

                        # write multiple rows
                        writer.writerows(data)

                schmoney_string_final = (
                    schmoney_string + " " + str(youget_RBC1) + " " + str(sell_toleranz)
                )

                if difference > float(220):
                    status = "BliBlaBlub"
                    trigger(howMuchBRBC, youget_RBC1, youget_RBC2, diff, status, "XED")

                    # Difference anpassbar
                elif difference > sell_toleranz:

                    if autotrade == "YES":
                        with open("swap_schmoney.txt", "w") as myfile:
                            myfile.write(schmoney_string_final)
                        os.system('node "C:/Users/radli/code/api_schmoney_maker.js"')
                        with open("transaction_status.txt", "r") as mystatus:
                            status = mystatus.read()
                    else:
                        status = "BliBlaBlub"

                    trigger(howMuchBRBC, youget_RBC1, youget_RBC2, diff, status, "XED")

                    if autotrade == "YES":
                        if status == "YES":
                            with open("should_i_die.txt", "w") as suicide:
                                suicide.write("YES")
                            driver.quit()
                            time.sleep(30)
                            sys.exit()

        except:
            print(error)
            print("sry Bro muss los")
            dead("XED")
            driver.quit()

    if str(coin_name) == "RBC":
        # inititalize:
        with open("transaction_status.txt", "w") as mystatus:
            mystatus.write("NO")

        header = ["row", "time", "price"]
        with open("sell_rbc.csv", "w", encoding="UTF8", newline="") as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

        row_lauf = 0
        schmoney_string = "RBC BUSD " + howMuchBRBC  # for the api later on
        sell_toleranz = int(toleranz) - 60

        open("sell_rbc_history.txt", "w").close()  # errase content
        # Chrome screen weg:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        chrome_options.add_argument("disable-gpu")
        chrome_options.add_argument("window-size=1920x1080")
        chrome_options.add_argument("--log-level=3")
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=chrome_options
        )

        pancakeswap_init(
            "0x8e3bcc334657560253b83f08331d85267316e08a", howMuchBRBC, driver, True
        )

        ##################################################################################################################

        # NEW WINDOW handling
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])

        uniswap_init(
            "0xa4eed63db85311e22df4473f87ccfc3dadcfa3e3", howMuchBRBC, driver, True
        )

        try:
            while True:

                driver.switch_to.window(driver.window_handles[0])
                # Pancakeswap
                time.sleep(10)

                result1 = driver.find_element_by_xpath(
                    '//*[@id="swap-currency-output"]/div[2]/div/div[1]/div/input'
                )
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
                print("For " + howMuchBRBC + "RBC you get:")
                print(youget_RBC1 + " $ on Pancakeswap")
                print(youget_RBC2 + " $ on Uniswap")

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

                # Statt:
                # youget_BSCm = float(youget_RBC1)
                # youget_RBCm = float(youget_RBC2)

                difference = float(youget_BSCm - youget_RBCm)
                diff = round(difference, 2)
                differenceSTR = str(diff)

                print("The Difference is: " + differenceSTR)
                if autotrade == "YES":
                    print("The trigger is at: " + str(sell_toleranz) + " (YES)")
                else:
                    print("The trigger is at: " + str(sell_toleranz) + " (NO)")
                    # Pancakeswap
                driver.switch_to.window(driver.window_handles[0])

                with open("sell_rbc_history.txt", "a") as myfile:
                    myfile.write("\n")
                    myfile.write("\n")
                    myfile.write(current_time + "\n")
                    myfile.write("For " + howMuchBRBC + "RBC you get:\n")
                    myfile.write(youget_RBC1 + " $ on Pancakeswap\n")
                    myfile.write(youget_RBC2 + " $ on Uniswap\n")
                    myfile.write("The Difference is: " + differenceSTR + "\n")
                    if autotrade == "YES":
                        myfile.write(
                            "The trigger is at: " + str(sell_toleranz) + " (YES)"
                        )
                    else:
                        myfile.write(
                            "The trigger is at: " + str(sell_toleranz) + " (NO)"
                        )

                with open("should_i_die.txt", "r") as suicide:
                    should_i = suicide.read()
                if should_i == "YES":
                    died_intentionally()
                    time.sleep(30)
                    sys.exit()

                # csv management
                if difference > -1000:
                    with open("sell_rbc.csv", "a", encoding="UTF8", newline="") as f:

                        data = [[row_lauf, current_time, difference]]
                        writer = csv.writer(f)

                        # write multiple rows
                        writer.writerows(data)

                schmoney_string_final = (
                    schmoney_string + " " + str(youget_RBC1) + " " + str(sell_toleranz)
                )

                # Difference anpassbar
                if difference > sell_toleranz:
                    if autotrade == "YES":
                        with open("swap_schmoney.txt", "w") as myfile:
                            myfile.write(schmoney_string_final)
                        os.system('node "C:/Users/radli/code/api_schmoney_maker.js"')
                        with open("transaction_status.txt", "r") as mystatus:
                            status = mystatus.read()
                    else:
                        status = "BliBlaBlub"

                    trigger(howMuchBRBC, youget_RBC1, youget_RBC2, diff, status, "RBC")

                    if autotrade == "YES":
                        if status == "YES":
                            with open("should_i_die.txt", "w") as suicide:
                                suicide.write("YES")
                            driver.quit()
                            time.sleep(30)
                            sys.exit()

        except:
            print("sry Bro muss los")
            dead("RBC")
            driver.quit()
