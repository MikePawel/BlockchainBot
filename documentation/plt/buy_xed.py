from multiprocessing import Process
import os

def buy_xed_diff():
    os.system('python "C:/Users/radli/code/documentation/plt/buy_xed_diff.py"')

def buy_xed_price():
    os.system('python "C:/Users/radli/code/documentation/plt/buy_xed_price.py"')



if __name__ == '__main__':
    buy_xed_p1 = Process(target=buy_xed_diff)
    buy_xed_p2 = Process(target=buy_xed_price)
    buy_xed_p1.start()
    buy_xed_p2.start()
    buy_xed_p1.join()
    buy_xed_p2.join()
        
        