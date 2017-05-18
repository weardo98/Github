'''
Tkinter_tutorial.py demonstrates some of the standard widgets  
and the grid() geometry manager
'''
from Tkinter import *
root = Tk()

# A canvas widget
drawpad = Canvas(root, background='brown')
drawpad.grid(row=0, column=1)
item = drawpad.create_oval(10, 50, 100, 100, fill='green')

# A checkbox widget
box = Checkbutton(root, text="Check here.")
box.grid(row=0, column=0)


# An editor widget
editor = Text(width=30, height=4)
editor.grid(row=2, column=1, rowspan=2, sticky=SE)

# A button. This widget is demonstrating using an event handler with 
# the command argument
times_pressed = 0
def pressed():
    global times_pressed
    times_pressed = times_pressed + 1
    editor.insert(END, times_pressed)
    editor.see(END)
button = Button(root, text='Click me.', 
                command=pressed)
button.grid(row=1, column=0)

# Slider
speed = IntVar()
slider = Scale(root, from_=1, to=10, 
               label='Speed', variable=speed)
slider.grid(row=2, column=0)
speed.get()

# Radio buttons: you can only select one
radio = [0]*4 # create a list
data = IntVar()
for i in range(4):
    radio[i] = Radiobutton(root, text=str(i),
                           variable=data, value=i)
    radio[i].grid(row=i,column=2)
data.set(3)

root.mainloop()