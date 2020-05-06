from PIL import Image, ImageGrab
import time

time.sleep(2)
image = ImageGrab.grab().convert('L')  
data = image.load()
for i in range(270, 320):
        for j in range(300, 480):
         data[i, j]=150

image.show()
