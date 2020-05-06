import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time




def obstruct(data):
   for i in range(270, 320):
        for j in range(300, 480):
          if  data[i, j]<100:
              pyautogui.keyDown("up")
              return True
   return False           
                    
    

if __name__ == "__main__":
    
    time.sleep(3)
    pyautogui.keyDown("up")
    while True:
       image = ImageGrab.grab().convert('L')  
       data = image.load()
       obstruct(data)
      
  
    #image.show()     

        
            
        


    
             
     
       