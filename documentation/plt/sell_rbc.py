from multiprocessing import Process
import os

def sell_rbc_diff():
    os.system('python "C:/Users/radli/code/documentation/plt/sell_rbc_diff.py"')

def sell_rbc_price():
    os.system('python "C:/Users/radli/code/documentation/plt/sell_rbc_price.py"')



if __name__ == '__main__':
    sell_rbc_p1 = Process(target=sell_rbc_diff)
    sell_rbc_p2 = Process(target=sell_rbc_price)
    sell_rbc_p1.start()
    sell_rbc_p2.start()
    sell_rbc_p1.join()
    sell_rbc_p2.join()
        
        