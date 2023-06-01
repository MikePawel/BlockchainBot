from multiprocessing import Process
import os

def buy_rbc_diff():
    os.system('python "C:/Users/radli/code/documentation/plt/buy_rbc_diff.py"')

def buy_rbc_price():
    os.system('python "C:/Users/radli/code/documentation/plt/buy_rbc_price.py"')



if __name__ == '__main__':
    buy_rbc_p1 = Process(target=buy_rbc_diff)
    buy_rbc_p2 = Process(target=buy_rbc_price)
    buy_rbc_p1.start()
    buy_rbc_p2.start()
    buy_rbc_p1.join()
    buy_rbc_p2.join()
        
        