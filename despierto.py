# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:55:48 2021

@author: harim
"""

import pyautogui as gui, sys


if sys.argv[1].isnumeric():
    
    loops = 1
    while loops < (int(sys.argv[1])*3):
        gui.click(980,740)
        print("* Click *")
        gui.sleep(20)
        loops += 1
        if loops%3 == 0:
            print("Minute: {} / {}".format(int(loops/3), sys.argv[1]))

else:
    
    print("\nVALID COMMAND-LINE ARGUMENT REQUIERED:\n")
    print("[ 0-9+ ] --> number of MINUTES to keep the machine awake.\n")
