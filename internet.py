# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 08:43:54 2021

@author: harim
"""

import pyautogui as gui, requests, sys

def ConnectToWiFi (auto_connect):
    """Checks whether there is an internet connect and established it."""
        
    try:
        print("CHECKING FOR INTERNET CONNECTION...\n")
        print("SUCCESSFUL CONNECTION (STATUS CODE {})...\n".format(requests.get("http://216.58.192.142").status_code))
    
    except:
    
        print("CLIKING THE INTERNET ICON...\n")
        gui.click(1188,746)
        
        print("CLICKING THE FIRST AVAILABLE NETWORK...\n")
        gui.click(1060,180, duration=0.5)
    
        if auto_connect == True:
        
            print("CHECK THE AUTOMATIC CONNECTION BOX...\n")
            gui.click(1060, 230, duration=0.2)
            
        print("CONNECT TO THE NETWORK...\n")
        gui.click(1272, 273, duration=0.2)
        
        print("CLIKING THE INTERNET ICON AGAIN...\n")
        gui.click(1188,746)

    print("ALL SET!\n")
    sys.exit()


print()#######################################################################


if len(sys.argv) > 1:
    
    if sys.argv[1] in "automatic":

        ConnectToWiFi(auto_connect=True)
    
    else:
        
        print("\nNOTE: to click on the automatic connection box run internet.py [ automatic ] in the terminal.\n")
        
else:
    
    ConnectToWiFi(auto_connect=False)
    
