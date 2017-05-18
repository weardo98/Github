#####
# radius_changer.py
# 
# Creates a Scale and a Canvas. Updates a circle based on the Scale.
# (c) 2013 PLTW
# version 11/1/2013
####

import Tkinter #often people import Tkinter as *

#####
# Create root window 
####
root = Tkinter.Tk()

#####
# Create Model
######
radius_intvar = Tkinter.IntVar()
radius_intvar.set(100) #initialize radius
# center of circle
x = 640 
y = 512

######
# Create Controller
#######
# Event handler for slider
def radius_changed(new_intval):
    # Get data from model
    # Could do this: r = int(new_intval)
    r = radius_intvar.get()
    # Controller updating the view
    canvas.coords(circle_item, x-x, y-r, x+x, y+r)
# Instantiate and place slider
radius_slider = Tkinter.Scale(root, from_=1, to=360, variable=radius_intvar,    
                              label='Radius', command=radius_changed)
radius_slider.grid(row=1, column=0, sticky=Tkinter.W)
# Create and place directions for the user
text = Tkinter.Label(root, text='Drag slider \nto adjust\ncircle.')
text.grid(row=0, column=0)

######
# Create View
#######
# Create and place a canvas
canvas = Tkinter.Canvas(root, width=1280, height=1024, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)

# Create a circle on the canvas to match the initial model
r = radius_intvar.get()
circle_item = canvas.create_oval(x-r, y-y, x+r, y+y, 
                                 outline='#000000', fill='#00FFFF')
#######
# Event Loop
#######
root.mainloop()