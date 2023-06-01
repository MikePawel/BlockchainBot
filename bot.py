from multiprocessing import Process
from auto_buy_xed import*
from auto_buy_rbc import*
from bought import*
from current_token_amount import*
import time
from error_notifier import*
import os

def autoswap_rbc():
    os.system('node autoswap_js/autoswap_rbc.js')    

def autoswap_xed():
    os.system('node autoswap_js/autoswap_xed.js')

def autoswap_sell_rbc():
    os.system('node autoswap_js/autoswap_sell_rbc.js')

def autoswap_sell_xed():
    os.system('node autoswap_js/autoswap_sell_xed.js')



if __name__ == '__main__':
    while True:


        with open("txt/suicide.txt", "w") as myfile:
            myfile.write('NO')

        os.system("node C:/Users/radli/code/autoswap_js/wallet/wallet_info.js")
        with open("C:/Users/radli/code/autoswap_js/wallet/wallet_info.txt", "r") as myfile:
            current_token = myfile.read()
        name = current_token.split(' ')
        name = name[1]

        buy_rbc = Process(target=autoswap_rbc)
        buy_xed = Process(target=autoswap_xed)
        sell_rbc = Process(target=autoswap_sell_rbc)
        sell_xed = Process(target=autoswap_sell_xed)
        if name=='BUSD':
            buy_rbc.start()
            buy_xed.start()
            buy_rbc.join()
            buy_xed.join()
        elif name=='RBC':
            sell_rbc.start()
            sell_rbc.join() 
        elif name=='XED':
            sell_xed.start()
            sell_xed.join()
        else:
            setup_init_error('DiesDas')
            sys.exit()
        
        time.sleep(15)
        setting_up()
        