# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 03:09:33 2024

@author: caitl
"""

import graphics 

WIDTH = 970
HEIGHT = 550

def initialize_window():
    # creates the canvas window for the graphics
    win = graphics.GraphWin("Surviving Smith",WIDTH,HEIGHT)
    # Sets the coordinate system
    win.setCoords(0,0, WIDTH, HEIGHT)
    
    #Sets the initial window as our logo image 
    logo_image = graphics.Image(graphics.Point(WIDTH/2, HEIGHT/2), "logo.png")
    logo_image.draw(win)


    return win
