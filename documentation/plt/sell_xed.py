from multiprocessing import Process
import os

def sell_xed_diff():
    os.system('python "C:/Users/radli/code/documentation/plt/sell_xed_diff.py"')

def sell_xed_price():
    os.system('python "C:/Users/radli/code/documentation/plt/sell_xed_price.py"')



if __name__ == '__main__':
    sell_xed_p1 = Process(target=sell_xed_diff)
    sell_xed_p2 = Process(target=sell_xed_price)
    sell_xed_p1.start()
    sell_xed_p2.start()
    sell_xed_p1.join()
    sell_xed_p2.join()
        
        