# ListenerByPuusepp

import win32api
import time
import sys
import win32con
from easygui import *

# TODO: osades arvutites hiirega valimine ei tööta - kogu salvestus läheb katki.

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

nupud = ["Alusta", "Help"]
vajutati = buttonbox("Programmeerimine on ", choices = nupud)
if vajutati == "Help":
    vajutati = buttonbox("vasak vottab koordinaadid ", choices = ["Alusta"])

if vajutati == "Alusta":
    # Viivita sekund salvestuse algusega
    time.sleep(1)
    
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
    

    """
    Kood võtab ekraani koordinaadid kuhu hiirega vajutan ja siis salvestab need järjendisse.
    """
    salvestatud = []
    viivitus = []
    
    start = time.clock()
    
    while True:
        new_left_click, new_right_click = win32api.GetKeyState(0x01), win32api.GetKeyState(0x02)

        if new_left_click != state_left:  # Button state changed
            state_left = new_left_click
            
            if new_left_click < 0:
                x, y = win32api.GetCursorPos()
                salvestatud.append((x, y))
                print(x, y)
                
                end = time.clock()
            
                viivitus.append((end-start))
                
                start = time.clock()
            
        if new_right_click != state_right:  # Button state changed
            state_right = new_right_click
            if new_right_click < 0:
                break
        # Salvestuse viivitus
        time.sleep(0.001)


    """
    Annab valiku sul koodi mangima hakkata
    """

    nupud = ["Play"]
    vajutati = buttonbox("Koordinaadid salvestatud. Vajuta play nuppu et alustada mängimist ", choices = nupud)

    time.sleep(1)

    for i in range(len(salvestatud)):
        time.sleep(viivitus[i])
        coord = salvestatud[i]
        click(coord[0],coord[1])
        
    
    #for (end-start) in viivitus:
