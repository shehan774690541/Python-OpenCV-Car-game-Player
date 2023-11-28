import numpy as np
from PIL import ImageGrab 
import cv2
import time

last_time = time.time()
while (True):
    printscreen_pli = ImageGrab.grab(bbox=(0, 100, 800, 640))
    printscreem_numpy = np.array(printscreen_pli.getdata(), dtype='uint8')\
    .reshape((printscreen_pli.size[1], printscreen_pli.size[0],3))
    cv2.imshow('window', printscreem_numpy)
    if cv2.waitKey(25) & 0xFF == ord('q') :
        cv2.destroyAllWindows()
        break
    