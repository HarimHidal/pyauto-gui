# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:36:18 2021

@author: harim
"""

import pyautogui as gui 

print()

print("CLICK ON WINDOWS ICON...\n")
gui.click(19,745, duration=0.3)

print("CLICK ON SETTINGS ICON...\n")
gui.click(25,654, duration=0.3)

print("SELECT BLUETOOTH...\n")
gui.click(404,358, duration=0.6)

print("CLICK ON THE FORONRE DEVICE...\n")
gui.click(400,370, duration=1.8)

print("SELECT REMOVE...\n")
gui.click(699,435, duration=0.3)
gui.sleep(1.2)

print("CLICK ON ADD DEVICE...\n")
gui.click(363,137, duration=0.3)

print("SELECT A BLUETOOTH DEVICE...\n")
gui.click(498,185, duration=0.3)

