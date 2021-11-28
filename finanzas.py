# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 22:20:10 2021

@author: harim
"""

import webbrowser as wb, pyautogui as gui, time , re, sys, pyperclip


mensual_link = "https://docs.google.com/spreadsheets/d/XXXXXXXXXXXX/edit#gid=0"
anual_link = "https://docs.google.com/spreadsheets/d/XXXXXXXXXXXX/edit#gid=XXXXXXX"


##############################################################################

def OpenSpreadsheet (name, link):
    """Opens or activates the web page on the browswer whetehr the given name is or not an active window."""
    
    ActWin = gui.getAllWindows()
    
    print("CHECK WHETHER Finanzas Spreadsheet IS OPEN OR NOT...\n")
    for item in ActWin:
    
        if re.search(name, item.title) != None:
    
            print("ACTIVATE THE WINDOW...\n")
            gui.getWindowsWithTitle(name)[0].activate()
            gui.click()
            time.sleep(0.2)
            break
    
        elif ActWin.index(item) == (len(ActWin)-1):    
    
            print("OPEN THE LINK OF THE GOOGLE SPREADSHEET...\n")
            wb.open(link)
    
            print("ASK FOR USER AUTHORIZATION TO CONTINUE...\n")
            time.sleep(3)
            gui.alert("Do you want to continue with the edit (" + str(sys.argv[1]) + ") ?")
  
    
def SearchKeyword (key, lag):
    """Searches the keyword inside the spreadsheet document."""
    
    print("SEARCH FOR THE KEYWORD IN THE DOC...\n") 
    gui.hotkey("ctrl", "f")
    gui.write(key, interval=lag)
    gui.press("esc")    
  
    
def DeleteVertically ():
    """Deletes the cells top-to-down until there is a cell purely alphbetic (a-zA-Z)."""
    
    print("DELETING THE CELLS VERTICALLY...\n")
    while True:
        gui.hotkey("ctrl", "c")
        if pyperclip.paste().isnumeric():
            gui.press("delete")
            gui.press("down")
        if pyperclip.paste().isspace():
            gui.press("down")
        if pyperclip.paste().isalpha():
            gui.press("esc")
            break    


def PrintCommands ():
    """Documentation when the script is run with no command-line arugments."""
    
    print("\nVALID COMMAND-LINE ARGUMENT REQUIERED:\n")
    print("[ mensual ] --> toma el numero copiado y lo pega")
    print("[ anual ] --> copia solo los datos de las celdas")
    print("[ default ] --> borra todos los valores de input \n")


print()########################################################################


if len(sys.argv) > 1:

    if sys.argv[1] in "anual":
        
        OpenSpreadsheet(r"Finanzas", anual_link)
        
        SearchKeyword(time.ctime()[4:7], 0.2) # searches the current month in three letter format
        
        print("COPY THE DATA FROM THE CELLS OF THE MONTH...\n")
        gui.press("down", presses=2, interval=0.2)
        gui.hotkey("shift", "right", "down", "down", interval=0.1)
        gui.hotkey("ctrl", "c", interval=0.1)
        
        print("PASTE THE CELLS IN PLACE AS VALUES ONLY...\n")
        gui.hotkey("ctrl", "shift", "v", interval=0.1)
        
        print("ALL SET!\n")
        sys.exit()
    
    elif sys.argv[1] in "mensual":
        
        OpenSpreadsheet(r"Finanzas", mensual_link)
        
        SearchKeyword("nom", 0.2)
        
        gui.press("tab", presses=2, interval=0.1)
        gui.press("enter")
    
        print("UNIFY THE FORMAT OF THE NUMBER COPIED...\n")
        paste = pyperclip.paste()
        money = "+"
        for number in paste:
            if number.isnumeric():
                money += number
            if number == '.':
                break
        
        print("PASTE THE DATA FROM THE CLIPBOARD...\n")
        pyperclip.copy(money)
        gui.press("home")
        gui.write("=")
        gui.press("end")
        gui.hotkey("ctrl", "v", interval=0.1)
        gui.press("enter")
        
        print("ALL SET!\n")
        sys.exit()
    
    elif sys.argv[1] in "default":
            
        OpenSpreadsheet(r"Finanzas", mensual_link)
        
        SearchKeyword("gastado", 0.1)
        
        gui.press("down")
        DeleteVertically()

        print("SEARCH FOR THE KEYWORD IN THE DOC...\n") 
        gui.hotkey("ctrl", "f")
        gui.write("gastado", interval=0.1)
        gui.press("enter") # this line prevents the use of the SearchKeyword function
        gui.press("esc") 
        
        gui.press("down")
        DeleteVertically()
        
        SearchKeyword("ingresado", 0.1)
        
        gui.press("down")
        DeleteVertically()        
        
        print("ALL SET!\n")
        sys.exit()
        
    else:
        
        PrintCommands()
        sys.exit()
        
else:
    
    PrintCommands()
    sys.exit()