# -*- coding: utf-8 -*-
'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # “as” lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'meme.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 3)
# Show the image data in a subplot
ax[0].imshow(img)
ax[2].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[1].set_xlim(64,128)
ax[1].set_ylim(64,128)
ax[2].set_xlim(150,160)
ax[2].set_ylim(250,260)
ax[0].plot(225,150,'ro')
ax[0].plot(260,160,'ro')
ax[0].set_title('MEME')
ax[1].set_title('ZOOM')
ax[2].set_title('RANDOM TITLE HEAR')
# Show the figure on the screen
fig.show()