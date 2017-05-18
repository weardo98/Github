import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('gpu.jpg')
image = np.array(img)
hight = img.shape[0]
width = img.shape[1]

for y in range(hight):
    for x in range(width):
        if (y+x)/40%2==0:
            img[y][x]=[255,0,255]
fig, ax = plt.subplots()
ax.imshow(img)
fig.show()